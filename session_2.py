# assign values to variables
i = 3/7
j = 1/7


# define a function
def PrintSession_2():

# define commands for the function
	a = print("3/7+1/7 =", i+j)
	print(type(a))
	b = print("15-8 =", 15-8)
	print(type(b))
	c = print("3/7*4 = ", i*4)
	print(type(c))
	
# define our function as the main function
def main():
	PrintSession_2()

# ensure the main is executed when commanded
if __name__== "__main__":
	main()
