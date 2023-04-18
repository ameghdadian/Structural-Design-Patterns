from proxy import Library, Ebook, EbookProxy, LoggingEbookProxy


def main():
    library = Library()
    filenames = ['a', 'b', 'c']
    for filename in filenames:
        library.add(LoggingEbookProxy(filename))

    library.open_ebook('a')
    library.open_ebook('b')


if __name__ == '__main__':
    main()
