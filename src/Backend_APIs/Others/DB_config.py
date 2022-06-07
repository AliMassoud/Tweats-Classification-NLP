from dotenv import load_dotenv, find_dotenv
import os

DB_conf = {
    'DB_URL': os.getenv('DB_URL'),
    'DB_NAME': os.getenv('DB_NAME'),
    'DB_USERNAME':os.getenv('DB_USERNAME'),
    'DB_PASSWORD': os.getenv('DB_PASSWORD')
}