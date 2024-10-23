# Lucca Carvalho Magalhaes
def encoder(passwd):
    encoded = ""
    for i in passwd:
        encoded += str((int(i) + 3) % 10)
    return encoded

def decoder(encoded_pass):
    decoded_pass = ""
    for i in encoded_pass:
        if int(i) < 3:
            decoded_pass += str((int(i) + 10) - 3)
        else:
            decoded_pass += str((int(i) - 3))
    return decoded_pass

if __name__ == "__main__":
    while True:
       
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()

        opt = int(input("Please enter an option: "))
        passwd = "1"
        if opt == 1:
            password = input("Please enter your password to encode: ")
            password = str(encoder(password))
        elif opt == 2:
            print(f"The encoded password is {password}, and the original password is {decoder(password)}.")
        elif opt == 3:
            break
