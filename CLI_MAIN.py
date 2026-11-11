#To get the user route by a ContextVar
from GLOBAL_ROUTE import route
from CLI_CONFIG import args
import logging
import CLI_CONFIG

route.set(args.route)

#get the logger config
import CLI_LOGGER

logger = logging.getLogger(CLI_LOGGER.__name__)
logger.info(CLI_CONFIG.main()) #Use the return as logs