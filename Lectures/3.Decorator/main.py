from decorator import CloudStream, Stream, EncryptedCloudStream, CompressedCloudStream


def main():
    # store_credit_card(EncryptedCloudStream(CloudStream()))
    # store_credit_card(CompressedCloudStream(CloudStream()))
    store_credit_card(
        EncryptedCloudStream(CompressedCloudStream(CloudStream()))
    )


def store_credit_card(stream: Stream):
    stream.write("1234-1234-1234-1234")


if __name__ == '__main__':
    main()
