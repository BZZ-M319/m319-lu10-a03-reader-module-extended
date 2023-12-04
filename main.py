from input_reader import read_int, read_float
def main():
    # do something to show functionality
    mark = read_float('Please enter a mark for your python class> ', lower_bound= 0, upper_bound= 6)
    score_0_to_100 = read_int('Please enter a whole number between 0 and 100> ', lower_bound = 0, upper_bound = 100)
    positive_zahl = read_int('Please enter a positive whole number> ', lower_bound = 1)
    negative_zahl = read_int('Please enter a negative whole number> ', upper_bound = -1)

    print('Your mark is: ', mark)
    print('Your rating is: ', score_0_to_100)
    print('Your positive number is: ', positive_zahl)
    print('Your negative number is: ', negative_zahl)


if __name__ == '__main__':
    main()