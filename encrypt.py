""" 
0 This script is under development approach with caution.
And the catch is it only encrypts and does not decrypt, 
the second part is coming soon keep checking.  

1 When run this script will encrypt all the files in the 
current directory with the exception of the files mentioned.
in the variable ***ignore_files*** and child directories.

2 To install the requirements run this command on your CMD: pip install cryptography

"""

# Importation of the required libraries
import os
from cryptography.fernet import Fernet


# Create a list to store the files targeted for encryption 
target_files = list()


# List of files in the current directory to exempt from encryption
ignore_files =["encrypt.py", "secure.key", "decrypt.py"]


# Generate a string to use as a key when encrypting 
secure_key = Fernet.generate_key()


# Go through all the files in the current directory 
# and add them to the files list but ignore the ones 
# mentioned in the ignore_files list and child directories

for file in os.listdir():
	if file in ignore_files:
		continue
	if os.path.isfile(file):
		target_files.append(file)


# Create a file named secure.key in the current directory
# and copy to it the contents of secure_key

with open("secure.key", "wb") as key:
	key.write(secure_key)


# Go through all the files in the current directory
# and encrypt their contents except the ones mentioned
# in the ignore_files list and child directories

for file in target_files:
	with open(file, "rb") as f:
		file_contents = f.read()
	encrypted_contents = Fernet(secure_key).encrypt(file_contents)
	with open(file, "wb") as f:
		f.write(encrypted_contents)




