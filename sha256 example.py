import hashlib

message = input("Enter the secret message: ")
hash = hashlib.sha256(str(message).encode("utf-8")).hexdigest()
print("The hash fucntion of the message *" + message + "* is " + hash)