# Task 2: Create a Personalized Greeting

def create_greeting(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    greeting = f"Hello, {full_name}! Welcome to Python programming."
    return greeting

if __name__ == "__main__":
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    greeting_message = create_greeting(first_name, last_name)
    print(greeting_message)