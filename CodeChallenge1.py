# How many candles should be moved in order to turn isosceles triangle to a square?
import math


def get_movable_candles(n):
    no_of_rows = int(math.sqrt(n))
    print(type(no_of_rows))
    movable_candles = 0
    for i in range(1, no_of_rows):
        no_of_candles_in_i = (2 * i) - 1
        if no_of_candles_in_i < no_of_rows:
            temp = (no_of_rows - no_of_candles_in_i)
            movable_candles += temp
    return movable_candles


no_of_candles = int(input('Enter the no. of candles'))
print(get_movable_candles(no_of_candles))