from configparser import ConfigParser
import argparse
import os

def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("config_file", type=str, help="Configuration file")
    args = parser.parse_args()
    return args

def program():

    print "Welcome to CONTACT-TOOLS SDK"

    import globals
    globals.init()

    parsed_input = parse_input()
    parser = ConfigParser()
    parser.read(os.path.expanduser(parsed_input.config_file))

    print "Reading configuration: "
    access_token = parser.get('secret', 'access_token')
    url = parser.get('secret', 'url')
    endpoint = parser.get('secret', 'endpoint')

    print access_token
    print url
    print endpoint

def main():
    try:
        program()
    except Exception as e:
        print e

if __name__ == "__main__":
    main()
