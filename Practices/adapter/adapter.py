from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class EmailProvider(ABC):
    @abstractmethod
    def download_emails(self):
        pass


class LocalProvider(EmailProvider):
    def download_emails(self):
        print("Connecting to local email provider.")


class EmailClient:
    def __init__(self):
        self.providers: List[EmailProvider] = []

    def add(self, provider: EmailProvider):
        self.providers.append(provider)

    def download_emails(self):
        for provider in self.providers:
            provider.download_emails()


# Now Google provides following interface to connect to Gmail
# But it doesn't conform to our interface. By using Adapter
# pattern, we make it conform to our interface.
class GmailClient:
    def connect(self):
        print("Connecting to Gmail")

    def get_emails(self):
        print("Downloading emails from Gmail")

    def disconnect(self):
        print("Disconnecting from Gmail")


# Adapter
class GmailAdapter(EmailProvider):
    def __init__(self, gmail_client: GmailClient):
        self.gmail_client = gmail_client

    def download_emails(self):
        self.gmail_client.connect()
        self.gmail_client.get_emails()
        self.gmail_client.disconnect()


def main():
    client1 = LocalProvider()
    client2 = LocalProvider()
    gmail = GmailAdapter(GmailClient())

    clients = EmailClient()
    clients.add(client1)
    clients.add(client2)
    clients.add(gmail)

    clients.download_emails()


if __name__ == '__main__':
    main()
