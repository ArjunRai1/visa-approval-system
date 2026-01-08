from visa_approval_system.exception import USvisaException
import sys
from visa_approval_system.logger import logging

logging.info("Testing exception module")

try:
    a = 2/0
except Exception as e:
    raise USvisaException(e, sys)