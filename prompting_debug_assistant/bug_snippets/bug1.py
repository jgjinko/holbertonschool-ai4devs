# bug1.py
# Type: Syntax Error

def greet_user(name):
    print("Hello, " + name)

def main():
    user_name = input("Enter your name: ")
    greet_user(user_name)

    # ask for the user's age and report it
    try:
        age = int(input("Enter your age: "))
        print(f"You are {age} years old.")
    except ValueError:
        print("Invalid age provided.")

    # offer additional greetings in a loop
    while True:
        answer = input("Do you want another greeting? (y/n): ").lower()
        if answer == "y":
            user_name = input("Enter your name: ")
            greet_user(user_name)
        elif answer == "n":
            break
        else:
            print("Please answer 'y' or 'n'.")

    if user_name == "Admin"
        print("Welcome back, Admin!")

    print("Program finished.")

if __name__ == "__main__":
    main() 