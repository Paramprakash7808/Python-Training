import logging
import os

LOG_FOLDER = "logs"
LOG_FILE = os.path.join(LOG_FOLDER, "application.log")

def setup_logging():
    if not os.path.exists(LOG_FOLDER):
        os.makedirs(LOG_FOLDER)

    logging.basicConfig(filename=LOG_FILE,level=logging.INFO,format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")