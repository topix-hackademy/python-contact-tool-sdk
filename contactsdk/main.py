from configparser import ConfigParser
import argparse
import os

from contactsdk.connector import Connector

def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("config_file", type=str, help="Configuration file")
    args = parser.parse_args()
    return args

def program():

    print "*********************************************"
    print "* Welcome to CONTACT-TOOLS SDK Command Line *"
    print "*********************************************"

    import globals
    globals.init()

    parsed_input = parse_input()
    parser = ConfigParser()
    parser.read(os.path.expanduser(parsed_input.config_file))

    access_token = parser.get('secret', 'access_token')
    base_url = parser.get('secret', 'base_url')
    endpoint = parser.get('secret', 'endpoint')

    # Create Connector
    connector = Connector(access_token, base_url, endpoint)

    print "\n#### Read Configuration from %s ####" % parsed_input.config_file
    print connector

def main():
    try:
        program()
    except Exception as e:
        print e

if __name__ == "__main__":
    main()
