from facade import (
    Message, AuthToken, Connection, NotificationServer, NotificationService
)


def main():
    # LOTS OF WORK TO DO!
    # server = NotificationServer()
    # connection = server.connect('172.192.11.11')
    # auth_token = server.authenticate("app_id", "key")
    # message = Message("Hello world")
    # server.send(auth_token, message, "target")
    # connection.disconnect()
    service = NotificationService()
    service.send("Hello World", "target")
