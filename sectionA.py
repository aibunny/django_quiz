import hashlib

def hash_using_md5(input_text:str)->str:
	md5 = hashlib.md5()
	md5.update(input_text.encode("utf-8"))
	hashed_string = md5.hexdigest()
	return hashed_string

#example 
md5_hash = hash_using_md5("Hello InterIntel")
print(f"MD5 HASH: {md5_hash} \n")


def hash_using_sha256(input_text:str)->str:
    sha256 = hashlib.sha256()
    sha256.update(input_text.encode("utf-8"))
    hashed_string= sha256.hexdigest()
    return hashed_string

# Example
sha256_hash = hash_using_sha256("Hello InterIntel")
print(f"SHA-256 HASH: {sha256_hash} \n")

######################################################### FERNET #######################################

from cryptography.fernet import Fernet
#TODO: Run pip install cryptography

def hash_decrypt_using_fernet(
    input_text:str, key:str
    ) -> tuple[str,str]:
    ##fernet uses an encrption key to 
    #encrypt so i passed it in as a parameter
    cipher = Fernet(key)
    hashed_string = cipher.encrypt(input_text.encode('utf-8'))
    decrypted_string = cipher.decrypt(hashed_string).decode('utf-8')
    return hashed_string, decrypted_string

# generate encrption key
key = Fernet.generate_key()
message = "Hello InterIntel"

hashed_string, fernet_decrypted_string = hash_decrypt_using_fernet(message, key)
print(f"KEY {key}")
print(f"FERNET HASH: {hashed_string}")
print(f"decrypted_string : {fernet_decrypted_string} \n")


######################################################### RSA #######################################
from cryptography.hazmat.primitives import serialization,hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

def encrypt_decrypt_rsa(input_string: str) -> tuple[str, str]:
    # Generate private and public keys
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    public_key = private_key.public_key()
    
    # Serialize private key to PEM format
    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ).decode('utf-8')

    # Serialize public key to PEM format
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode('utf-8')

    print(f"Private Key (PEM format):\n{private_key_pem}")
    print(f"Public Key (PEM format):\n{public_key_pem}")

    # Encrypt using the public key
    hash_algorithm = hashes.SHA256()
    mgf = padding.MGF1(algorithm=hash_algorithm)
    hashed_string = public_key.encrypt(
        input_string.encode('utf-8'),
        padding.OAEP(
            mgf=mgf,
            algorithm=hash_algorithm,
            label=None
        )
    )

    # Decrypt using the private key
    decrypted_string = private_key.decrypt(
        hashed_string,
        padding.OAEP(
            mgf=mgf,
            algorithm=hash_algorithm,
            label=None
        )
    ).decode('utf-8')

    return hashed_string, decrypted_string

# Example
message = "Hello InterIntel"

rsa_hash, rsa_decrypted_string = encrypt_decrypt_rsa(message)
print("RSA HASH:", rsa_hash)
print("RSA decrypted string:", rsa_decrypted_string)