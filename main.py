def main():
    while True:
        try:
            print('Enter a filename: ')
            x = input()
            f = open(x, 'r')
            print(f.read())
            while True:
                try:
                    print('Enter a quicksort variant: ')
                    x = input()
                    y = ['first', 'median3', 'random']
                    if x not in y:
                            raise NameError
                    break;
                except NameError:
                    print('Incorrect variant. Options are "first", "median3", or "random".')
            break
        except IOError:
            print('File does not exist.\n')
main()
