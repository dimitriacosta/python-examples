"""

********************************
* Print an empty box like this *
********************************

"""

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a string of lenght 1.')
    if (width < 2) or (height < 2):
        raise Exception('"width" and "heoght" must be greater or equal to 2.')

    print(symbol * width)

    for _ in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

symbol = input('Type the symbol: ')
width = input('Type the width: ')
height = input('Type the height: ')
boxPrint(symbol, int(width), int(height))
