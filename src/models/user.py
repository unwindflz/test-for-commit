class User:
    """
    A class representing a user in the application.
    """
    def __init__(self, username, email):
        """
        Initializes a User instance.
        
        :param username: The username of the user.
        :param email: The email address of the user.
        """
        self.username = username
        self.email = email

    def __str__(self):
        """
        Returns a string representation of the User.
        """
        return f'User(username={self.username}, email={self.email})'

    def update_email(self, new_email):
        """
        Updates the email of the user.
        
        :param new_email: The new email address.
        :raises ValueError: If the new email is invalid.
        """
        if '@' not in new_email:
            raise ValueError('Invalid email address')
        self.email = new_email

    def to_dict(self):
        """
        Converts the User instance to a dictionary.
        
        :return: A dictionary representation of the user.
        """
        return {'username': self.username, 'email': self.email}
