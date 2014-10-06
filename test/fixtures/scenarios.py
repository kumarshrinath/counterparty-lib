from .params import ADDR, MULTISIGADDR, DEFAULT_PARAMS as DP

UNITEST_FIXTURE = [
    ['burn', (ADDR[0], DP['burn_quantity']), {'encoding': 'multisig'}],
    ['issuance', (ADDR[0], None, 'DIVISIBLE', DP['quantity'] * 1000, True, False, None, None, 'Divisible asset'), {'encoding': 'multisig'}],
    ['issuance', (ADDR[0], None, 'NODIVISIBLE', 1000, False, False, None, None, 'No divisible asset'), {'encoding': 'multisig'}],
    ['issuance', (ADDR[0], None, 'CALLABLE', 1000, True, True, 1409400251, DP['quantity'], 'Callable asset'), {'encoding': 'multisig'}],
    ['issuance', (ADDR[0], None, 'LOCKED', 1000, True, False, None, None, 'Locked asset'), {'encoding': 'multisig'}],
    ['issuance', (ADDR[0], None, 'LOCKED', 0, True, False, None, None, 'LOCK'), {'encoding': 'multisig'}],
    ['order', (ADDR[0], 'XCP', DP['quantity'], 'DIVISIBLE', DP['quantity'], 2000, 0), {'encoding': 'multisig'}],
    ['send', (ADDR[0], ADDR[1], 'DIVISIBLE', DP['quantity']), {'encoding': 'multisig'}],
    ['send', (ADDR[0], ADDR[1], 'XCP', DP['quantity']), {'encoding': 'multisig'}],
    ['order', (ADDR[0], 'XCP', DP['quantity'], 'DIVISIBLE', DP['quantity'], 2000, 0), {'encoding': 'multisig'}],
    ['order', (ADDR[0], 'XCP', DP['quantity'], 'BTC', round(DP['quantity'] / 100), 2000, DP['fee_required']), {'encoding': 'multisig'}],
    ['order', (ADDR[0], 'BTC', round(DP['quantity'] / 150), 'XCP', DP['quantity'], 2000, 0), {'encoding': 'multisig', 'fee_provided': DP['fee_provided']}],
    ['send', (ADDR[0], MULTISIGADDR[0], 'XCP', DP['quantity'] * 3), {'encoding': 'multisig'}],
    ['create_next_block', 490],
    ['order', (ADDR[0], 'XCP', DP['quantity'], 'BTC', round(DP['quantity'] / 125), 2000, DP['fee_required']), {'encoding': 'multisig'}],
    ['order', (ADDR[1], 'BTC', round(DP['quantity'] / 125), 'XCP', DP['quantity'], 2000, 0), {'encoding': 'multisig', 'fee_provided': DP['fee_provided']}],
    ['create_next_block', 500]
]

