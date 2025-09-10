import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    # Load env variables
    firstName = os.getenv('FIRST_NAME')
    lastName = os.getenv('LAST_NAME')
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    gmail = os.getenv('GOOGLE_EMAIL')
    google_password = os.getenv('GOOGLE_PASSWORD')
    linkedin_email = os.getenv('LINKEDIN_EMAIL')
    linkedin_password = os.getenv('LINKEDIN_PASSWORD')
    baseUrl = os.getenv('BASE_URL', 'https://emergimentors.com.au/')