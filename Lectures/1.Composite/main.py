from composite import Shape, Group


def main():
    group1 = Group()
    group1.add(Shape())
    group1.add(Shape())

    group2 = Group()
    group2.add(Shape())
    group2.add(Shape())

    group = Group()
    group.add(group1)
    group.add(group2)

    group.render()


if __name__ == '__main__':
    main()
