from cryptography.fernet import Fernet

# Generate a random key for encryption
key = Fernet.generate_key()

# Create a Fernet instance with the key
fernet = Fernet(key)

# Define the input and output file paths
input_file = 'D:\apple\passwords.text'
output_file = 'D:\apple\example.encrypted'

# Read the contents of the input file
with open(input_file, 'rb') as f:
    data = f.read()

# Encrypt the data
encrypted_data = fernet.encrypt(data)

# Write the encrypted data to the output file
with open(output_file, 'wb') as f:
    f.write(encrypted_data)

# Save the key to a file
with open('key.key', 'wb') as f:
    f.write(key)
