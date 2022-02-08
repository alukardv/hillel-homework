from flask import Flask, request, escape
from datetime import datetime
from random import randint

app = Flask(__name__)


@app.route('/')
def my_main():
    return '<a href="./whoami">whoami</a> <br>'  '<a href="./source_code">source_code</a><br>' '<a href="./random?length=42&specials=1&digits=0">random</a> <br>'


@app.route('/whoami/')
def whoami():
    ip_address: str = str(request.remote_addr)
    user_agent: str = str(request.headers.get('User-Agent'))
    server_time: str = str(datetime.now().strftime('%H:%M:%S'))

    return f'<a href="./..">main</a> <br> Browser client: {user_agent}<br> Ip client:{ip_address}<br> Current time on the server: {server_time}'


@app.route('/source_code/')
def source_code():
    with open('flask_application.py', 'r') as file:
        lines_file = file.readlines()
    source_code_text = escape(''.join(lines_file))

    return f'<a href="./..">main</a> <br> <pre>{source_code_text}</pre>'


@app.route('/random/')
def random():
    result: str = 'Error: length out of range'
    try:
        length: int = int(request.values.get('length', 0))
    except ValueError:
        length = 0
        result: str = 'Error Value'
    except Exception:
        length = 0
    try:
        specials: int = int(request.values.get('specials', 0))
    except Exception:
        specials = 0
    try:
        digits: int = int(request.values.get('digits', 0))
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
            result += pool_for_random[randint(0, len(pool_for_random)-1)]

    return f'<a href="./..">main</a> <br> {result}'


app.run(debug=True, host='0.0.0.0')
