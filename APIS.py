import requests
import json

# 1. POST Request – Creating a New Post
url = 'https://jsonplaceholder.typicode.com/posts'

# Data to be sent in POST request
payload = {  
    "userId": 45,
    "title": "The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking",
    "body": "It is our choices, Harry, that show what we truly are, far more than our abilities."
}

headers = {'Content-Type': 'application/json'}
response = requests.post(url, json=payload, headers=headers)

# Check response for POST request
print("POST Status Code:", response.status_code)
print("POST Response:", response.json()) 

# -------------------------------------------------------------------

# 2. GET Request – Fetching All Posts
response = requests.get('https://jsonplaceholder.typicode.com/posts')

# If request is successful, print data
if response.status_code == 200:
    data = response.json()
    pretty_data = json.dumps(data, indent=4)  
    print("GET Request Data:", pretty_data)
else:
    print('GET Request Failed')

# -------------------------------------------------------------------

# 3. PUT Request – Updating an Existing Post
url = 'https://jsonplaceholder.typicode.com/posts/1'  

# Data to replace the entire post
payload = {  
    "Id": 101,  
    "userId": 45,
    "title": "Updated Title",
    "body": "Updated body of the post."
}

# PUT request to update post
response = requests.put(url, json=payload, headers=headers)

print("PUT Status Code:", response.status_code)  
print("PUT Response:", response.json())  

# -------------------------------------------------------------------

# 4. DELETE Request – Deleting a Post
url = 'https://jsonplaceholder.typicode.com/posts/1'  # Deleting post with ID 1

response = requests.delete(url)
print("DELETE Status Code:", response.status_code) 
