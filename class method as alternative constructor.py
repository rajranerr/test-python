#  the @classmethod decorator to implement alternative constructors. Because Python does not support traditional method overloading (defining multiple __init__ methods with different signatures), class methods allow you to instantiate objects from different data formats like strings, dictionaries, or files. 

# Core Implementation Template: A class method receives the class itself as its first argument (conventionally named cls) instead of an instance (self). It processes the input data and returns an initialized object by calling cls(...).

# Ex:
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data_string):
        """Creates a User instance from a comma-separated string."""
        name, age_str = data_string.split(",")
        # cls(...) dynamically calls the __init__ method of this class
        return cls(name.strip(), int(age_str.strip()))

    @classmethod
    def from_dict(cls, data_dict):
        """Creates a User instance from a dictionary."""
        return cls(data_dict["name"], data_dict["age"])

# 1. Using the standard constructor
user1 = User("Kritika", 18)

# 2. Using the alternative string constructor
user2 = User.from_string("Raj, 21")

# 3. Using the alternative dictionary constructor
user3 = User.from_dict({"name": "Shivakshi", "age": 20})

print(user1.name, user1.age)
print(user2.name, user2.age)
print(user3.name, user3.age)

# Ex:
class AdminUser(User):
    pass

# This returns an instance of AdminUser, not User, because of `cls`
admin = AdminUser.from_string("Mukesh, 19")
print(type(admin))
print(admin.name, admin.age)