from baseClass import baseClass


def main():
    me = baseClass()
    print(me.text)
    print('is warren happy: {0}'.format(me.isHappy()))

    if me.isHappy():
        me.giveBeer()
    else:
        me.giveBeer()
        me.giveBeer()
        me.giveBeer()

    print('is warren happy: {0} with {1} beers'.format(me.isHappy(), me.beer))



if __name__ == '__main__':
    main()