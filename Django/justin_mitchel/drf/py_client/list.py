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
  req = input('Please enter the number from one of the options: ').split(' ', 1)
  if req[0] != '' and int(req[0]) in arr:
    endpoint = f"http://localhost:8000/{args['views'][req[0]]['url']}/"
    
    if 'GET' in args['views'][req[0]]['methods'] and \
        'Authorization' not in args['views'][req[0]]['auth']:
      get_response = requests.get(endpoint) 
      print(get_response.json())
    elif 'Authorization' not in args['views'][req[0]]['auth']:
      post_response = requests.post(endpoint) 
      print(post_response.json())
    else:
      auth_endpoint = f"http://localhost:8000/{args['views'][req[0]]['auth']['url']}/"
      username = input('User Name: ')
      password = getpass()

      auth_response = requests.post(
        auth_endpoint, 
        json={'username': username, 'password': password}
      ) 
      # print(auth_response.json())

      if auth_response.status_code == 200:
        token = auth_response.json()['token']
        headers = {
          "Authorization": f"{args['views'][req[0]]['auth']['Authorization']} {token}"
        }

        get_response = requests.get(endpoint, headers=headers) 
        print(get_response.json())
        data = get_response.json()
        next_url = data['next']
        print('next_url', next_url)
        move_next = 'next' in data
        while move_next:
          if next_url is not None:
            move_next = input('Do you want to view the next page of results (Y/N)? ').lower() == 'y'
            if move_next:
              get_response = requests.get(next_url, headers=headers)
              data = get_response.json()
              next_url = data['next']
              print('next_url', next_url)
              results = data['results']
              print(results)
              print()
          else:
            move_next = False

    confirm = input("Do you want to try another (Y/N) (H)elp: ").lower()
    if confirm not in ['h', 'y']:
      repeat = False
    elif confirm == 'h':
      show = True
  elif req[0] == '':
    repeat = False
  else:
    print(f"")
    print('Invalid Input!')