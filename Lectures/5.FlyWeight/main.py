from flyweight import Point, PointService


def main():
    service = PointService()
    for point in service.get_points():
        point.draw()


if __name__ == '__main__':
    main()
