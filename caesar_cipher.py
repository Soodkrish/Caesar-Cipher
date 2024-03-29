
import string
def ceaser_cipher(message,value,mode):
    symbols = string.ascii_letters+string.punctuation
    changed = ''
    for letter in message:
        if letter in symbols:
            l = symbols.find(letter)
            if mode == 'e':
                ti = l + value
            elif mode == 'd':
               ti = l - value
            else:
                print("-- Usage : ( 'e' for Encryption | 'd' for Decryption ) --")
                exit()
            if ti >= len(symbols):
                ti= ti- len(symbols)
            elif ti < 0:
                ti= ti + len(symbols)

            changed = changed + symbols[ti]

        else:
            changed = changed + letter
    if mode == 'e':
        print()
        print("\033[1;32;40m!! Encryption Successful !!\033[m")
        print()
        print(f"Encrypted Message : \033[1;33;40m{changed}\033[m ")
    elif mode == 'd':
        print()
        print("\033[1;32;40m!! Decryption Successful !!\033[m")
        print()
        print(f"Decrypted Message : \033[1;33;40m {changed}\033[m")

message = input("Enter The Message:")
print()
mode = input("Enter The Mode ( 'e' for Encryption | 'd' for Decryption ) : ").lower()
print()
if mode == 'e':
    print("\033[1;36;40m|||| ENCRYPTION MODE SELECTED ||||\033[m")
    print()
    value = int(input("\033[1;31;40mEnter The Shift Value For (Encryption)\033[m: "))
elif mode == 'd':
    print("\033[1;36;40m|||| DECRYPTION MODE SELECTED ||||\033[m")
    print()
    value = int(input("\033[1:31:40mEnter The Shift Value For (Decryption)\033[m : "))
ceaser_cipher(message,value,mode)