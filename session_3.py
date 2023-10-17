#define x as an integer the user inputs
x = int(input('x = '))

#define the function we want executed
def practice():				#name the function
	print(f'{x}**3 + 8')	#print the value of the integer inputed into the function we want
	y = x**3 + 8			# define y as the actual function f(x)
	print(y)
	if y>27:				# this needs to be underneath the code of the function otherwise y isn't defined
		print("YAY!")				


#define main function
def main():
	practice()

#call this as the inital command
if __name__ == "__main__":
	main()


