#!/usr/local/bin/python3

def print_title(title):
    print('*' * (len(title) + 4))
    print('* ' + title + ' *')
    print('*' * (len(title) + 4))
    
title = input('What do you want to print? ')
print_title(title)
