import re

default_email = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
default_phone = re.compile(r'^\([1-9]{2}\) 9?[6-9][0-9]{3}-[0-9]{4}$')

class Contact:
    def __init__(self, name, email, phone, favorite = False):
        self._name = name
        self._email = email
        self._phone = phone
        self._favorite = favorite
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError('Name must be a string')
        self._name = value
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if not default_email.match(value):
            raise ValueError('Email must be a valid e-mail')
        self._email = value

    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, value):
        if not default_phone.match(value):
            raise ValueError('Phone must be a valid number')
        self._phone = value
    
    @property
    def favorite(self):
        return self._favorite
    
    @favorite.setter
    def favorite(self, value):
        if not isinstance(value, bool):
            raise ValueError('Favorite must be a valid boolean')
        self._favorite = value
    
    def __str__(self):
        return f"('name', '{self.name}'), ('email', '{self.email}'), ('phone', '{self.phone}'), ('favorite', {self.favorite})"
