import random
import string

# This will be printed in the starting so the user will know that user can quit the password generater any time any time 
print("Please enter 'q' to quit.")

# Infinit loop this loop will keep running untill the user quits password generater by typing q
while 0 < 1:
    try:
        # Password is bing generated here 
        def generate_password(length=12):
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            return password

        if __name__ == "__main__":
            
            # Asking for the password length from user 
            password_length = input("Enter the desired password length: ")

            # If user types or enters q than the programme will be stop
            if password_length.lower() == 'q':
                break

            # If length entered by user is less than 8
            elif int(password_length) < 8:
                print('Sorry length must be equal to or more than 8.')

            # If length is >= 8
            else:
                generated_password = generate_password(int(password_length))
                print("Generated Password:", generated_password)

    # If the programme throws any error and does not work 
    except ValueError:
        print('Please enter a valid number for the password length.')
