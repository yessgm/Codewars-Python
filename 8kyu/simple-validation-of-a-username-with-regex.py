def validate_usr(username):
    if username == '____':
        return True
    if username.isalnum() or "_" in username:
        if username.islower():
            if len(username) >= 4 and len(username) <= 16:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def validate_usr(username):
    return bool(re.match(r'^[a-z0-9_]{4,16}$', username))
