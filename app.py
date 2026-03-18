import logging

from sleeper_wrapper import Stats


# Application sets log level to ERROR in its logger
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

# Info log is not visible
logger.info("Starting application")
# Warning log is not visible
logger.warning("Applicaton log: warning message")
# Error log is visible
logger.error("Applicaton log: error message")
# Warning log from library is visible
stats = Stats()
