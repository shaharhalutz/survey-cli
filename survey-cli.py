#!/usr/bin/env python

import sys, argparse, logging
from argparse import RawTextHelpFormatter
import json
from notifications import send_notification
from db import get_users
from utils import create_url

def push(filename):

    # Config:
    try:
        f = open(filename, 'r') 
    except IOError:
        logging.error("Config File does not exist, please provide a config file.(please see config.example.json)")
        return 
    
    try:
        config = json.load(f)
    except :
        logging.error("Config File is not formated correctly. (please see config.example.json)")
        return 
    
    logging.debug("recieved Config: %s" % config)

    # create notification:
    message = config["notification"]["message"]
    users = get_users(config)

    # DEBUG:
    logging.info("notifications to push: %s" % str(len(users) ))

    # push to Users:
    sent = []
    not_sent = []
    for user in users:
      token = user["token"]
      #uuid = user["uuid"]
      url = create_url(config,token)
      push_success = send_notification(token,message,url)
      if push_success:
        sent.append(token)
      else:
        not_sent.append(token)
        
    logging.info("pushed successfuly : %s" % str(len(sent) ))

    if len(not_sent):
      logging.error("error sending to : {}".format(' '.join(map(str, not_sent))))



# Main
def main(args, loglevel):
  logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)
  logging.info("Pushing notifications according to config file: %s" % args.argument)
  push(args.argument)

# MAIN:
if __name__ == '__main__':
  parser = argparse.ArgumentParser( formatter_class = RawTextHelpFormatter,
                                    description = "push batch of notifications to survey users according to config file.",
                                    epilog = "Please see config.example.json as a reference configuration. \n",
                                    fromfile_prefix_chars = '@' )

  # Parameters:
  parser.add_argument(
                      "argument",
                      help = "Pass a config filename",
                      metavar = "Filename")
  parser.add_argument(
                      "-v",
                      "--verbose",
                      help="increase output verbosity",
                      action="store_true")
  parser.add_argument(
                      "-p",
                      "--push",
                      help="push Notifications",
                      action="store_true")

  args = parser.parse_args()
  
  # Setup logging
  if args.verbose:
    loglevel = logging.DEBUG
  else:
    loglevel = logging.INFO
  
  # Main:
  main(args,loglevel)
  