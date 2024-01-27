class User:
    def __init__(self, f_name, l_name, desig, age):
        self.f_name = f_name
        self.l_name = l_name
        self.desig = desig
        self.age = age
        self.login_attempt = 0

    def describe_user(self):
        print("**** DESCRIBE USER ****")
        print("-" * 23)
        print(f"fullname: {self.f_name}{self.l_name}")
        print(f"desig: {self.desig}")
        print(f"age: {self.age}")

    def greet_user(self):
        print(f"you are welcome, {self.f_name} {self.l_name}.")

    def increment_login_attempt(self):
        self.login_attempt += 1

    def reset_login_attempt(self):
        self.login_attempt = 0


user1 = User("Michael", "Ukeje", "Software Engineer", 31)
user2 = User("Daniela", "Petrova", "Hacker ethical", 29)
user1.describe_user()
user1.greet_user()

print()
user2.increment_login_attempt()
user2.increment_login_attempt()
user2.increment_login_attempt()
user2.increment_login_attempt()
print(f"attempts: {user2.login_attempt}")
user2.reset_login_attempt()

print(f"attempts after reset: {user2.login_attempt}")