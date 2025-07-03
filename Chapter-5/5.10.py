current_users = ['admin', 'johndoe', 'alice123', 'ech_guru', 'sarah99', 'dev_user']
new_users = ['johndoe', 'alice123','skywalker42', 'pixel_panda', 'nova_coder', 'luna_lens', 'zeno_wave']
current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f'{new_user} is already taken. You will need to enter a new username ')
    else:
        print(f' the username {new_user} is available')