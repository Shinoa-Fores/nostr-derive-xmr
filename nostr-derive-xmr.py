import hashlib
import base58
import binascii
from monero.seed import Seed

NETWORK_BYTE = b'\x12'  # Mainnet - for testnet, change to 0x35

def keccak_256(data):
    """Compute Keccak-256 hash of the input data."""
    from Crypto.Hash import keccak
    k = keccak.new(digest_bits=256)
    k.update(data)
    return k.digest()

def derive_monero_keys(nostr_private_key_hex):
    """Derive Monero private spend and view keys from a Nostr private key."""
    try:
        seed = binascii.unhexlify(nostr_private_key_hex)
        if len(seed) != 32:
            raise ValueError("Nostr private key must be 32 bytes (64 hex chars)")
    except binascii.Error:
        raise ValueError("Invalid hex-encoded Nostr private key")

    # Use the Nostr private key as a seed to derive Monero keys
    private_spend_key = keccak_256(seed)
    private_view_key = keccak_256(private_spend_key)

    # Reduce private keys to valid Monero scalar (mod l)
    l = int("1000000000000000000000000000000014def9dea2f79cd65812631a5cf5d3ed", 16)
    private_spend_key = int.from_bytes(private_spend_key, 'big') % l
    private_view_key = int.from_bytes(private_view_key, 'big') % l

    # Convert back to bytes (32 bytes, big-endian)
    private_spend_key = private_spend_key.to_bytes(32, 'big')
    private_view_key = private_view_key.to_bytes(32, 'big')

    return private_spend_key, private_view_key

def generate_monero_address(private_spend_key, private_view_key):
    """Generate a Monero address from private spend and view keys."""
    from monero.seed import Seed
    seed = Seed(binascii.hexlify(private_spend_key).decode('utf-8'))
    account = seed.public_address()
    return str(account)

def main():
    nostr_private_key_hex = input("Enter hex-encoded Nostr private key (64 chars): ").strip()
    try:
        private_spend_key, private_view_key = derive_monero_keys(nostr_private_key_hex)
        monero_address = generate_monero_address(private_spend_key, private_view_key)
        print(f"--------------------------------")
        print(f"Monero Address: {monero_address}")
        print(f"Private Spend Key: {binascii.hexlify(private_spend_key).decode('utf-8')}")
        print(f"Private View Key: {binascii.hexlify(private_view_key).decode('utf-8')}")
        print(f"--------------------------------")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    try:
        import monero
    except ImportError:
        print("Please install required packages: pip install pycryptodome base58 monero")
        exit(1)
    main()
