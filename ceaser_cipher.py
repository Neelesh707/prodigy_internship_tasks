
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryption(key,text):
    cipher_text=""
    for char in text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position+key)%26
            cipher_text+=alphabet[new_position]
        else:
            cipher_text+=char
    print(f"Here is the text after encryption\n{cipher_text}")


def decryption(key,text):
    normal_text=""
    for char in text:
        if char in alphabet:
            position=alphabet.index(char)
            old_position=(position-key)%26
            normal_text+=alphabet[old_position]
        else:
            normal_text+=char
    print(f"Here is the text after decryption\n{normal_text}")


flag=False 
while not flag:
    ch=input("Type 'encrypt' for encryption and 'decrypt' for decryption\n").lower()
    key=int(input("Enter Key value : "))
    text=input("Enter a string : ").lower()

    if ch=="encrypt":
        encryption(key,text)
    elif ch=="decrypt":
        decryption(key,text)
    else:
        print("Invalid choice!\n")
    ag=input("Type 'yes' to continue ,Type 'no' to exit\n").lower()
    if ag=='no':
        flag=True
        print("Program Termination successfull\n")
        



