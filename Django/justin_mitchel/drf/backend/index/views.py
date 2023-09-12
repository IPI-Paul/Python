import requests
from django.http import HttpResponse
from django.apps import apps
from django.conf import settings
from django.urls.resolvers import URLResolver, URLPattern
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.models import User
import inspect
import sys
import json

# Filters the static file views.json to return only the json objects where the App
# view name matches a urlpattern pattern and the urlpattern name matches the name
# filed in the views.json file. 
def filter_args(args, urls, view, args_filter):
  args_keys = []
  for itm in urls:
    _ = [
      key for key in args if args[key]['name'] == itm['url'] and view == itm['view']
    ]
    if len(_) > 0:
      for x in _: 
        if x not in args_keys:
          args_keys.append(x)
          item = args[x]
          item['view_name'] = view
          args_filter.append(item)
  return args_filter

# Retrives all view names from the urlpatterns pattern and all pattern names from 
# the urlpatterns passed in.
def get_all_view_names(urlpatterns):
  view_names = []
  view_patterns = []
  for pattern in urlpatterns:
    if isinstance(pattern, URLResolver):
      get_all_view_names(pattern.url_patterns)
    elif isinstance(pattern, URLPattern):
      try:
        if pattern.callback.view_class.__name__ not in view_names:
          view_names.append(pattern.callback.view_class.__name__)
        if (pattern.callback.view_class.__name__ != 'view' or len([x for x in view_patterns if x['url'][pattern.name]]) == 0) and \
            pattern.name is not None:
          view_patterns.append({'view': pattern.callback.view_class.__name__, 'url': pattern.name})
      except:
        view_names.append(pattern.callback.__name__)
        if pattern.callback.__name__ != 'view' and pattern.name is not None:
          view_patterns.append({'view': pattern.callback.__name__, 'url': pattern.name})
  return (view_names, view_patterns)

# Retrieves all the links in the detail field of the static file views.json.
def get_details(args_filter, view, detail):
  _ = [
    item['detail'] 
    for item in args_filter if 'detail' in item and item['view_name'] == view
  ]
  if len(_) > 0:
    for x in _: 
      if x not in detail:
        detail.append(x)
  return detail

# Builds the footer tag for the index page. Styling is imported from the static 
# file styles.css.
def get_footer():
  html = '<span>Developed by IPI Paul &copy;</span> &nbsp;'
  html += '<a href="github.com/ipi-paul/" target="_blank">github.com/ipi-paul/</a>'
  return html

# Appends all functions names within each class of App Views.
def get_functions(views, view):
  functions = '<div class=function>'
  for obj in views:
    if isinstance(obj, dict):
      if obj['class'] == view:
        if functions != '<div class=function>':
          functions += ', '
        functions += f'<span>{obj["function"]}</span>'
  functions += '</div>'
  return functions

# Converts object to a string representation of the object.
def get_json(obj, exclude=[]):
  jsobj = '{'
  for item in obj:
    if not item.startswith('_') and not item.startswith('get_') and \
      not item in exclude:
      if jsobj != '{':
        jsobj += ', '
      try:
        jsobj += f'"{item}": ' + (f"null" if obj[item] is None else f"`{obj[item]}`")
      except:
        pass
  jsobj += '}'
  return jsobj

# Retrieves all titles, special notes, urls and descriptions from the static file 
# views.json where the json objects have been collected with the filer_args function.
def get_links(args_filter, view, app):
  url = []
  links = []
  title = ''
  desc = ''
  if len(args_filter) > 0:
    for item in args_filter:
      if item['view_name'] == view:
        url = item['url']
        idx = f" {item['view']}" if 'view' in item else ''
        desc = item['description'] 
        note = item['special_note']
        title = item['title'] 
        if 'load_content' not in item:
          urls = ''
          for method in item['methods']:
            if urls != '':
              urls += ', '
            if method != 'POST':
              urls +=  f"{method}{idx}: <a href={url} target=_blank>/{url}</a> "
            else:
              if 'json' in item:
                jsobj = get_json(item['json'])
                urls += f"{method}{idx}: <a href='#' onClick='postForm(event, {jsobj})'>/{url}</a>"
              else:
                urls += f"{method}: <a href='#' onClick='postForm(event)'>/{url}</a>"
          links.append({
            "title": title,
            "special_note": note,
            "description": desc,
            "url": urls
          })
        elif 'load_content' in item and item['load_content']:
          jsobj = get_json(item['json'], item['exclude_fields'])
          if 'PUT' in item['methods']:
            links.append({
              "title": title,
              "special_note": note,
              "description": desc,
              "url": f"{', '.join(item['methods'])}{idx}: <a href='#' onClick='loadContent(event, {jsobj}, &apos;PUT&apos;)'>/{url}</a>"
            })
          else:
            links.append({
              "title": title,
              "special_note": note,
              "description": desc,
              "url": f"{', '.join(item['methods'])}{idx}: <a href='#' onClick='loadContent(event, {jsobj}, &apos;POST&apos;)'>/{url}</a>"
            })
  return links