SCENARIO_1 = [
    ['burn', (ADDR[0], int(.62 * DP['quantity'])), {'encoding': 'multisig'}],
    ['send', (ADDR[0], ADDR[1], 'XCP', DP['small']), {'encoding': 'multisig'}],
    ['order', (ADDR[0], 'BTC', DP['small'], 'XCP', DP['small'] * 2, DP['expiration'], 0), {'encoding': 'multisig', 'fee_provided': DP['fee_provided']}],
    ['order', (ADDR[0], 'XCP', round(DP['small'] * 2.1), 'BTC', DP['small'], DP['expiration'], DP['fee_required']), {'encoding': 'multisig'}],
    ['btcpay', (ADDR[0], 'b7a20fda89961cb1f3632fae11960769eb215b67092ab93911de977459c5b04cd646f64fb17ee3dc83700fae7d1155d2e2a7de1f634dd7dbd57fe7246f13f140'), {'encoding': 'multisig'}],
    ['issuance', (ADDR[0], None, 'BBBB', DP['quantity'] * 10, True, False, 0, 0.0, ''), {'encoding': 'multisig'}],
    ['issuance', (ADDR[0], None, 'BBBC', round(DP['quantity'] / 1000), False, True, 17, 0.015, 'foobar'), {'encoding': 'multisig'}],
    ['send', (ADDR[0], ADDR[1], 'BBBB', round(DP['quantity'] / 25)), {'encoding': 'multisig'}],
    ['send', (ADDR[0], ADDR[1], 'BBBC', round(DP['quantity'] / 190000)), {'encoding': 'multisig'}],
    ['dividend', (ADDR[0], 600, 'BBBB', 'XCP'), {'encoding': 'multisig'}],
    ['dividend', (ADDR[0], 800, 'BBBC', 'XCP'), {'encoding': 'multisig'}],
    ['broadcast', (ADDR[0], 1388000000, 100, DP['fee_multiplier'], 'Unit Test'), {'encoding': 'multisig'}],
    ['bet', (ADDR[0], ADDR[0], 0, 1388000100, DP['small'], round(DP['small'] / 2), 0.0, 15120, DP['expiration']), {'encoding': 'multisig'}],
    ['bet', (ADDR[0], ADDR[0], 1, 1388000100, round(DP['small'] / 2), round(DP['small'] * .83), 0.0, 15120, DP['expiration']), {'encoding': 'multisig'}],
    ['bet', (ADDR[0], ADDR[0], 0, 1388000100, DP['small'] * 3, DP['small'] * 7, 0.0, 5040, DP['expiration']), {'encoding': 'multisig'}],
    ['bet', (ADDR[0], ADDR[0], 1, 1388000100, DP['small'] * 7, DP['small'] * 3, 0.0, 5040, DP['expiration']), {'encoding': 'multisig'}],
    ['bet', (ADDR[0], ADDR[0], 2, 1388000200, DP['small'] * 15, DP['small'] * 13, 1, 5040, DP['expiration']), {'encoding': 'multisig'}],
    ['bet', (ADDR[0], ADDR[0], 3, 1388000200, DP['small'] * 13, DP['small'] * 15, 1, 5040, DP['expiration']), {'encoding': 'multisig'}],
    ['broadcast', (ADDR[0], 1388000050, round(100 - (.415/3) - .00001, 5), DP['fee_multiplier'], 'Unit Test'), {'encoding': 'multisig'}],
    ['broadcast', (ADDR[0], 1388000101, 100.343, DP['fee_multiplier'], 'Unit Test'), {'encoding': 'multisig'}],
    ['broadcast', (ADDR[0], 1388000201, 2, DP['fee_multiplier'], 'Unit Test'), {'encoding': 'multisig'}],
    ['order', (ADDR[0], 'BBBB', DP['small'], 'XCP', DP['small'], DP['expiration'], 0), {'encoding': 'multisig'}],
    ['burn', (ADDR[0], (1 * DP['quantity']), True), {'encoding': 'multisig'}],  # Try to burn a whole 'nother BTC.
    ['send', (ADDR[0], ADDR[1], 'BBBC', 10000), {'encoding': 'multisig'}],
    ['callback', (ADDR[0], .3, 'BBBC'), {'encoding': 'multisig'}],
    ['rps', (ADDR[0], 5, 11021663, DP['move_random_hash'], 100), {'encoding': 'multisig'}],
    ['rps', (ADDR[1], 5, 11021663, '6e8bf66cbd6636aca1802459b730a99548624e48e243b840e0b34a12bede17ec', 100), {'encoding': 'multisig'}],
    ['rpsresolve', (ADDR[0], 3, DP['rps_random'], 'a54b7aea0e6875394b5ab938ab15a3b81f01303eedc7b726602357480e90cc90af5c2e5c41e84fbf96a7d03a5ae740552c4611786dc112826c75f147f1cd13eb'), {'encoding': 'multisig'}],
    ['rpsresolve', (ADDR[1], 5, 'fa765e80203cba24a298e4458f63ff6b', 'a54b7aea0e6875394b5ab938ab15a3b81f01303eedc7b726602357480e90cc90af5c2e5c41e84fbf96a7d03a5ae740552c4611786dc112826c75f147f1cd13eb'), {'encoding': 'multisig'}],
    ['rps', (ADDR[0], 5, 11021663, DP['move_random_hash'], 10), {'encoding': 'multisig'}],
    ['create_next_block', 46],
    ['rps', (ADDR[0], 5, 11021664, DP['move_random_hash'], 10), {'encoding': 'multisig'}],
    ['rps', (ADDR[1], 5, 11021664, DP['move_random_hash'], 10), {'encoding': 'multisig'}],
    ['create_next_block', 73],
    ['rps', (ADDR[0], 5, 11021665, DP['move_random_hash'], 10), {'encoding': 'multisig'}],
    ['rps', (ADDR[1], 5, 11021665, DP['move_random_hash'], 10), {'encoding': 'multisig'}],
    ['rpsresolve', (ADDR[0], 3, DP['rps_random'], '2501cd2ee7e1c5f407e970b75a05ccbee4be74e605781de5dd3a6838a165f7bf72fe4a5e983752587b92edbb5da26c67c7f2968d2dde2e0f930acfce1ab9b669'), {'encoding': 'multisig'}],
    ['create_next_block', 101]
]

