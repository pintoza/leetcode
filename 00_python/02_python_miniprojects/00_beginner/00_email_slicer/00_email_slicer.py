def get_user_input():
    return input("Enter your email address: ").strip()

def make_username(email):
    return email[:email.index("@")]

def make_domain(email):
    return email[email.index("@") + 1:]

def main():
    email = get_user_input()
    username = make_username(email)
    domain = make_domain(email)
    print(f"Your username is {username} and your domain is {domain}")

if __name__ == "__main__":
    main()

