import logging


# setup logging formats and a log file name
def start_logging():
    logging.basicConfig(filename="logfile.log", format="[%(asctime)s] %(message)s",
                        filemode="w", level=logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler())


# wrapper function for the main() (main.py) functions to log script execution messages.
def log_actions(fun):
    def wrapper(*args, **kwargs):
        start_logging()
        fun(*args, **kwargs)
        logging.shutdown()
    return wrapper
