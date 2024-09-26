import os
import logging

def initLogger():
    if (os.path.isdir("logs") is False): os.mkdir("logs")

    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s][%(levelname)s][%(threadName)s][%(module)s][%(funcName)s][line %(lineno)d] %(message)s',
        handlers=[
            logging.FileHandler("logs/logs.log", mode='w+'),
            logging.StreamHandler()
        ]
    )

    logger = logging.getLogger()
    logger.info("Logger created!")
#end-def