
try: 
	a = int(input("Input an integer: "))
	b = int(input("Input another integer: "))

	sum = a+b
	difference = a-b
	product = a*b
	quotient = a/b
except ZeroDivisionError:
	quotient= "cannot divide by zero"
except ValueError:
	quotient = "not a number"
finally:
	print(sum)
	print(difference)
	print(product)
	print(quotient)
  
  
