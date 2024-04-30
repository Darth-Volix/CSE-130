# 1. Name: 
#    Nicholas Wilkins
# 2. Assignment Name: 
#    Lab 02: Authentication Program
# 3. Assignment Description:
#    For this assignment I was supposed to write the contents 
#    (usernames and passwords) of a separate file into two different 
#    lists within this program. From there I prompt the user for a 
#    username and password and check to see if what they have 
#    provided is valid credentials, ultimately telling the user
#    the result.
# 4. What was the hardest part? Be as specific as possible.
#    The hardest part of the program was actually a tie between two
#    different parts of the code. Remmebering how to open and read 
#    the contents of one file into lists in another took some research
#    and looking at past projects, which took some time. The other hard
#    part of the program was properly iterating through the lists to 
#    determine if the inputs matched or were valid. I had a bug where 
#    it would print the result multiple times because of an error in
#    my syntax/logic. I would say that figuring out how
#    to compare inputs to the contents of the lists was the hardest part
#    to solve. Redaing the file into lists was a problem with my memory,
#    the input camparisons and validation was a logic problem that took
#    some real thinking on my part. 
# 5. How long did it take for you to complete the assignment?
#    It took me about 3.5 hours to complete this assignment when you
#    include filming the video and uploading it to youtube. 

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
    provided_username = input('Username: ')
    provided_password = input('Password: ')

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
    if provided_username in usernames:
        for i in range(len(usernames)):
            if provided_username == usernames[i]:
                index = i
                if provided_password == passwords[index]:
                    print('You are authenticated!')
                else:
                    print('You are not authorized to use the system.')
    else:
        print('You are not authorized to use the system.')

def main():
    '''
    Entry point of the program.
    '''
    usernames, passwords = create_lists()
    provided_username, provided_password = get_user_input()
    check_credentials(usernames, passwords, provided_username, provided_password)


if __name__ == "__main__":
    main()            