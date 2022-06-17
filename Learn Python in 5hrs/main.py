# Tutorial: https://m.youtube.com/watch?v=t8pPdKYpowI
# Introduces PyCharm IDE, which is now my preferred IDE on my Linux Distro
# Altered to present in an interactive environment, which also increased learning
import requests


def get_projects():
    response = requests.get(f"https://gitlab.com/api/v4/users/{user_id}/projects")
    my_projects = response.json()

    for project in my_projects:
        print(f"Project Name: {project['name']}\nProject Url: {project['web_url']}\n")


user_id = None
while user_id != "q":
    user_id = input("Please enter the User Name or type q to quit: ") or "nanuchi"
    if user_id == "q":
        print("All Done, bye ;D")
        continue
    try:
        get_projects()
    except TypeError:
        print('There was an error with that user name!')
        continue