# Build the Nav Bar for the index page. Styling is imported from the static 
# file styles.css.
def get_nav_bar(request):
  html = ''
  if f"{request.user}" != 'AnonymousUser':
    html = f'<span>Welcome back {request.user}!</span> &nbsp;'
  else:
    html = '<a href="admin/login" target="_blank">Login</a>'
  return html

# Retrieves all urls from the detail field of static file views.json where the name 
# field matches the Apps urlpattern name.
def get_object_links(obj, detail, css, fields, app_name, args_filter):
  exclude = []
  _, functions = get_view_objects(app_name, 'models')
  for item in functions[1:]:
    if 'function' in item:
      if item['function'] not in exclude:
        exclude.append(item['function'])
    elif item not in exclude:
        exclude.append(item)
  obj.__dict__.pop('_state')
  items = []
  for item in fields:
    if item in list(obj.__dict__.keys()):
      items.append(item)
  for item in items:
    fields.pop(fields.index(item))
  link = '<span class=smText>('
  for url in detail:
    args_excl = [
      x['exclude_fields'] 
      for x in args_filter 
      if len(x['exclude_fields']) > 0 and x['detail'] == url
    ] or []
    if len(args_excl) > 0:
      args_excl = args_excl[0]
    else:
      args_excl = []
    if link != '<span class=smText>(':
      link += ', '
    if '?/delete/' in url or '?/update/' in url:
      location = f"/{url.replace('?', str(obj.id))}"
      if '?/delete/' in url:
        href = f"href='#' onClick='deleteItem(event)'"
      else:
        jsobj = '{'
        for item in obj.__dict__:
          if not item.startswith('_') and not item.startswith('get_') and \
            item not in exclude and item not in args_excl:
            if jsobj != '{':
              jsobj += ', '
            nobj = ''
            _ = [
              x[0]  for x in [
                x['replace'] for x in args_filter 
                if 'replace' in x and x['detail'] == url and app_name in x['name']
              ]
              if len(x) > 0 and item in x[0]
            ]
            if len(_) > 0:
              for x in _:
                if item in x:
                  nobj += f'"{x[item]}": `{obj.__dict__[item]}`'
            jsobj += nobj if nobj != '' else f'"{item}": `{obj.__dict__[item]}`'
          elif item.startswith('get_'):
            if item.startswith('get_')[4:] not in exclude:
              exclude.append(item)
        for item in exclude:
          try:
            fields.pop(fields.index(item))
          except:
            pass
        for field in fields:
          if field not in args_excl:
            if jsobj != '{':
              jsobj += ', '
            jsobj += f'"{field}": ""'
        jsobj += '}'
        href = f"href='#' onClick='updateItem(event, {jsobj}, `{css}`)'"
      link += f"<a {href}>{location}</a>"
    else:
      link += f"<a href={url}{obj.id} target=_blank>/{url}{obj.id}</a>"
  link += ')'
  return link

# Retrieves all Serializer fields for each App.
def get_serializer_fields(app):
  fields = []
  functions = []
  try:
    for name, obj in inspect.getmembers(sys.modules[f'{app}.serializers']):
      if name.lower().endswith('serializer'):
        for item in list(obj.__dict__.keys()):
          if 'get' in item:
            functions.append(item[4:])
  except:
    pass
  try:
    serializers = [
      obj.Meta.fields for name, obj in inspect.getmembers(sys.modules[f'{app}.serializers'])
      if name.lower().endswith('serializer')
    ]
    for serializer in serializers:
      for field in serializer:
        if field not in fields and field != 'pk':
          fields.append(field)
    for function in functions:
      if function in fields:
        fields.pop(fields.index(function))
  except:
    pass
  return fields

# Retrieves all the views object names from each App.
def get_view_objects(app_name, app_type='views'):
  views = []
  try:
    obj = [obj for name, obj in inspect.getmembers(sys.modules[app_name])
      if (name == app_type)
    ]
    class_name = ''
    for line in inspect.getsource(obj[0]).splitlines(True)[1:-1]:
      if 'def ' in line or 'class ' in line:
        start = line.index("def") + 4 if 'def ' in line else line.index("class") + 6
        try:
          idx = line.index("(")
          if not line[start:idx] in views:
            if 'class ' in line:
              class_name = line[start:idx]
            if 'def ' in line and start > 4:
              views.append({
                'class': class_name,
                'function': line[start:idx]
                })
            else:
              views.append(line[start:idx])
        except:
          pass
  except:
    pass
  return (obj, views)

