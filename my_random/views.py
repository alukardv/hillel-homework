from django.http import HttpResponse
from django.shortcuts import render
from random import randint

menu = {'about/whoami': ' Whoami', 'about/source_code': 'Source code', 'my_random': 'Random'}


def my_first_view(request):
    result: str = 'Error: length out of range'
    try:
        length: int = int(request.GET.get('length', 0))
    except ValueError:
        length = 0
        result: str = 'Error Value'
    except Exception:
        length = 0
    try:
        if request.GET.getlist('specials') == 'on':
            specials: int = 0
        else:
            specials: int = 1
    except Exception:
        specials = 0
    try:
        if request.GET.getlist('digits') == 'on':
            digits: int = 0
        else:
            digits: int = 1
    except Exception:
        digits = 0

    if 0 < length <= 100:

        english_letters: str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        spec: str = '!"№;%:?*()_+'
        num: str = '0123456789'
        pool_for_random = english_letters
        result = ''

        if specials == 1:
            pool_for_random += spec

        if digits == 1:
            pool_for_random += num

        for i in range(length):
            result += pool_for_random[randint(0, len(pool_for_random) - 1)]
    return render(request, 'my_random/random.html', {'menu': menu, 'title': 'Random', 'result': result})
