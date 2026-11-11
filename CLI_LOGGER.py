from GLOBAL_ROUTE import route
import OWN_FORMATTER
from pathlib import Path
import logging.config

routes = Path(route.get())
log_archive = routes / "CLI_LOG.log"

config = {
   "version" : 1,
   "disable_existing_loggers" : False,
   "formatters" : {
       "custom" : {
           "()" : OWN_FORMATTER.CLIFormatter
       }
   },
   "handlers" : {
       "CLI" : {
           "class" : "logging.StreamHandler",
           "formatter" : "custom",
           "level" : "INFO"
       },
       "FILE" : {
           "class" : "logging.FileHandler",
           "filename" : log_archive,
           "formatter" : "custom",
           "level" : "INFO"
       }
   },
   "root" : {
       "level" : "INFO",

       "handlers" : [
           "CLI",
           "FILE"
       ]
   }
}

logging.config.dictConfig(config)