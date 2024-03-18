# -*- coding: utf-8 -*-

"""doctopt bitcoin address convert tool

Usage:
  genaddr.py priv2addr      <private>

Options:
  -h --help                                             Show this screen.
  --version                                             Show version.

Example:

    genaddr.py priv2addr 0000000000000000000000000000000000000000000000000000000000000001 # gen address from private 0x0000000000000000000000000000000000000000000000000000000000000001=>1BgGZ9tcN4rm9KBzDn7KprQz87SZ26SAMH
"""

import base58
import binascii
import hashlib
import fileinput
import sys
from pycoin import ecdsa, encoding
from docopt import docopt
from bip32utils import Base58


def hash160(x): # Both accepts & returns bytes
    return hashlib.new('ripemd160', hashlib.sha256(x).digest()).digest()

def parse_wif(private_key_WIF):
    first_encode = base58.b58decode(private_key_WIF)
    private_key_full = binascii.hexlify(first_encode)
    private_key = private_key_full[2:-8]
    print('private: ', private_key.upper().decode('utf-8'))


def gen_address(private_key, compressed=True):
    # private_key = codecs.encode(os.urandom(32), 'hex').decode()
    secret_exponent = int('0x' + private_key, 0)
    wif = encoding.secret_exponent_to_wif(secret_exponent, compressed=compressed)
    print('WIF: ' + encoding.secret_exponent_to_wif(secret_exponent, compressed=compressed))
    public_pair = ecdsa.public_pair_for_secret_exponent(ecdsa.secp256k1.generator_secp256k1, secret_exponent)
    #print('public pair:', public_pair)
    hash160 = encoding.public_pair_to_hash160_sec(public_pair, compressed=compressed)
    print("hash160: {}".format(hash160.hex()))
    return(
        encoding.hash160_sec_to_bitcoin_address(
            hash160, address_prefix=b'\0'
        ),
        (hash160.hex(), wif)
    )


def gen_address_from_160(hash160):
    return encoding.hash160_sec_to_bitcoin_address(bytes.fromhex(hash160))


def decode(addr):
    return encoding.bitcoin_address_to_hash160_sec(addr).hex()


def sha256(pharse):
    return hashlib.sha256(pharse).hexdigest()



if __name__ == '__main__':
    arguments = docopt(__doc__, version='genaddr 1.0')

    if arguments['priv2addr']:
        key = arguments['<private>']
        if len(key) < 32:
            key = '0' * (32 - len(key)) + key
        print('private:', key)
        print('compress address')
        address, _ = gen_address(key)
        print("Bitcoin address: {}".format(address))
        print('uncompress address')
        address, _ = gen_address(key, False)
        print("Bitcoin address: {}".format(address))
