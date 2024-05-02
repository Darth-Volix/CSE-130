import json

def create_lists():
    '''
    Reads data from a JSON file and extracts usernames and passwords.

    Returns:
        tuple: A tuple containing two lists: usernames and passwords.
    '''
    with open('Lab02.json', 'r') as json_file:
        data = json.load(json_file)

        usernames = data['username']
        passwords = data['password']

    return usernames, passwords

def get_user_input():
    '''
    Prompts the user to input their username and password.

    Returns:
        tuple: A tuple containing the provided username and password as strings.
    '''
    provided_username = input('Please enter your username: ')
    provided_password = input('Please enter your password: ')

    return provided_username, provided_password

def check_credentials(usernames, passwords, provided_username, provided_password):
    '''
    Checks if the provided username and password match the stored credentials.

    Parameters:
        usernames (list): List of valid usernames.
        passwords (list): List of corresponding passwords.
        provided_username (str): User-provided username.
        provided_password (str): User-provided password.

    Returns:
        None: Prints authentication status.
    '''
    try:
        index = usernames.index(provided_username)
        if provided_password == passwords[index]:
            print('You are authenticated!')
        else:
            print('You are not authenticated.')
    except ValueError:
        print('You are not authenticated.')

def main():
    '''
    Entry point of the program.
    '''
    usernames, passwords = create_lists()
    provided_username, provided_password = get_user_input()
    check_credentials(usernames, passwords, provided_username, provided_password)

if __name__ == "__main__":
    main()           