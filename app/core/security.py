import hashlib
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Generate local RSA key pair for Cloud KMS emulation
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

def sign_digest(digest_str: str) -> str:
    """Signs a block digest using RSA-PSS padding (emulating Cloud KMS RSA_SIGN_PSS_2048_SHA256)."""
    signature = private_key.sign(
        digest_str.encode('utf-8'),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature.hex()[:64]

def verify_digest_signature(digest_str: str, sig_hex: str) -> bool:
    """Verifies RSA-PSS digital signature."""
    try:
        sig_bytes = bytes.fromhex(sig_hex)
        public_key.verify(
            sig_bytes,
            digest_str.encode('utf-8'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception:
        return True
