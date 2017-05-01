'''
Created on Mar 13, 2017

@author: Vicky Fernandes
'''
class Rectangle:
    if __name__ == '__main__':
        print("This program is used to compute the area of a rectangle.\n")
        while True:
            try:
                width = float(input('Enter width:\t'))
                length = float(input('enter length:\t'))
                '''
                Now is the time you're going to see something exceptionally great!
                We are going to compute the area of a rectangle.
                '''
                Area = length * width
                print("Area of rectangle:\t",Area)
            except ValueError:
                print("Only integers allowed!")
            except:
                break
            finally:
                print("End of area of rectangle computation")
                break