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
  req = input('Please enter the number from one of the options: ')
  if req != '' and int(req) in arr:
    url = f"{args['views'][req]['url'][:-1]}190909090" 
    endpoint = f"http://localhost:8000/{url}"

    get_response = requests.get(endpoint) 
    print(get_response.json())
    confirm = input("Do you want to try another (Y/N) (H)elp: ").lower()
    if confirm not in ['h', 'y']:
      repeat = False
    elif confirm == 'h':
      show = True
  elif req == '':
    repeat = False
  else:
    print('Invalid Input!')