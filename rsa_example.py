from python_rsa import rsa

# Getting user message.
print("Enter message to be encrypted.")
message = input("> ")
print("")

# Doing RSA stuff.
Pk, pk = rsa.generate_Pk_and_pk(11, 13)
encrypted_message = rsa.encrypt_string(message, Pk)
decrypted_message = rsa.decrypt_string(encrypted_message, pk)

# Giving user information.
print("Original message: " + message)
print("")
print("Encrypted message: " + str(encrypted_message))
print("")
print("Decrypted message: " + decrypted_message)

