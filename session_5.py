import numpy as np #for working with numbers
from astropy.table import Table #for creating the table class
from astropy.io import ascii  # I don't know why we need this
from astropy.io import fits   # i dont know why we need this

pi = np.pi  # pi doesn't mean anything unless yo apply numpy to it. they it has the value of pi
x = np.linspace(0,pi*2,1000) # x creates the line space of range 0 to 2 pi with 1000 values between
y = np.sin(x) # the function that each x is plugged into

data = Table([x,y], names=['x','y']) #creates the table and structure and names each column
ascii.write(data, 'table.txt', format='commented_header') #make the information in the table into a text file
data_in = ascii.read('table.txt')  #defines the function as a file to read

print(data_in)  #prints the function
