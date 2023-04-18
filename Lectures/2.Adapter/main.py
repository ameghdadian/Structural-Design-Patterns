from adapter import Image, ImageView, VividFilter, Caramel, CaramelFilter


def main():
    image_view = ImageView(Image())
    image_view.apply(CaramelFilter(Caramel()))


if __name__ == '__main__':
    main()
