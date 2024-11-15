import requests
import os
import shutil
from datetime import datetime

folder_name= "yaw_mintah"
file_name = "yaw_mintah.txt"
file_path = os.path.join(folder_name, file_name)

# creating folder if it doesn't exists
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f'Directory {folder_name}, created successfully')

# creating and inputting file if it doesn't exists
if os.path.exists(file_path):
    print(f"File {file_name}, already exists in {folder_name}.")
else:
    with open(file_path, 'w') as file:
        file.write("Welcome guys!!")
    print('file created')


# downloading file from url
url = "https://raw.githubusercontent.com/sdg000/pydevops_intro_lab/main/change_me.txt"

response = requests.get(url)

if response.status_code == 200:
    print(f"File successfully downloaded.")
    with open(file_path, "wb") as file:
        file.write(response.content)
        print('File saved successfully.')
else:
    print(f"Failed to download file. Status code: {response.status_code}")

# overwriting file content
user_input = input("Describe what you have learned so far in a sentence: ")
now = datetime.now()
print(now)
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

with open(file_path, 'w') as file:
    file.write(user_input + "\n")
    file.write(f"Last modified on: {current_time}")
    print("File successfully modified.")

with open(file_path, 'r') as file:
    print("\nYou Entered: ", end=' ')
    print(file.read())