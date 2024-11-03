import logging
import os

def setup_logger(name, log_file, level=logging.INFO):
    """
    Sets up a logger with the specified name and log file.
    
    Args:
        name: The name of the logger.
        log_file: The file where logs will be written.
        level: The logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL).
    """
    # Create a logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create a file handler for writing logs
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)

    # Create a formatter and set it for the file handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    return logger

# Setup loggers for different parts of the application
app_logger = setup_logger('app', 'logs/app.log')
helmet_detection_logger = setup_logger('helmet_detection', 'logs/helmet_detection.log')
speed_detection_logger = setup_logger('speed_detection', 'logs/speed_detection.log')
