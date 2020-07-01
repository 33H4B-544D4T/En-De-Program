#------------------- 21 Days Coding Challenge (Project 02: Encryption-Decryption Algorithm)--------------------------------- 
from IPython.display import clear_output as cls

choice = ''
string = ''
message = ''
cls_choice = ''
upper_alphabets = [chr(x) for x in range(65,71)] #----- List of A-F Uppercase Alphabets
special_characters = ['!', '@', '#', '$', '%', '^'] #----- List of Characters included for Encryption
enc_hist = {} 
dec_hist = {}

#--------- Plain Alphanumeric List including 'Space'
plain_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']

#--------- Refrence Encryption List
encryption_list = ['A@', 'A#', 'A$', 'A%', 'B@', 'B#', 'B$', 'B%', 'C@', 'C#', 'C$', 'C%', 'D@', 'D#', 'D$', 'D%', 'E@', 'E#', 'E$', 'E%', 'F!', 'F@', 'F#', 'F$', 'F%', 'F^', 'A!', 'A^', 'B!', 'B^', 'C!', 'C^', 'D!', 'D^', 'E!', 'E^', '~']

print('Welcome to En-Decryption Algorithm.\n')

while str(choice) != '0':
    stringlist = []
    result = ''

    choice = input("\n Do you want to Encrypt or Decrypt the message?\n Enter 1 to Encrypt, 2 to Decrypt or 0 to Exit program: ")

    #---------Encryption Routine
    if str(choice) == '1':
        try:
            message = input('\nEnter message for encryption: ').upper()
    
            for i in range(0, len(message)):
                result += encryption_list[plain_characters.index(message[i])] #-----Encryption via Indexing

            print(f'\nEncoded Message: {result} \n\n')
        
            enc_hist[message] = result
        
        except Exception as e: 
            print(f"Error: {e}. Try Again.") #---- Displays Error in Formatted Form
            
    #---------Decryption Routine
    elif str(choice) == '2':
        message = input('\nEnter message to decrypt: ').upper()     
        
        try:
            #-----Message Slicing and Appension 
            for char in message:
                if char in upper_alphabets:
                    string = ''
                    string += char
                elif char in special_characters:
                    string += char
                    stringlist.append(string)
                    string = ''
                elif char == '~':
                    stringlist.append(char)
            #---------------------------------
            
            for i in range(0, len(stringlist)):
                result += plain_characters[encryption_list.index(stringlist[i])] #-----Decryption via Indexing

            print(f'\nDecoded Message: {result} \n\n')
        
            dec_hist[message] = result
        
        except Exception as e: 
            print(f"Error: {e}. Try Again.") #---- Displays Error in Formatted Form
        
    elif str(choice) != '0':
        print('You have entered an invalid input, Please try again. \n\n')
        
    #---------History and Conclusion
    else:
        cls()
        
        print("\nYour Encryption Histroy:\n")
        num = 1
        for key in enc_hist:
            print(f"{num}. You encrypted: '{key}' into '{enc_hist[key]}'.") #---- Encryption History
            num += 1
       
        print("\n\nYour Decryption Histroy:\n")
        num = 1
        for key in dec_hist:
            print(f"{num}. You decrypted: '{key}' into '{dec_hist[key]}'.") #---- Decryption History
            num += 1
    
        print("\n\nThanks for using the Algorithm.")