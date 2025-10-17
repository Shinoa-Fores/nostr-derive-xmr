# nostr-derive-xmr

If you use <a href="https://github.com/wujifoo/nostr-bip-85-prototype/tree/main">bip-85</a> and derive keys from these you can have infinite wallets all derived from you master key.

Install dependencies:

```
pip3 install pycryptodome base58 monero

```

Run application. You will be asked to provide your hex encoded private key to proceed, as shown in the example below:


```
#python3 nostr-derive-xmr.py
Enter hex-encoded Nostr private key (64 chars): 66522599e02d44f8116569843e534b87e36657f873b56a93bd0618ec1a2b50b0
--------------------------------
Monero Address: 456P4Jvx8vCZ8dak4JfgTiNBUPUnwXuxcJSuyVDzJp7Bi5cWQXfj6cYPhvQAQMxKmChUyokUiv5sW22cviw8AS5bNRJQBKS
Private Spend Key: 0140a5edfa89a1b45c09e668dd66359722ed4d1fa2e8853edd42d57c59d51539
Private View Key: 0509a4f544a4a10e0143ba329c98204edaa3f2f00fc5c71584ebb4db272822ac
--------------------------------

```
