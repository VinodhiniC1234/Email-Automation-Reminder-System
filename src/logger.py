import logging
import os

# ensure logs folder exists
os.makedirs("logs", exist_ok=True)

def setup_logger():
    logging.basicConfig(
        filename="logs/app.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    return logging