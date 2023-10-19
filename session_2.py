# assign values to variables
i = 3/7   #decimals are float numberes
j = 1/7


# define a function
def PrintSession_2():

# define commands for the function
	print("3/7+1/7 =", i+j)  #adds the two float numbers
	print(type(i+j))    #defines the class type
	print("15-8 =", 15-8)    #subtract two integers
	print(type(15-8))	# define type
	print("3/7*4 = ", i*4)	#multiply int and float
	print(type(i*4))	#define type
	
# define our function as the main function
def main():
	PrintSession_2()

# ensure the main is executed when commanded
if __name__== "__main__":
	main()
