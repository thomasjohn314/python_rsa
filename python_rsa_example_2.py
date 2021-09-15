# Importing python_rsa module
import python_rsa


# Getting user message
print("Enter message to be encrypted.")
msg = input("> ")
print("")
print("")


# Generating key pairs
Pk, pk = python_rsa.generate_Pk_and_pk(757, 887)

# Encrypting message
encrypted_msg = [python_rsa.encrypt(ord(char), Pk) for char in msg]

# Decrypting message
decrypted_msg = "".join([chr(python_rsa.decrypt(char, pk)) for char in encrypted_msg])


# Giving user basic information
print("Basic Information:")
print("")
print(" Original message: " + msg)
print("")
print(" Decrypted message: " + decrypted_msg)
print("")
print("")

# Giving user advanced information
print("Advanced Information:")
print("")
print(" Public key: " + str(Pk))
print("")
print(" Private key: " + str(pk))
print("")
print(" Encrypted message: " + str(encrypted_msg))

