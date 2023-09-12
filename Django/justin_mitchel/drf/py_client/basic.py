import requests
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
  options += f"URL: {args['views'][str(x)]['url']}, "
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

    if 'GET' in args['views'][req[0]]['methods'] and args['views'][req[0]]['url'] == 'api_01/01':
      get_response = requests.get(endpoint)
    elif 'GET' in args['views'][req[0]]['methods'] and args['views'][req[0]]['url'] == 'api_01/02':
      if len(req) > 1 and req[1]:
        get_response = requests.get(endpoint, json=json.loads(req[1]))
      else:
        get_response = requests.get(
          endpoint, 
          params=args['views'][req[0]]['params'], 
          json=args['views'][req[0]]['json']
        ) # HTTP Request
    elif 'GET' in args['views'][req[0]]['methods'] and args['views'][req[0]]['url'][0:6] in ['api_02', 'api_03', 'api_04', 'api_05']:
      if len(req) > 1 and req[1]:
        get_response = requests.get(endpoint, json=json.loads(req[1]))
      else:
        get_response = requests.get(
          endpoint, 
          json=args['views'][req[0]]['json']
        ) # HTTP Request
    elif 'POST' in args['views'][req[0]]['methods'] and args['views'][req[0]]['url'][0:6] in ['api_03', 'api_05', 'api_06', 'api_07']:
      if len(req) > 1 and req[1]:
        get_response = requests.post(endpoint, json=json.loads(req[1]))
      else:
        get_response = requests.post(
          endpoint, 
          json=args['views'][req[0]]['json']
        ) # HTTP Request

    # print(get_response.headers) # print raw text response
    # print(get_response.text) # print raw text response
    # print(get_response.json()['message']) # print JSON response
    # print(get_response.status_code)
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