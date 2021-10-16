inp = [0, 0, 0, 0, 0, 0, 0, 0, 0]

out = [0, 0, 0, 0, 0, 0, 0, 0, 0]

results = []

memory = [
    'a_cdefaijkltmnop',
    'wzstueabez012000',
    '67890ABCDEFGHIJK',
    'nooodtdvw000eta?',
    'T!VW00Y!ETA?*-+/',
    '{}[]=&%£"!()abcd',
    'efghijklmnopqrsA',
    'BCDEFGHIJKLNMuuu',
    'vwxipsilonnnnnnz',
    '%%/9876543210|!"',
    '£$ohdear!%&/((((',
    ')*;:_AAAABSIDEOW',
    'abcdefghijklmnop',
    'qrstuvwxyz012345',
    '678?8?8?8?9!!!!!',
    'EGIN.CERTIFICATE',
    'a_cdefaijkltmnop',
    'wzstueabez012000',
    '67890ABCDEFGHIJK',
    'nooodtdvw000eta?',
    'T!VW00Y!ETA?*-+/',
    '{}[]=&%£"!()abcd',
    'efghijklmnopqrsA',
    'BCDEFGHIJKLNMuuu',
    'vwxipsilonnnnnnz',
    '%%/9876543210|!"',
    '£$ohdear!%&/((((',
    ')*;:_AAAABSIDEOW',
    'abcdefghijklmnop',
    'qrstuvwxyz012345',
    '678?8?8?8?9!!!!!',
    'EGIN.CERTIFICATE'
]

import sys

for i in range(10):
    out[7] = inp[7] & inp[1]
    out[6] = inp[5] ^ inp[0]
    out[8] = inp[8] ^ out[6]
    out[5] = inp[0]
    out[3] = inp[3] ^ inp[4] ^ inp[2]
    out[4] = inp[0] | (not inp[5]) | out[3]
    out[2] = inp[6] ^ ((inp[3] & inp[4]) | (inp[2] & (inp[4] ^ inp[3])))
    out[0] = inp[8] ^ out[2] 
    out[1] = inp[5]

    results.append("0b"+"".join(str(x) for x in out[::-1]))

    inp[:] = out[:]


print("{FLG:" + "".join(memory[int(x,2)//16][int(x,2)%16] for x in results) + "}")
