from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('API_KEY')

DOWNLOAD_DIR = 'downloads'
VIDEOS_DIR = os.path.join(DOWNLOAD_DIR, 'videos')
CAPTIONS_DIR = os.path.join(DOWNLOAD_DIR, 'captions')
OUTPUTS_DIR = 'outputs'

