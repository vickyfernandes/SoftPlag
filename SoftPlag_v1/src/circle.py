'''
Created on Mar 13, 2017
@author: Vicky_Fernandes
'''
import math
class Circle:
    if __name__ == '__main__':
        print("This program is used to compute the area of a circle.\n")
        while True:
            try: 
                radius = float(input('Enter radius:\t'))
                Area = math.pi * radius * radius
                print("Area of circle:\t",Area)
            except ValueError:
                print("Only integers allowed.")
            except:
                break
            finally:
                print("End of area of circle computation")
                break