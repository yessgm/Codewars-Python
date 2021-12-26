def validate(username, password):
    database = Database()
    return database.login(username, password)
