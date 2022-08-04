import sys
import pandas as pd

def read_configuration_file():
    try:
        subscriptions = pd.read_csv('subscriptions.csv')
    except:
        print("Unable to find the subscriptions.csv file. Please create one within the venv.")
        sys.exit(0)
    try:
        munchkinList = subscriptions.munchkin_id
    except:
        print("The subscriptions.csv file does not follow the correct naming convention")
        print("Please ensure the column headers are labeled as the following: ")
        print("munchkin_id, client_id, client_secret, environment")
        sys.exit(0)
    return munchkinList

def read_options_to_user():
    munchkinList = read_configuration_file()
    i = 0
    print("Options in Config File: ")
    for munchkin_id in munchkinList:
        print(str(i) + " " + munchkin_id)
        i += 1

def get_subscription_info(knownSubscription):
    subscriptions = pd.read_csv('subscriptions.csv')
    munchkin_ids = subscriptions.munchkin_id
    client_ids = subscriptions.client_id
    client_secrets = subscriptions.client_secret
    print()
    print("Using Sub: \n {0} \n {1} \n {2}".format(munchkin_ids[knownSubscription], client_ids[knownSubscription], client_secrets[knownSubscription]))
    print()

    return munchkin_ids[knownSubscription], client_ids[knownSubscription], client_secrets[knownSubscription]
