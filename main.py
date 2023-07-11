import sys
print(sys.executable)

from app.api.models.user import User
# Create a User object
user = User(1, "John Doe", "johndoe@example.com", "password123")

# Authenticate user
email = input("Enter your email: ")
password = input("Enter your password: ")

if user.authenticate(email, password):
    print("Authentication successful!")
else:
    print("Authentication failed.")