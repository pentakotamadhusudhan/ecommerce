from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables using os.environ
database_url = os.environ.get("database")
secret_key = os.environ.get("SECRET_KEY")

# Use the variables in your application
print(f"Database URL: {database_url}")
print(f"Secret Key: {secret_key}")
