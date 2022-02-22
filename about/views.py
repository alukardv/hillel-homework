from html import escape

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from datetime import datetime

menu = {'about/whoami': ' Whoami', 'about/source_code': 'Source code', 'my_random': 'Random'}



def index(request):
    return render(request, 'about/index.html', {'menu': menu, 'title': 'Home'})


def whoami(request):
    ip_address: str = str(request.META.get('REMOTE_ADDR'))
    user_agent: str = str(request.headers.get('User-Agent'))
    server_time: str = str(datetime.now().strftime('%H:%M:%S'))
    return render(request, 'about/whoami.html', {'menu': menu, 'title': 'Whoami', 'ip_address': ip_address, 'user_agent': user_agent, 'server_time': server_time})


def source_code(request):
    with open(__file__, 'r') as file:
        lines_file = file.readlines()
    source_code_text = escape(''.join(lines_file))
    return render(request, 'about/source_code.html', {'menu': menu, 'title': 'Whoami', 'source_code_text': source_code_text})
