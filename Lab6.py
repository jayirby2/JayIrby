# Jay Irby encoder edited by Dale Bittner
def encode(password):
    encoded_pass = ''
    for i in password:
        encoded_pass += str((int(i) + 3))
    return encoded_pass

def decode(password):
    original_pass = ''
    for i in password:
        original_pass += str((int(i) - 3))
    return original_pass
def main():
    def menu():
        print('Menu')
        print('-------------')
        print('1. Encode\n2. Decode\n3. Quit')
        print('')
        print('Please enter an option:', end=' ')

    menu()
    user_input = int(input())
    while user_input != 3:

        if user_input == 1:
            print('Please enter your password to encode:', end=' ')
            password = str(input())
            encoded_pass = encode(password)
            print('Your password has been encoded and stored!')
            print('')
            menu()
            user_input = int(input())

        elif user_input == 2:
            decode(encoded_pass)
            print(f'The encoded password is {encoded_pass}, and the original password is {decode(encoded_pass)}')
            print('')
            menu()
            user_input = int(input())


if __name__ == "__main__":
    main()



