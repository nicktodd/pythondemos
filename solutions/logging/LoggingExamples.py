import logging
import logging.config



#logger.setLevel(logging.CRITICAL) # try changing the level to see what appears
logging.config.fileConfig("logging.conf")
logger = logging.getLogger('myOtherLogger')
logger.warning('This is a warning message')
logger.info('This is an info message')
logger.critical('This is a CRITICAL message')
