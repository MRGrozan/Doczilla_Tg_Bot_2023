from loguru import logger

def create_log_files():
    logger.add("logs/main_{time}.log",rotation="12:00", compression="zip", retention="10 days")

def add_log_server_files():
    logger.add("logs/server_{time}.log",rotation="12:00", compression="zip", retention="10 days")