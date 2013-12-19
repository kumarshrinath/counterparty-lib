#! /usr/bin/python3

import binascii
import struct
import sqlite3

from . import (util, bitcoin)

FORMAT = '>32s32s'
ID = 11

def btcpayment (deal_id):
    tx0_hash, tx1_hash = deal_id[:64], deal_id[64:] # UTF‐8 encoding means that the indices are doubled.
    tx0_hash_bytes, tx1_hash_bytes = binascii.unhexlify(tx0_hash), binascii.unhexlify(tx1_hash)
    data = config.PREFIX + struct.pack(config.TXTYPE_FORMAT, ID)
    data += struct.pack(FORMAT, tx0_hash_bytes, tx1_hash_bytes)

    db = sqlite3.connect(LEDGER)
    db.row_factory = sqlite3.Row
    cursor = db.cursor()

    cursor.execute('''SELECT * FROM deals \
                      WHERE (tx0_hash=? AND tx1_hash=?)''',
                   (tx0_hash, tx1_hash))
    deal = cursor.fetchone()
    assert not cursor.fetchone()
    try:
        if not deal['backward_id']:
            source = deal['tx1_address']
            destination = deal['tx0_address']
            btc_amount = deal['backward_amount']
        else:
            source = deal['tx0_address']
            destination = deal['tx1_address']
            btc_amount = deal['forward_amount']
        if source == destination:
            raise exceptions.UselessError('You’re trying to buy from yourself!')
    except TypeError:
        raise exceptions.InvalidDealError('Invalid Deal ID:', deal_id)

    return bitcoin.transaction(source, destination, btc_amount, config.MIN_FEE, data)

def parse_btcpayment (db, cursor, tx, message):
    # Ask for forgiveness…
    validity = 'Valid'

    # Unpack message.
    try:
        tx0_hash_bytes, tx1_hash_bytes = struct.unpack(FORMAT, message)
        tx0_hash, tx1_hash = binascii.hexlify(tx0_hash_bytes).decode('utf-8'), binascii.hexlify(tx1_hash_bytes).decode('utf-8')
    except Exception:
        tx0_hash, tx1_hash = None, None
        validity = 'Invalid: could not unpack'

    cursor.execute('''SELECT * FROM deals WHERE (tx0_hash=? AND tx1_hash=?)''', (tx0_hash, tx1_hash))
    deal = cursor.fetchone()
    assert not cursor.fetchone()
    if not deal: return db, cursor
    # Credit source address for the currency that he bought with the bitcoins.
    # BTC must be paid all at once and come from the ‘correct’ address.
    if deal['tx0_address'] == tx['source'] and tx['btc_amount'] >= deal['forward_amount']:
        cursor.execute('''UPDATE deals SET validity=? WHERE (tx0_hash=? AND tx1_hash=?)''', ('Valid', tx0_hash, tx1_hash))
        db.commit()
        if deal['backward_id']:    # Gratuitous
            db, cursor = credit(db, cursor, tx['source'], deal['backward_id'], deal['backward_amount'])
    if deal['tx1_address'] == tx['source'] and tx['btc_amount'] >= deal['backward_amount']:
        cursor.execute('''UPDATE deals SET validity=? WHERE (tx0_hash=? AND tx1_hash=?)''', ('Valid', tx0_hash, tx1_hash))
        if deal['forward_id']:     # Gratuitous
            db, cursor = util.credit(db, cursor, tx['source'], deal['forward_id'], deal['forward_amount'])

    deal_id = tx0_hash + tx1_hash
    print('\tBTC payment for deal:', deal_id, '(' + tx['tx_hash'] + ')')

    return db, cursor

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4