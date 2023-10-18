import numpy as np #for working with numbers
from astropy.table import Table #for creating the table class
from astropy.io import ascii
from astropy.io import fits

pi = np.pi
x = np.linspace(0,pi*2,1000)
y = np.sin(x)

data = Table([x,y], names=['x','y'])
ascii.write(data, 'table.txt', format='commented_header')
data_in = ascii.read('table.txt')

print(data_in)
