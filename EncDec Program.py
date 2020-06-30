import random
from IPython.display import clear_output as cls

choice = ''
message = ''
string = ''
cls_choice = ''
upper_alphabets = [chr(x) for x in range(65,90)]
special_characters = ['!', '@', '#', '$', '%', '^']
enc_hist = {}
dec_hist = {}

plain_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']
encryption_list = ['A@', 'A#', 'A$', 'A%', 'B@', 'B#', 'B$', 'B%', 'C@', 'C#', 'C$', 'C%', 'D@', 'D#', 'D$', 'D%', 'E@', 'E#', 'E$', 'E%', 'F!', 'F@', 'F#', 'F$', 'F%', 'F^', 'A!', 'A^', 'B!', 'B^', 'C!', 'C^', 'D!', 'D^', 'E!', 'E^', '~']

print('Welcome to En-Decryption Algorithm.\n')

while str(choice) != '0':
    stringlist = []
    result = ''

    choice = input("\n Do you want to Encrypt or Decrypt the message?\n Enter 1 to Encrypt, 2 to Decrypt or 0 to Exit program: ")

    if str(choice) == '1':
        message = input('\nEnter message for encryption: ').upper()
    
        for i in range(0, len(message)):
            result += encryption_list[plain_characters.index(message[i])]

        print(f'\nEncoded Message: {result} \n\n')
        
        enc_hist[message] = result
        
            
    elif str(choice) == '2':
        message = input('\nEnter message to decrypt: ').upper()     
        
        for char in message:
            if char in upper_alphabets:
                string += char
            elif char in special_characters:
                string += char
                stringlist.append(string)
                string = ''
            elif char == '~':
                stringlist.append(char)
            else:
                print(f"Character ('{char}') Out of Range. Try Again.")

        for i in range(0, len(stringlist)):
            result += plain_characters[encryption_list.index(stringlist[i])]

        print(f'\nDecoded Message: {result} \n\n')
        
        dec_hist[message] = result
        
    elif str(choice) != '0':
        print('You have entered an invalid input, please try again. \n\n')
        
    else:
        cls()
        
        print("\nYour Encryption Histroy:\n")
        num = 1
        for key in enc_hist:
            print(f"{num}. You encrypted: '{key}' into '{enc_hist[key]}'.")
            num += 1
       
        print("\n\nYour Decryption Histroy:\n")
        num = 1
        for key in dec_hist:
            print(f"{num}. You decrypted: '{key}' into '{dec_hist[key]}'.")
            num += 1
    
        print("\n\nThanks for using the Algorithm.")