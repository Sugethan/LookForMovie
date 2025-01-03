class logins():
    
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

class user():
    
    def __init__(self, id: str, name: str, logins: logins):
        self.id = id
        self.name = name
        self.logins = logins
