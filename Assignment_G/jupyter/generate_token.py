#!/usr/bin/env sh
# import IPython as IPython
# import bcrypt
import hashlib

# python generate_token.py --password=password
#
# Generate a access token
# Copy this line into the .env file:
# ACCESS_TOKEN=5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8

if __name__ == "__main__":
    print("Generate a access token")
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("-p",
        "--password", 
        dest="password",
        help="The password you want to use for authentication.",
        required=True)
    args = parser.parse_args()

    print("\nCopy this line into the .env file:\n")
    # hash = IPython.lib.passwd(args.password)
    dataBase_password = args.password
    hash = hashlib.sha1(dataBase_password.encode()).hexdigest()
    print("ACCESS_TOKEN=" + hash)
