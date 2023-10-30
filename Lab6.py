# Jay Irby encoder
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
            encoded_pass = ''
            for i in password:
                encoded_pass += str((int(i) + 3))
            print('Your password has been encoded and stored!')
            print('')
            menu()
            user_input = int(input())

        elif user_input == 2:
            original_pass = ''
            for i in encoded_pass:
                original_pass += str((int(i)-3))
            print(f'The encoded password is {encoded_pass}, and the original password is {original_pass}')
            print('')
            menu()
            user_input = int(input())


if __name__ == "__main__":
    main()



