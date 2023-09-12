from django.http import HttpResponse
from django.apps import apps
from django.conf import settings
from django.urls.resolvers import URLResolver, URLPattern
import inspect
import sys


def get_all_view_names(urlpatterns):
  view_names = []
  view_patterns = {}
  for pattern in urlpatterns:
    if isinstance(pattern, URLResolver):
      get_all_view_names(pattern.url_patterns)
    elif isinstance(pattern, URLPattern):
      view_names.append(pattern.callback.__name__)
      view_patterns[pattern.callback.__name__] = pattern.pattern
  return [view_names, view_patterns]

def listViews(request):
  root_urlconf = __import__(settings.ROOT_URLCONF)
  all_urlpatterns = root_urlconf.urls.urlpatterns
  views_list, urls = get_all_view_names(all_urlpatterns)
  css = ''
  css = open(f'{settings.STATICFILES_DIRS[0]}/css/styles.css', 'r').read()
  show = False
  html = '<head><title>CS Dojo - Tutorials</title>'
  html = f'<style>\n{css}\n</style>'
  html += '</head><pre>'
  for app in apps.get_app_configs():
    views = []
    if show:
      obj = [obj for name, obj in inspect.getmembers(sys.modules[app.verbose_name.lower()])
        if (name == 'views')
      ]
      for line in inspect.getsource(obj[0]).splitlines(True)[1:-1]:
        if line[0:3] == 'def':
          idx = line.index("(")
          views.append(line[4:idx])
      html += f'{app.verbose_name}:\n'
      html += f'\tViews:\n'
      for view in views:
        url = f"{urls[view]}".replace('<', '&lt;').replace('>', '&gt;')
        link = f" <a href={url} target=_blank>/{url}</a>"
        func = f' <span class=smText>(Function: {url})</span>'
        html += f'\t\t{view}'
        html += f'{link}\n' if 'view' in view.lower() else f'{func}\n'
      html += f"\tModels:\n" 
      for model in app.get_models():
        html += f"\t\t{model.__dict__['__doc__']}\n"
        html += f'\tObjects:\n'
        for obj in model.objects.all():
          html += f'\t\t{obj.id}: {obj.content}\n'
    if app.verbose_name == 'Index':
      show = True
  html += '</pre>'
  return HttpResponse(html)
