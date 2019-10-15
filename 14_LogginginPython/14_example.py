import logging

# Create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename=".\\14_LogginginPython\\lumberjack.log", level=logging.WARNING, format = LOG_FORMAT, filemode="w")
logger = logging.getLogger()

# Test the logger
# logger.info("Our first message.")
# logger.info("Our second message.")

# print(logger.level)

# Test messages
logger.debug("This is a harmless debug message.")
logger.info("Just some useful info.")
logger.warning("I'am sorry, but I can't do that, Dave.")
logger.error("Did you just try to divide by zero?")
logger.critical("The entire internet is down!!")

