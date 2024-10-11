def Secret_Code(message):
    secret_code = ""
    for char in message:
        if char.isalpha():  # Check if the character is a letter
            if char == 'z':
                secret_code += 'a'
            elif char == 'Z':
                secret_code += 'A'
            else:
                secret_code += chr(ord(char) + 1)
        else:
            secret_code += char  # Keep spaces and punctuation as they are
    return secret_code

def main():
    print("Write the message to secret code ")
    message = input("Enter a message: ")
    encoded_message = Secret_Code(message)
    print(encoded_message)

if __name__ == "__main__":
    main()