import requests
from getpass import getpass
import json
import os

args = json.loads(open(f'backend/static/json/views.json', 'r').read())
arr = []
file_name = __file__.split(os.path.sep)[-1]
for arg in args['views']:
  if 'console_view' in args['views'][arg]:
    if len([x for x in args['views'][arg]['console_view'] if file_name in x]) > 0:
      arr.append(int(arg))
options = ''
for x in arr:
  options += f"{x}) Methods: {','.join(args['views'][str(x)]['methods'])}, "
  options += f"type: {args['views'][str(x)]['type']}, "
  options += f"URL: {args['views'][str(x)]['url']}/{args['views'][str(x)]['view']}, "
  options += f"""\n{
    args['views'][str(x)]['description'].replace('<br><span class=info>', '`n').replace('</span>', '')
    }\n\n""".replace('`n', '\n')
print(options)

repeat = True
show = False
while repeat:
  if show:
    print(options)
    show = False
  req = input('Please enter the number from one of the options: ').split(' ', 2)
  if req[0] != '' and int(req[0]) in arr:
    if len(req) > 1 and req[1]:
      url = f"{args['views'][req[0]]['url'][:-8]}{req[1]}/update/"
      endpoint = f"http://localhost:8000/{url}"
    else:
      endpoint = f"http://localhost:8000/{args['views'][req[0]]['url']}/"

    if len(req) > 2 and req[2]:
      data = json.loads(req[2])
    else:
      data = args['views'][req[0]]['json']

    if 'Authorization' not in args['views'][req[0]]['auth']:
      get_response = requests.put(endpoint, json=data) 
    else:
      auth_endpoint = f"http://localhost:8000/{args['views'][req[0]]['auth']['url']}/"
      username = input('User Name: ')
      password = getpass()

      auth_response = requests.post(
        auth_endpoint, 
        json={'username': username, 'password': password}
      ) 

      if auth_response.status_code == 200:
        token = auth_response.json()['token']
        headers = {
          "Authorization": f"{args['views'][req[0]]['auth']['Authorization']} {token}"
        }
        get_response = requests.delete(endpoint, json=data, headers=headers) 

    print(get_response.json())
    confirm = input("Do you want to try another (Y/N) (H)elp: ").lower()
    if confirm not in ['h', 'y']:
      repeat = False
    elif confirm == 'h':
      show = True
  elif req[0] == '':
    repeat = False
  else:
    print('Invalid Input!')