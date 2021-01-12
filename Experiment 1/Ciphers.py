import math
import random
import string
import numpy as np

def transposition_cipher(message, keyword, flag):
    '''Set flag = True for encryption and False for decryption '''
    if flag == True:
        matrix = []
        temp = []
        j = 0

        for letter in message:
            if j < len(keyword):
                if (ord(letter) >= 65 and ord(letter) <= 90 ) or (ord(letter) >= 97 and ord(letter) <= 122):
                    temp.append(letter)
                    j += 1
            else:
                matrix.append(temp)
                temp = [letter]
                j = 1
        else:
            for i in range(len(keyword) - len(temp)):
                temp += random.choice(string.ascii_letters)
            matrix.append(temp)

        matrix.insert(0, list(keyword))

        matrix = list(zip(*sorted(zip(*matrix))))
        matrix = matrix[1:]

        encrypted_message = ""
        count = 0

        for i in range(len(keyword)):
            for j in range(len(matrix)):
                if count < 5:
                    encrypted_message += matrix[j][i]
                    count += 1
                else:
                    encrypted_message += " " + matrix[j][i]
                    count = 1

        return encrypted_message
    else:
        encrypted_message = "".join(message.split()) # Removing spaces from the message
        encrypted_message_list = list(encrypted_message)

        matrix = []
        temp = []
        j = 0
        column_length = len(encrypted_message) // len(keyword)

        for letter in encrypted_message_list:
            if j < column_length:
                temp.append(letter)
                j += 1
            else:
                # print(temp)
                matrix.append(temp)
                temp = [letter]
                j = 1
        else:
            matrix.append(temp)

        numpy_matrix = np.array(matrix)
        numpy_matrix = np.transpose(numpy_matrix)

        sorted_key = list(keyword)
        sorted_key.sort()

        numpy_matrix = np.vstack((sorted_key, numpy_matrix))
        numpy_matrix = list(zip(*sorted(zip(*numpy_matrix), key = lambda i: list(key).index(i[0]))))
        numpy_matrix = numpy_matrix[1:]

        decrypted_message = []
        for sublist in numpy_matrix:
            decrypted_message += sublist

        decrypted_message = ''.join(decrypted_message)

        return decrypted_message

def caeser_cipher(message, shift, flag):
    '''Set flag = True for encryption and False for decryption '''
    output = ""

    if flag == True: 
        for letter in message:
            if ord(letter) >= 65 and ord(letter) <= 90:
                encrypted_letter = chr(((ord(letter) - 65 + shift) % 26) + 65) 
                output += encrypted_letter
            elif ord(letter) >= 97 and ord(letter) <= 122:
                encrypted_letter = chr(((ord(letter) - 97 + shift) % 26) + 97) 
                output += encrypted_letter
    else:
        for letter in message:
            if ord(letter) >= 65 and ord(letter) <= 90:
                decrypted_letter = chr(((ord(letter) - 65 - shift) % 26) + 65) 
                output += decrypted_letter
            elif ord(letter) >= 97 and ord(letter) <= 122:
                decrypted_letter = chr(((ord(letter) - 97 - shift) % 26) + 97) 
                output += decrypted_letter

    return output

def vernam_cipher(message, keyword):
    output = ""

    for letter1, letter2 in zip(message, keyword):
        xored_character = chr(ord(letter1) ^ ord(letter2)) 
        output += xored_character
            
    return output

if __name__ == "__main__":
    while True:
        print("Select an encryption algorithm: ")
        print("a. Substitution Cipher")
        print("b. ROT 13")
        print("c. Columnar Transposition Cipher")
        print("d. Double Columnar Transposition Cipher")
        print("e. Vernam Cipher")
        print("f. Diffie Hellman Key Exchange")
        print("g. Exit")
        
        choice = input()
        if choice == "a" or choice == "A":
            plain_text = input("\nEnter the plain text: ")
            shift = int(input("Enter the shift: "))
            encrypted_message = caeser_cipher(plain_text, shift, True)
            decrypted_message = caeser_cipher(encrypted_message, shift, False)

            print("Encrypted Message: " + encrypted_message)
            print("Decrypted Message: " + decrypted_message + "\n")
        
        elif choice == "b" or choice == "B":
            plain_text = input("\nEnter the plain text: ")
            shift = 13
            encrypted_message = caeser_cipher(plain_text, shift, True)
            decrypted_message = caeser_cipher(encrypted_message, shift, False)

            print("Encrypted Message: " + encrypted_message)
            print("Decrypted Message: " + decrypted_message + "\n")

        elif choice == "c" or choice == "C":
            plain_text = list(input("\nEnter the plain text: "))
            key = input("Enter a keyword: ")

            encrypted_message = transposition_cipher(plain_text, key, True)
            decrypted_message = transposition_cipher(encrypted_message, key, False)

            print("Encrypted message: " + encrypted_message)
            print("Decrypted message: " + decrypted_message + "\n")
        
        elif choice == "d" or choice == "D":
            plain_text = list(input("\nEnter the plain text: "))
            key = input("Enter a keyword: ")

            encrypted_message = transposition_cipher(plain_text, key, True)
            encrypted_message = transposition_cipher(encrypted_message, key, True)
            decrypted_message = transposition_cipher(encrypted_message, key, False)
            decrypted_message = transposition_cipher(decrypted_message, key, False)

            print("Encrypted message: " + encrypted_message)
            print("Decrypted message: " + decrypted_message + "\n")

        elif choice == "e" or choice == "e":
            plain_text = input("\nEnter the plain text: ")
            key = input("Enter a keyword of same length: ")
            
            while len(plain_text) != len(key):
                print("Plain text and Keyword are not of same length. Please give the input again.")
                plain_text = input("\nEnter the plain text: ")
                key = input("Enter a keyword of same length: ")

            encrypted_message = vernam_cipher(plain_text, key)
            decrypted_message = vernam_cipher(encrypted_message, key)

            print("Encrypted Message: " + encrypted_message)
            print("Decrypted Message: " + decrypted_message + "\n")

        elif choice == "f" or choice == "F" or choice == "g" or choice == "G":
            break
        else:
            print("\nEnter valid choice.\n")




