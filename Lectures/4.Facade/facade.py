'''
    We use this pattern to provide a simple interface to a complex system.
'''


class Message:
    def __init__(self, content: str):
        self.content = content


class Connection:
    def disconnect(self):
        pass


class AuthToken:
    pass


class NotificationServer:
    # connect() -> Connection
    # authenticate(appId, key) -> AuthToken
    # send(authToken, message, target)
    # conn.disconnect()

    def connect(self, ip_add: str) -> Connection:
        return Connection()

    def authenticate(self, app_id: str, key: str):
        return AuthToken()

    def send(self, auth_token: AuthToken, message: Message, target: str):
        print("Sending a message")


# Facade(Front)
# All the complexity is hidden in here. if a dependent class chanegs,
# the only place that's affected is this class.
class NotificationService:
    def send(self, message: str, target: str):
        server = NotificationServer()
        connection = server.connect('172.192.11.11')
        auth_token = server.authenticate("app_id", "key")
        server.send(auth_token, Message(message), target)
        connection.disconnect()
