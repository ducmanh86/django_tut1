def challenge():
    """
    main function for test
    """
    for i in range(30, 301):
        if i % 7 == 0 and i % 13 == 0:
            print('a-z')
        elif i % 7 == 0:
            print('abc')
        elif i % 13 == 0:
            print('xyz')
        else:
            print(i)

if __name__ == '__main__':
    challenge()
