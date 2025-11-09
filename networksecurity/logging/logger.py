import logging
import os
from datetime import datetime

def setup_logger():
    # Logs directory with date-based subfolders
    current_date = datetime.now().strftime('%Y-%m-%d')
    logs_dir = os.path.join(os.getcwd(), "logs", current_date)
    os.makedirs(logs_dir, exist_ok=True)
    
    # Create log filename with timestamp
    LOG_FILE = f"{datetime.now().strftime('%H_%M_%S')}.log"
    LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)
    
    # Configure logging
    logging.basicConfig(
        filename=LOG_FILE_PATH,
        format='%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.INFO
    )
    
    # Console handler for immediate feedback
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logging.getLogger().addHandler(console_handler)
    
    return LOG_FILE_PATH

# Usage
if __name__ == "__main__":
    log_path = setup_logger()
    logging.info("Logger setup completed")
    logging.info(f"Logging to: {log_path}")