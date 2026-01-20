
try: 
	a = int(input("Input an integer"))
	b = int(input("Input another integer"))

	sum = a+b
	difference = a-b
	product = a*b
	quotient = a/b
except ZeroDivisionError:
	print("cannot divide by zero")
except ValueError:
	print("not a number")
finally:
	print(sum)
	print(difference)
	print(product)
	print(quotient)
  
  
