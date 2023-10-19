#define a class (a blueprint for an object) with
#an initial set of parameters

import sys

class Shape: #blueprint for shapes

	#this is the program that defines what is basically
	#going to be printed

	def print(whale):
		print("This is my whale <3")
		print(f"length of fin = {whale.fin}")
		print(f"length of tail = {whale.tail}")
		print(f"number of eyes = {whale.eye}")
		# enter an f'string so that you can easily combine 
		# the text explanation with the input numerical value
		yes = True
		no = False
		print("It has a tail = ", yes )
		print("It is furry = ", no )
		#i could have replaced yes/no with just True which is bool I think


	def __init__(whale,fn=25,tl=30,eye=2):
		whale.fin = float(fn)  #describes this number as a float
		whale.tail = float(tl)
		whale.eye = int(eye)  # this becomes an integer

#our main and only program runs these values. This is the measure of my whale

def main():
	
	fn = 25
	tl = 30
	eye = 2


#describe the components of the shape and names it

	my_whale = Shape(fn=fn,tl=tl,eye=eye)
# print the shape
	my_whale.print()

# main that our main function
if __name__ == "__main__":
	main()