import inspect
import logging


class BaseClass:

    def getLogger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)

        fileHandler = logging.FileHandler('logfile')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # accepts filehandler object
        logger.setLevel(logging.DEBUG)
        return logger