import requests 
import json 

def menu():
	print("Menu:")
	print("1. View all users")
	print("2. View selected user")
	print("3. View selected user's posts")
	print("4. Exit")
	choice = int(input("Input your choice: "))

response = requests("https://jsonplaceholder.typicode.com/users")
content = response.content
print("Welcome to reminisce's ali fetcher!")
menu()

if choice == 1:
	

