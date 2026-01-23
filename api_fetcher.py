import requests 
import json 

def menu():
	print("Menu:")
	print("1. View all users")
	print("2. View selected user")
	print("3. View selected user's posts")
	print("4. Exit")
	choice = int(input("Input your choice: "))

def fetch_users():
	print("All users:")
	print("-"*11)
	for user in users: 
		if "id" in user and "name" in user:
			print(f"{index}. Name: {user['name']}, Id: {user['Id']}")

def fetch_user_details(id_choice):
	print("User details:")
	print("-"*11)
	for user in users:
		if id_choice in user:
			print(f"Name: {user['name']}")
			print(f"Id: {user['Id']}")
			print(f"Email: {user['email']}")
			print("Address:")
			print(f"  Street: {user['address']['street']}")
			print(f"  Suite: {user['address']['suite']}")
			print(f"  City: {user['address']['city']}")

def fetch_user_posts(id_choice):
	print("User posts")
	print("-"*11)
	
	
	
#start
print("Welcome to reminisce's api fetcher!")
try:
    response = requests.get("https://jsonplaceholder.typicode.com/users", timeout=5)
    response.raise_for_status()
    users = response.json()
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
		fetch_users()

	elif choice == 2:
		id_choice = int(input("Enter user Id: "))
		fetch_user_details(id_choice)
		

	elif choice == 3:
		id_choice = int(input("Enter user Id: "))
		fetch_user_posts(id_choice)
		
	else:
		print("Thanks for using reminisce's api fetcher")
		break
	
	

