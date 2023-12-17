from login import *
from credentials import *

#logout
try:
    logout=smartApi.terminateSession(username)
    logger.info("Logout Successfull")
except Exception as e:
    logger.exception(f"Logout failed: {e}")