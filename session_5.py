import numpy as np #for working with numbers
from astropy.table import Table #for creating the table class

pi = np.pi  # pi doesn't mean anything unless yo apply numpy to it. they it has the value of pi
x = np.linspace(0,pi*2,1000) # x creates the line space of range 0 to 2 pi with 1000 values between
y = np.sin(x) # the function that each x is plugged into

data = Table([x,y], names=['x','y']) #creates the table and structure and names each columN

print(data)  #prints the function
