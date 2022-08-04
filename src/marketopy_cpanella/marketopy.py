import argparse
import os
import json

def main():
    # substitute the default Munchkin ID here to make using the tool via the command line easier
    DEFAULT_MUNCHKIN = ""
    DEFAULT_CLIENT_ID = ""
    DEFAULT_CLIENT_SECRET = ""
    parser = argparse.ArgumentParser()



    parser.add_argument('-m', '--munchkin', help="munchkin ID of the instance",
                        default=DEFAULT_MUNCHKIN)
    parser.add_argument('-t', '--threads', help="number of threads to spawn for lead creation, default is 5",
                        default="5", type=int)
    parser.add_argument('-s', '--service',
                        help="service to run on the targeted REST API. (createLeads, createPrograms, bulk, etc.)",
                        default="")
    # substitute the default Client ID here to make using the tool via the command line easier
    parser.add_argument('-i', '--client_id', help="Client ID from custom launchpoint service",
                        default=DEFAULT_CLIENT_ID)
    # substitute the default Client Secret here to make using the tool via the command line easier
    parser.add_argument('-e', '--client_secret', help="Client secret from custom lauchpoint service",
                        default=DEFAULT_CLIENT_SECRET)
    parser.add_argument('-q', '--quantity', help="number of leads or assets to create, default is 10", default="10",
                        type=int)
    parser.add_argument('-k', '--known', help="the number associated to the subscriptions position in the subscriptions.csv", type=int)

    # save arguments values
    args = parser.parse_args()

    # store values in global vars
    service = str(args.service).lower()
    munchkin_id = args.munchkin
    client_secret = args.client_secret
    client_id = args.client_id
    threads = int(args.threads)
    quantity = int(args.quantity)

    # checks to see if we are using a sub within the subscriptions.csv config file
    if args.known != "" and args.known > 0:
        print()
        print("Subscription is known, checking configuration file...")
        print()
        munchkin_id, client_id, client_secret = config_reader.get_subscription_info(args.known)
    elif args.known < 0:
        config_reader.read_options_to_user()
        sys.exit(0)

    # create an instance of auth to save data to
    try:
        auth = subscription.LaunchPoint(munchkin_id, client_id, client_secret)
    except:
        print()
        print("Unable to create auth object.")
        print("Please validate that munchkin, client_id and client_secret exist.")
        print()
        sys.exit(0)

    # if service is empty it will print out instructions for the user
    if service == "":
        print()
        print("Service not recognized. Available services are:")
        print("    - bulk              - creates random leads to be bulk imported into a subscription")
        print("    - mix               - creates a set of mixed leads (by country) to be bulk imported")
        print("    - createPrograms    - creates webinar event programs in a subcription")
        print("    - pushLeads         - syncs bulk leads with programs")
        print("    - token             - gets a auth token from a subscription")
        print()
        print("Examples: ")
        print("     python3 apitool.py -s bulk -q 10000")
        print("     python3 apitool.py -s createPrograms -q 10")
        print("     python3 apitool.py -s token")
        print("     python3 apitool.py --help")
        print()
        sys.exit(0)



    if munchkin != "" and munchkin is not None
        and client_id != "" and client_id is not None
        and client_secret != "" and client_secret is not None
        or

    kafka_conf = conf.get_kafka_config()
    ims_conf = conf.get_ims_config()

if __name__ == "__main__":
    main()