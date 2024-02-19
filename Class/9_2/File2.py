import File1
File1.mult(3)
x = 4
File1.mult(3)#this returns 81 still because x was defined in the last function
print(File1.mult(3))


x = 4
print(f"File1.mult(3) = {File1.mult(3)}")
#can edit the name space by putting the file name "." what you are trying to do
#so...
print(File1.x) # prints out the value of x #which is 27

 name = File 1
#  name = __main__
# this make name the parent file and then you should say 
if __name__ == '__main__':
	assert mult(1) = 27
from math import pi as whatever_you_want
import numpy as np
import scipy as sp
from matplotlib import pyplot as plt
# from *module* import *this* as *bleh*
# from module import *
from math import * # dangerous bc you can get conflicts, not a good practice, should not use it