# Generates and displays the index page. Styling is imported from the static 
# file styles.css and JavaScript from the script.js file.
@ensure_csrf_cookie
def ListViews(request):
  css = '/static/css/styles.css'
  js = '/static/js/scripts.js'
  args = json.loads(open(f'{settings.STATICFILES_DIRS[0]}/json/views.json', 'r').read())['views']
  show = False
  html = '<head><title>Coding For Entrepreneurs - Tutorials</title>'
  html += f'<script src={js} defer></script>'
  html += f'<link rel=stylesheet href={css}\n</link>'
  html += f'</head><body class=body>'
  html += f'<nav>{get_nav_bar(request)}</nav>'
  html += '<div class=container>'
  exclude = [
    'Administration', 'Authentication and Authorization', 
    'Content Types', 'Sessions', 'Messages', 'Static Files', 
    'django-cors-headers', 'Django REST framework', 'Auth Token', 
    'Rest_Framework_Simplejwt', 'Index'
  ]
  index = 0
  for app in apps.get_app_configs():
    if app.verbose_name not in exclude:
      symbol, vis = ('-', 'visible') if index >= len([x for x in apps.get_app_configs()]) - 2 \
        else ('+', 'hidden')
      app_name = app.verbose_name.lower()
      try:
        all_urlpatterns = [
          obj for name, obj in inspect.getmembers(sys.modules[f'{app.name}.urls']) 
          if name == 'urlpatterns'
        ][0]
        views_list, urls = get_all_view_names(all_urlpatterns)
        obj, views = get_view_objects(app_name)
        fields = get_serializer_fields(app.name)
        html += f'<div class=app-name name={app.verbose_name}>'
        html += f'<h3 class=expand onClick="toggleView(event)">{symbol}</h3>'
        html += f'<h3 id={app.verbose_name} onClick="toggleView(event)">'
        html += f'{app.verbose_name}:</h3></div>'
        html += f'<div class={vis}><span class=views>Views:</span><br>'
        detail = []
        args_filter = []
        for view in views_list:
          desc = ''
          args_filter = filter_args(args, urls, view, args_filter)
          detail = get_details(args_filter, view, detail)
          links = get_links(args_filter, view, app)
          func = get_functions(views, view)
          html += f'<span class=view>{view}</span>'
          if func != '<div class=function></div>':
            html += f'<span class=functions>Functions: </span><br>{func}'
          for link in links:
            html += f'<span class=api-link>{link["url"]}</span><br>' 
            html += f'<h4>{link["title"]}</h4><br>'
            html += f'<span class=desc>{link["description"]}</span><br>'
            if link["special_note"] != '':
              html += f'<span class=note>{link["special_note"]}</span><br>'
        if len([x for x in app.get_models()]) > 0:
          html += f"<span class=models>Models:</span><br>" 
        for model in app.get_models():
          html += f"<span class=model>{model.__dict__['__doc__']}</span>"
          if len([x for x in model.objects.all()]) > 0:
            html += f'<span class=objects>Objects:</span><br>'
          for obj in model.objects.all():
            link = get_object_links(obj, detail, css, fields, app.name, args_filter)
            user_name = ''
            if 'user_id' in obj.__dict__ and obj.user_id is not None:
              user_name = f' ({User.objects.get(pk=obj.user_id)})'  
            html += f'<div class=object><span>{obj.id}{user_name}: {obj.title}</span>{link}</div><br>'
        html += '</div><br>'
      except:
        pass
    index += 1
  args_filter = filter_args(args, [
      {'view': 'javascipt_client', 'url': 'javascipt_client'}
    ], 'javascipt_client', [])
  links = get_links(args_filter, 'javascipt_client', app)
  html += '<div class=app-name name=jsclient>'
  html += '<h3 class=expand onClick="toggleView(event)">-</h3>'
  html += '<h3 id=jsclient onClick="toggleView(event)">'
  html += 'Login via Javascript Client:</h3></div>'
  html += '<div class=visible><span class=views>Views:</span><br>'
  for link in links:
    html += f'<span class=api-link>{link["url"]}</span><br>' 
    html += f'<h4>{link["title"]}</h4><br>'
    html += f'<span class=desc>{link["description"]}</span><br>'
    if link["special_note"] != '':
      html += f'<span class=note>{link["special_note"]}</span><br>'
  html += '</div>'
  html += f'</div><footer>{get_footer()}</footer></body>'
  return HttpResponse(html)
