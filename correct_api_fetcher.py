import requests 
import json 

users = []
user_posts = []
current_user = {}

def menu():
    print("Menu:")
    print("1. View all users")
    print("2. View selected user")
    print("3. View selected user's posts")
    print("4. Exit")
    choice = int(input("Input your choice: "))
    return choice

def display_users():
    if not users:
        print("No user data available, please check your network or try again later.")
        return
    print("All users:")
    print("-"*11)
    for index, user in enumerate(users, 1): 
        if "id" in user and "name" in user:
            print(f"{index}. Name: {user['name']}, Id: {user['id']}")

def display_user_details(id_choice):
    if not users:
        print("No user data available, please check your network or try again later.")
        return
    print("User details:")
    print("-"*11)
    user_found = False
    global current_user  
    for user in users:
        if "id" in user and user["id"] == id_choice:
            current_user = user  
            print(f"Name: {user['name']}")
            print(f"Id: {user['id']}")
            print(f"Email: {user['email']}")
            print("Address:")
            print(f"  Street: {user['address']['street']}")
            print(f"  City: {user['address']['city']}")
            print(f"  Zipcode: {user['address']['zipcode']}")
            user_found = True
            break
    if not user_found:
        print(f"User with ID {id_choice} not found.")

def fetch_user_posts(id_choice):
    global user_posts
    user_posts = []
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
    if not user_posts:
        print("No post data available for this user.")
        return
    print("User posts")
    print("-"*11)
    print(f"Posts by {current_user.get('name', 'Unknown User')}:")
    for index, post in enumerate(user_posts, 1):
        print(f"{index}. {post['title'][:30]}...")
    
    while True:
        try:
            view = int(input("View full post? (enter 0 for no, 1 for yes): "))
            break
        except ValueError:
            print("Invalid input, please enter 0 or 1.")
    
    if view == 1:
        while True:
            try:
                post_index = int(input(f"Enter post number (1-{len(user_posts)}): ")) - 1
                if 0 <= post_index < len(user_posts):
                    selected_post = user_posts[post_index]
                    print(f"\nTitle: {selected_post['title']}")
                    print(f"Body: {selected_post['body']}")  
                    break
                else:
                    print(f"Invalid post number, please enter a number between 1 and {len(user_posts)}.")
            except ValueError:
                print("Invalid input, please enter a valid number.")

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

#main loop
while True:
    choice = menu()
    
    if choice == 1:
        display_users()

    elif choice == 2:
        while True:
            try:
                id_choice = int(input("Enter user id: "))
                break
            except ValueError:
                print("Invalid input, please enter a valid number for user ID.")
        display_user_details(id_choice)

    elif choice == 3:
        while True:
            try:
                id_choice = int(input("Enter user id: "))
                break
            except ValueError:
                print("Invalid input, please enter a valid number for user ID.")
        fetch_user_posts(id_choice)
        display_user_posts()
        
    elif choice == 4:  
        print("Thanks for using reminisce's api fetcher")
        break
    
    else: 
        print("Invalid choice, please enter a number between 1 and 4.")
    
   
    print("\n" + "-"*30 + "\n")
