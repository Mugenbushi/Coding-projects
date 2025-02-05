import hashlib
import getpass

password_manager = {}

def create_account():
    username = input("Enter Your Username")
    password = getpass.getpass("Enter your desired password")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_password
    print("Account create succesfully")


def login():
    username = input("Enter your user name")
    password = getpass.getpass("Enter your password here")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print("login successful")
    else:
        print("invalid username or password")


def main():
    while True:
        choice = input("Enter 1 to create an account, 2 to login, or 0 to exit")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "0":
            break
        else:
            print("INvalid choice")

if __name__ == "__main__":
    main()