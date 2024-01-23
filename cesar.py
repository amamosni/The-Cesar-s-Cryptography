# Define the alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Function to encrypt a message
def encrypt(message, key):
  """
  Encrypts a message using the Caesar cipher.

  Args:
    message: The message to encrypt.
    key: The key for the cipher.

  Returns:
    The encrypted message.
  """

  encrypted_message = ""
  for letter in message:
    #Check in letter in alphabet
    if letter in alphabet:
      # Get the position of the letter in the alphabet
      letter_position = alphabet.find(letter)
      # Apply the key (sum the key)
      new_position = letter_position + key
      # Get the new letter
      new_letter = alphabet[new_position % len(alphabet)]
      # Add the new letter to the encrypted message
      encrypted_message += new_letter
    else:
      encrypted_message += letter
  return encrypted_message

# Function to decrypt a message
def decrypt(message, key):
  """
  Decrypts a message using the Caesar cipher.

  Args:
    message: The message to decrypt.
    key: The key for the cipher.

  Returns:
    The decrypted message.
  """

  decrypted_message = ""
  for letter in message:
    #Check in letter in alphabet
    if letter in alphabet:
      # Get the position of the letter in the alphabet
      letter_position = alphabet.find(letter)
      # Apply the inverse key
      new_position = letter_position - key
      # Get the new letter
      new_letter = alphabet[new_position % len(alphabet)]
      # Add the new letter to the decrypted message
      decrypted_message += new_letter
    else:
      decrypted_message += letter
  return decrypted_message

# Program options
options = {
  "1": encrypt,
  "2": decrypt
}

# Get the user's desired option
option = input("What do you want to do?\n1. encrypt\n2. decrypt\nEnter option: ")

# If the option is valid
if option in options:
  # Get the message from the user
  message = input("Enter the message: ").lower()

  # Get the key from the user
  key = int(input("Enter the key: "))

  # Apply the desired option
  message_result = options[option](message, key)

  # Print the result
  print("Result:", message_result)

# If the option is not valid
else:
  print("Invalid option.")