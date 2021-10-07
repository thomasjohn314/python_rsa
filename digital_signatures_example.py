from python_rsa import digital_signatures as ds

# Getting user message.
print("Enter message to be signed.")
message = input("> ")
print("")

# Doing digital signature stuff.
Pk, pk = ds.generate_Pk_and_pk(11, 13)
digital_signature = ds.sign_string(message, pk)
signature_valid = ds.verify_signature(digital_signature, message, Pk)

# Giving user information.
print("Original message: " + message)
print("")
print("Signature: " + str(digital_signature))
print("")
print("Signature validity: " + str(signature_valid))
