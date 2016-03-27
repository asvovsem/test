from colorama import *

def pos(x,y):
    return '\x1b[' + str(y) + ';' + str(x) + 'H'
def main():

    print ("Typo your favourite x and y posses")
    x1 = input()
    y1 = input()
    print (Fore.WHITE + pos( x1, y1) + "this")
    input()
if (__name__ == "__main__" ):
    main()
