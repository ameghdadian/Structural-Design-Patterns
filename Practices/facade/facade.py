from typing import List


class OAuth:
    def request_token(self, app_key: str, app_secret: str):
        print("Get a request token")
        return "requestToken"

    def get_access_token(self, request_token: str):
        print("Get an access token")
        return "accessToken"


class Tweet:
    pass


class TwitterClient:
    def get_recent_tweets(self, access_token: str) -> List[Tweet]:
        print("Getting recent tweets")

        return []


class TwitterAPI:
    def __init__(self, app_key: str, app_secret: str):
        self.app_key = app_key
        self.app_secret = app_secret

    def get_access_token(self):
        oauth = OAuth()
        request_token = oauth.request_token(self.app_key, self.app_secret)
        access_token = oauth.get_access_token(request_token)

        return access_token

    def get_recent_tweets(self):
        client = TwitterClient()
        client.get_recent_tweets(self.get_access_token())


def main():
    api = TwitterAPI("app_key", "app_secret")
    api.get_recent_tweets()


if __name__ == '__main__':
    main()
