import hashlib
from . import rsa


def generate_Pk_and_pk(p, q):

    # Generating public and private keys.
    # (In RSA anyone can encrypt and only one can decrypt. For this anyone can decrypt and only one can encrypt. This is why the key names are reversed.)
    pk, Pk = rsa.generate_Pk_and_pk(p, q)

    return(Pk, pk)


def sign_string(string, pk):

    # Create hash object.
    h = hashlib.new("sha512_256")
    h.update(string.encode())

    # Return hash encrypted with private key.
    return(rsa.encrypt_string(h.hexdigest(), pk))


def verify_signature(digital_signature, string, Pk):

    # Decrypt signature with public key.
    _hash = rsa.decrypt_string(digital_signature, Pk)

    # Create hash object.
    h = hashlib.new("sha512_256")
    h.update(string.encode())

    # Determine if signature is valid (Valid if hashes match) and then return answer.
    if _hash == h.hexdigest():

        return(True)

    else:

        return(False)
