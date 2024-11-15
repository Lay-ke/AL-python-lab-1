import os

def get_user_input():
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email: ")
    return name, phone, email

def update_profile_file(filepath):
    name, phone, email = get_user_input()
    with open(filepath, 'w') as file:
        file.write(f"Name: {name}\n")
        file.write(f"Phone: {phone}\n")
        file.write(f"Email: {email}\n")
    print("Profile updated successfully.")

def check_profile_file(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            content = file.read()
            print("Current Profile Information:\n")
            print(content)
            confirm = input("Is the above information up to date? (yes/no): ").strip().lower()
            if confirm != 'yes':
                update_profile_file(filepath)
    else:
        print("Profile file does not exist. Creating a new one.")
        update_profile_file(filepath)

def main():
    username = os.getlogin()
    print(username)
    home_dir = os.path.expanduser(f"~/{username}")
    print(home_dir)
    profile_file = os.path.join(home_dir, 'profile.txt')

    if os.path.basename(os.getcwd()) == username:
        print(f"You are in your home directory: {os.getcwd()}")
        check_profile_file(profile_file)
    else:
        print(f"Creating home directory for user: {username}")
        os.makedirs(home_dir, exist_ok=True)
        check_profile_file(profile_file)

    print("You can now continue using the terminal.")

if __name__ == "__main__":
    main()

