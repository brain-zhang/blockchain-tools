## Install

```
pip install -r reqirements.txt
```


## RUN
```
$ python3 genaddr.py priv2addr 0000000000000000000000000000000000000000000000000000000000000001

private: 0000000000000000000000000000000000000000000000000000000000000001
compress address
WIF: KwDiBf89QgGbjEhKnhXJuH7LrciVrZi3qYjgd9M7rFU73sVHnoWn
hash160: 751e76e8199196d454941c45d1b3a323f1433bd6
Bitcoin address: 1BgGZ9tcN4rm9KBzDn7KprQz87SZ26SAMH
uncompress address
WIF: 5HpHagT65TZzG1PH3CSu63k8DbpvD8s5ip4nEB3kEsreAnchuDf
hash160: 91b24bf9f5288532960ac687abb035127b1d28a5
Bitcoin address: 1EHNa6Q4Jz2uvNExL497mE43ikXhwF6kZm
```


## FAQ

if raise Error

```
Traceback (most recent call last):
  File "/mnt/d/project/brainzhang/blockchain-tools/genaddr.py", line 22, in <module>
    from pycoin import ecdsa, encoding
  File "/home/ubuntu/.local/lib/python3.10/site-packages/pycoin/encoding.py", line 57, in <module>
    from Crypto.Hash.RIPEMD import RIPEMD160Hash as ripemd160
ImportError: cannot import name 'RIPEMD160Hash' from 'Crypto.Hash.RIPEMD' 
```

fix:

https://stackoverflow.com/questions/72409563/unsupported-hash-type-ripemd160-with-hashlib-in-python

