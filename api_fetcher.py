import requests 
import json 

def menu():
	print("Menu:")
	print("1. View all users")
	print("2. View selected user")
	print("3. View selected user's posts")
	print("4. Exit")
	choice = int(input("Input your choice: "))


print("Welcome to reminisce's api fetcher!")
try:
    response = requests.get("https://jsonplaceholder.typicode.com/users", timeout=5)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.Timeout:
    print("Request timed out. Please try again.")
except requests.exceptions.ConnectionError:
    print("Connection error. Check your internet.")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")

while True:
	menu()
	if choice == 1:
		print("All users:")
		print("-"*11)
		user = next((u for u in users if u["id"] == user_id), None)
		if user:
    		print(f"Name: user['name']")
		else:
			print("User not found")

	elif choice == 2:
		print("User details:")
		print("-"*11)
		user_id = int(input("Input user Id: "))
		user = next((u for u in users if u["id"] == user_id), None)
		if user:
    		print(f"Name: user['name']")
			print(f"Username: user['username']")
			print(f"Email: user['email']")
		else:
    		print("User not found")

	elif choice == 3:
		post_data = response.fetch(

	else:
		print("Thanks for using reminisce's api fetcher")
		break
	
	

