import requests 
import json 

def menu():
	print("Menu:")
	print("1. View all users")
	print("2. View selected user")
	print("3. View selected user's posts")
	print("4. Exit")
	choice = int(input("Input your choice: "))

def display_users():
	print("All users:")
	print("-"*11)
	for index, user in enumerate(users,1): 
		if "id" in user and "name" in user:
			print(f"{index}. Name: {user['name']}, Id: {user['id']}")

def display_user_details(id_choice):
	print("User details:")
	print("-"*11)
	for user in users:
		if id_choice in user:
			print(f"Name: {user['name']}")
			print(f"Id: {user['Id']}")
			print(f"Email: {user['email']}")
			print("Address:")
			print(f"  Street: {user['address']['street']}")
			print(f"  City: {user['address']['city']}")
			print(f"  Zipcode: {user['address']['zipcode']}")

def fetch_user_posts(id_choice):
	try:
    	post_response = requests.get(f"https://jsonplaceholder.typicode.com/posts?userId={id_choice}", timeout=5)
    	post_response.raise_for_status()
    	user_posts = post_response.json()
	except requests.exceptions.Timeout:
    	print("Request timed out. Please try again.")
	except requests.exceptions.ConnectionError:
    	print("Connection error. Check your internet.")
	except requests.exceptions.HTTPError as e:
    	print(f"HTTP error: {e}")
	except requests.exceptions.RequestException as e:
    	print(f"Request failed: {e}")
	
def display_user_posts():
	print("User posts")
	print("-"*11)
	print("Posts by {user['name']}:")
	for index, post in enumerate(user_posts):
		print(f"{index}. {post['title'][:30]}...")
	view = int(input("View full post? (enter 0 for no, 1 for yes)"))
	if view == 0:
		menu()
	else:
		print(f"Title: {post['title']}")
		print(f"Body: {post['body'][:50]}")
	
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
		display_users()

	elif choice == 2:
		id_choice = int(input("Enter user id: "))
		display_user_details(id_choice)
		

	elif choice == 3:
		id_choice = int(input("Enter user id: "))
		fetch_user_posts(id_choice)
		display_user_posts()
		
	else:
		print("Thanks for using reminisce's api fetcher")
		break
	
	

