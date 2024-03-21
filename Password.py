import os

def initialize_password(password):
    with open("password.txt", "w") as file:
        file.write(password)

def check_password(password):
    with open("password.txt", "r") as file:
        stored_password = file.read().strip()
        return password == stored_password

def main():
    if not os.path.exists("password.txt"):
        password = input("Enter a password to initialize: ")
        initialize_password(password)
        print("Password initialized successfully.")
    else:
        while True:
            input_password = input("Enter the password: ")
            if check_password(input_password):
                print("Access granted!")
                break
            else:
                print("Incorrect password. Try again.")

if __name__ == "__main__":
    main()
