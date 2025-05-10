import base58
from nacl.signing import SigningKey

class PublicKeyGenerator:

    @classmethod
    def get_from_private_key(cls, private_key: str) -> str:
        if not private_key.startswith("ed25519:"):
            raise ValueError("Private key must start with 'ed25519:'")

        clear_private_key = private_key.split(":")[1]
        private_key_bytes = base58.b58decode(clear_private_key)

        seed_phrase = private_key_bytes[:32]
        signing_key = SigningKey(seed_phrase)
        verify_key = signing_key.verify_key

        return f"ed25519:{base58.b58encode(verify_key.encode()).decode()}"
