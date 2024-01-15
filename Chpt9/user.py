class User:
    def __init__(self, f_name, l_name, desig, age):
        self.f_name = f_name
        self.l_name = l_name
        self.desig = desig
        self.age = age

    def describe_user(self):
        print("**** DESCRIBE USER ****")
        print("-" * 23)
        print(f"fullname: {self.f_name}{self.l_name}")
        print(f"desig: {self.desig}")
        print(f"age: {self.age}")

    def greet_user(self):
        print(f"you are welcome, {self.f_name} {self.l_name}.")


user1 = User("Michael", "Ukeje", "Software Engineer", 31)
user1.describe_user()
user1.greet_user()