SCENARIO_2 = [
    ['burn', (MULTISIGADDR[0], int(.62 * DP['quantity'])), {'encoding': 'multisig'}],
    ['send', (MULTISIGADDR[0], MULTISIGADDR[1], 'XCP', DP['small']), {'encoding': 'multisig'}],
    ['order', (MULTISIGADDR[0], 'BTC', DP['small'], 'XCP', DP['small'] * 2, DP['expiration'], 0), {'encoding': 'multisig', 'fee_provided': DP['fee_provided']}],
    ['order', (MULTISIGADDR[0], 'XCP', round(DP['small'] * 2.1), 'BTC', DP['small'], DP['expiration'], DP['fee_required']), {'encoding': 'multisig'}],
    ['btcpay', (MULTISIGADDR[0], '3f995494228c67860250b3ab0decf77e9467fed9dc15dbd278ddf3f9aef0acd2a667e44ce48fcd05a74130bd8cf564486a3017b8afb24fa369249d77f21bd253'), {'encoding': 'multisig'}],
    ['issuance', (MULTISIGADDR[0], None, 'BBBB', DP['quantity'] * 10, True, False, 0, 0.0, ''), {'encoding': 'multisig'}],
    ['issuance', (MULTISIGADDR[0], None, 'BBBC', round(DP['quantity'] / 1000), False, True, 17, 0.015, 'foobar'), {'encoding': 'multisig'}],
    ['send', (MULTISIGADDR[0], MULTISIGADDR[1], 'BBBB', round(DP['quantity'] / 25)), {'encoding': 'multisig'}],
    ['send', (MULTISIGADDR[0], MULTISIGADDR[1], 'BBBC', round(DP['quantity'] / 190000)), {'encoding': 'multisig'}],
    ['dividend', (MULTISIGADDR[0], 600, 'BBBB', 'XCP'), {'encoding': 'multisig'}],
    ['dividend', (MULTISIGADDR[0], 800, 'BBBC', 'XCP'), {'encoding': 'multisig'}],
    ['broadcast', (MULTISIGADDR[0], 1388000000, 100, DP['fee_multiplier'], 'Unit Test'), {'encoding': 'multisig'}],
    ['bet', (MULTISIGADDR[0], MULTISIGADDR[0], 0, 1388000100, DP['small'], round(DP['small'] / 2), 0.0, 15120, DP['expiration']), {'encoding': 'multisig'}],
    ['bet', (MULTISIGADDR[0], MULTISIGADDR[0], 1, 1388000100, round(DP['small'] / 2), round(DP['small'] * .83), 0.0, 15120, DP['expiration']), {'encoding': 'multisig'}],
    ['bet', (MULTISIGADDR[0], MULTISIGADDR[0], 0, 1388000100, DP['small'] * 3, DP['small'] * 7, 0.0, 5040, DP['expiration']), {'encoding': 'multisig'}],
    ['bet', (MULTISIGADDR[0], MULTISIGADDR[0], 1, 1388000100, DP['small'] * 7, DP['small'] * 3, 0.0, 5040, DP['expiration']), {'encoding': 'multisig'}],
    ['bet', (MULTISIGADDR[0], MULTISIGADDR[0], 2, 1388000200, DP['small'] * 15, DP['small'] * 13, 1, 5040, DP['expiration']), {'encoding': 'multisig'}],
    ['bet', (MULTISIGADDR[0], MULTISIGADDR[0], 3, 1388000200, DP['small'] * 13, DP['small'] * 15, 1, 5040, DP['expiration']), {'encoding': 'multisig'}],
    ['broadcast', (MULTISIGADDR[0], 1388000050, round(100 - (.415/3) - .00001, 5), DP['fee_multiplier'], 'Unit Test'), {'encoding': 'multisig'}],
    ['broadcast', (MULTISIGADDR[0], 1388000101, 100.343, DP['fee_multiplier'], 'Unit Test'), {'encoding': 'multisig'}],
    ['broadcast', (MULTISIGADDR[0], 1388000201, 2, DP['fee_multiplier'], 'Unit Test'), {'encoding': 'multisig'}],
    ['order', (MULTISIGADDR[0], 'BBBB', DP['small'], 'XCP', DP['small'], DP['expiration'], 0), {'encoding': 'multisig'}],
    ['burn', (MULTISIGADDR[0], int(.62 * DP['quantity']), True), {'encoding': 'multisig'}],  # Try to burn a whole 'nother BTC.
    ['send', (MULTISIGADDR[0], MULTISIGADDR[1], 'BBBC', 10000), {'encoding': 'multisig'}],
    ['callback', (MULTISIGADDR[0], .3, 'BBBC'), {'encoding': 'multisig'}],
    ['rps', (MULTISIGADDR[0], 5, 11021663, DP['move_random_hash'], 100), {'encoding': 'multisig'}],
    ['rps', (MULTISIGADDR[1], 5, 11021663, '6e8bf66cbd6636aca1802459b730a99548624e48e243b840e0b34a12bede17ec', 100), {'encoding': 'multisig'}],
    ['rpsresolve', (MULTISIGADDR[0], 3, DP['rps_random'], '08dd31a576fc835a651c7ce8818bf80a3c16b973ec5055ae5f6b1c75567c9e33dcc4b9ea7e9b98d2c9376c7a3240b7019de79bd0074039d652d27781b6a13011'), {'encoding': 'multisig'}],
    ['rpsresolve', (MULTISIGADDR[1], 5, 'fa765e80203cba24a298e4458f63ff6b', '08dd31a576fc835a651c7ce8818bf80a3c16b973ec5055ae5f6b1c75567c9e33dcc4b9ea7e9b98d2c9376c7a3240b7019de79bd0074039d652d27781b6a13011'), {'encoding': 'multisig'}],
    ['rps', (MULTISIGADDR[0], 5, 11021663, DP['move_random_hash'], 10), {'encoding': 'multisig'}],
    ['create_next_block', 46],
    ['rps', (MULTISIGADDR[0], 5, 11021664, DP['move_random_hash'], 10), {'encoding': 'multisig'}],
    ['rps', (MULTISIGADDR[1], 5, 11021664, DP['move_random_hash'], 10), {'encoding': 'multisig'}],
    ['create_next_block', 73],
    ['rps', (MULTISIGADDR[0], 5, 11021665, DP['move_random_hash'], 10), {'encoding': 'multisig'}],
    ['rps', (MULTISIGADDR[1], 5, 11021665, DP['move_random_hash'], 10), {'encoding': 'multisig'}],
    ['rpsresolve', (MULTISIGADDR[0], 3, DP['rps_random'], '640f166066e9396abc163df5826a5184631fbccb470ce0724ef3349ed452fb62ce4d806a2f6266051585fc979e3a89f4c7b6a18ea0b41f51bfb26336137c4f26'), {'encoding': 'multisig'}],
    ['create_next_block', 101]
]

INTEGRATION_SCENARIOS = {
    'unittest_fixture': UNITEST_FIXTURE,
    'scenario_1': SCENARIO_1,
    'scenario_2': SCENARIO_2
}
