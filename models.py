from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @staticmethod
    def get(user_id):
        # Replace this with your database query to fetch a user by ID
        users = {'test': {'id': 'test', 'username': 'test', 'password': 'test'}}
        user_data = users.get(user_id)
        if user_data:
            return User(user_data['id'], user_data['username'], user_data['password'])
        return None
