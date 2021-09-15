# Coded for clarity not efficiency

# Importing python_rsa module
import python_rsa


# Getting user message
print("Enter message to be encrypted.")
message = input("> ")
print("")
print("")


# Generating key pairs
Pk, pk = python_rsa.generate_Pk_and_pk(757, 887)

# Converting message to unicode
unicode_message = [ord(character) for character in message]

# Encrypting unicode message
encrypted_unicode_message = [python_rsa.encrypt(character, Pk) for character in unicode_message]

# Decrypting unicode message
decrypted_unicode_message = [python_rsa.decrypt(character, pk) for character in encrypted_unicode_message]

# Generating string from decrypted unicode message
decrypted_message = ""
for character in decrypted_unicode_message:

    decrypted_message += chr(character)


# Giving user basic information
print("Basic Information:")
print("")
print(" Original message: " + message)
print("")
print(" Decrypted message: " + decrypted_message)
print("")
print("")

# Giving user advanced information
print("Advanced Information:")
print("")
print(" Public key: " + str(Pk))
print("")
print(" Private key: " + str(pk))
print("")
print(" Unicode message: " + str(unicode_message))
print("")
print(" Encrypted unicode message: " + str(encrypted_unicode_message))
print("")
print(" Decrypted unicode message: " + str(decrypted_unicode_message))

