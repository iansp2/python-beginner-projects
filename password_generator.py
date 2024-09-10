import string
import secrets


class Password:
    def __init__(self, length: int = 16, upper: bool = True, symbols: bool = True) -> None:
        if length < 6:
            raise ValueError("Password must have at least 6 characters.")
        
        self.length = length
        self.upper = upper
        self.symbols = symbols
        

    def generate_password(self) -> str:
        char_options = string.ascii_lowercase + string.digits

        if self.upper:
            char_options += string.ascii_uppercase

        if self.symbols:
            char_options += string.punctuation
        
        password = []

        # Ensure password has at least one uppercase letter and one symbol if requested
        if self.upper:
            password.append(secrets.choice(string.ascii_uppercase))

        if self.symbols:
            password.append(secrets.choice(string.punctuation))

        # Fill the rest of the password length
        password += [secrets.choice(char_options) for _ in range(self.length - len(password))]
        
        # Shuffle the list to ensure randomness
        secrets.SystemRandom().shuffle(password)

        return ''.join(password)


def check_strength(password: str) -> None:
    if len(password) < 16:
        print("Password is too short, consider using a password with at least 16 characters.")
        return
    
    if not any(char in string.punctuation for char in password):
        print("Password doesn't contain symbols.")
        return

    if not any(char in string.ascii_uppercase for char in password):
        print("Password doesn't contain upper case letters.")
        return

    print("Your password is strong af.")


def main() -> None:
    password_obj = Password()
    generated_password = password_obj.generate_password()
    print(f"Generated Password: {generated_password}")
    check_strength(generated_password)

if __name__ == "__main__":
    main()