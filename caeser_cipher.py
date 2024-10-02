def encrpt(txt,shft):
    result=""

    for i in range (len(txt)):
        char=txt[i]
        if char.isupper():
            result+=chr(ord(char)+shft-65)
        elif char.islower():
            result+=chr(ord(char)+shft+65)
        else:
            result+=char
    return result
def decrpt(cipher,shft):
    result=""
    for i in range(len(cipher)):
        char=cipher[i]
        if char.isupper():
            result+=chr(ord(char)+shft-65)
        elif char.islower():
            result+=chr(ord(char)+shft+65)
        else:
            result+=char
    return result 
txt=input('Enter text to be encrypted \n')
shft=int(input("Enter shift value\n"))

encrypted_txt=encrpt(txt,shft)
print(f'Encrypted text:{encrypted_txt}')

encrypted_input = input("Enter the encrypted text to decrypt: ")
shift_for_decryption = int(input("Enter the shift value used for encryption: "))

decrypted_text = decrpt(encrypted_input, shift_for_decryption)
print(f"Decrypted: {decrypted_text}")
