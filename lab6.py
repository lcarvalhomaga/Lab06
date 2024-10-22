# Lucca Carvalho Magalhaes
def encoder(passwd):
    encoded = ""
    for i in passwd:
        encoded += str((int(i) + 3) % 10) 
    return encoded

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
            passwd = input("Please enter your password to encode: ")
            passwd = encoder(passwd)
        elif opt == 2:
            print(f"The encoded password is {passwd}, and the original password is {decoder(passwd)}.")
        elif opt == 3:
            break
