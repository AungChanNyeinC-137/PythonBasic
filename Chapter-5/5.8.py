usernames = ['admin', 'johndoe', 'alice123', 'tech_guru', 'sarah99', 'dev_user']
for username in usernames:
    if username.lower() == 'admin':
        print(f'Hello {username},would you like to see a status report?')
    else:
        print(f'Hello {username}, thank you for logging in again.')