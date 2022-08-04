from os.path import exists
import time
import requests

class Authentication:

    def __init__(self, munchkin_id, client_id, client_secret):
        self.auth_url = "https://{0}.mktorest.com/identity/oauth/token?grant_type=client_credentials&client_id={1}&client_secret={2}"
        secrets_exist = self.__check_for_secrets__()
        if secrets_exist:
            import secrets
            self.secrets = secrets.SUBSCRIPTION_INFORMATION
        else:
            self.secrets = None
        self.munchkin_id = munchkin_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.TOKEN_SLEEP_TIME = 5  # In Seconds


    def __check_for_secrets__(self):
        return exists("secrets.py")

    def getAuthToken(self):
        if self.token < self.TOKEN_SLEEP_TIME:
            time.sleep(self.TOKEN_SLEEP_TIME)
            return self.__get_new_token__()
        else:
            return self.__get_new_token__()

    def __get_new_token__(self):
        if self.secrets is not None:
            import secrets
            print("ARRAY ENTRY WILL BE SUPPORTED IN THE FUTURE")
            self.munchkin_id = secrets.SUBSCRIPTION_INFORMATION[0]["MUNCHKIN_ID"]
            self.client_id = secrets.SUBSCRIPTION_INFORMATION[0]["CLIENT_ID"]
            self.client_secret = secrets.SUBSCRIPTION_INFORMATION[0]["CLIENT_SECRET"]
            for subscription in secrets.SUBSCRIPTION_INFORMATION:
                print('Subscription Details:\nMunchkin: {0}\nClient ID: {1}'
                      .format(subscription["MUNCHKIN_ID"], subscription["CLIENT_ID"]))
        else:
            response = requests.get(self.auth_url.format(self.munchkin_id, self.client_id, self.client_secret))
        return self.token
