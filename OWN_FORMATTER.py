import logging
import time

class CLIFormatter(logging.Formatter):
   def format(self, record):
       cli_time = time.strftime("%Y/%m/%d at %I:%M %p", time.localtime())
       return (
           f"{cli_time} | {record.msg}"
       )