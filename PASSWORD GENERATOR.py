import random
import string

print("===== PASSWORD GENERATOR =====")

while True:
    try:
        length = int(input("\nEnter password length (minimum 8): "))

        if length < 8:
            print("Password should be at least 8 characters long.")
            continue

        # Characters to use
        uppercase = string.ascii_uppercase
        lowercase = string.ascii_lowercase
        numbers = string.digits
        symbols = string.punctuation

        # Ensure at least one character from each category
        password = [
            random.choice(uppercase),
            random.choice(lowercase),
            random.choice(numbers),
            random.choice(symbols)
        ]

        # Remaining characters
        all_characters = uppercase + lowercase + numbers + symbols

        for _ in range(length - 4):
            password.append(random.choice(all_characters))

        # Shuffle the password
        random.shuffle(password)

        print("\nGenerated Password:")
        print("".join(password))

    except ValueError:
        print("Please enter a valid number.")
        continue

    again = input("\nGenerate another password? (yes/no): ").lower()

    if again != "yes":
        print("\nThank you for using Password Generator!")
        break
