from flask import Flask, request, escape, render_template
from datetime import datetime
from random import randint

app = Flask(__name__)

menu = {'whoami': ' Whoami', 'source_code': 'Source code', 'random':'Random'}

@app.route('/')
def my_main():
    return render_template('index.html', title="Home", menu=menu)

#    '<a href="./whoami">whoami</a> <br>'  '<a href="./source_code">source_code</a><br>' '<a href="./random?length=42&specials=1&digits=0">random</a> <br>'

@app.route('/whoami/')
def whoami():
    ip_address: str = str(request.remote_addr)
    user_agent: str = str(request.headers.get('User-Agent'))
    server_time: str = str(datetime.now().strftime('%H:%M:%S'))
    return render_template('whoami.html', title="Whoami", menu=menu, ip_address=ip_address, user_agent=user_agent, server_time=server_time)


@app.route('/source_code/')
def source_code():
    with open('./flask_application.py', 'r') as file:
        lines_file = file.readlines()
    source_code_text = escape(''.join(lines_file))
    return render_template('source_code.html', title="Source code", menu=menu, source_code_text=source_code_text)


@app.route('/random/', methods=['get', 'post'])
def random():
    result: str = 'Error: length out of range'
    try:
        length: int = int(request.form.get('length', 0))
    except ValueError:
        length = 0
        result: str = 'Error Value'
    except Exception:
        length = 0
    try:
        if request.form.getlist('specials') == 'on':
            specials: int = 0
        else:
            specials: int = 1
    except Exception:
        specials = 0
    try:
        if request.form.getlist('digits') == 'on':
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
            result += pool_for_random[randint(0, len(pool_for_random)-1)]

    return render_template('random.html', title="Random", menu=menu, result=result)


app.run(debug=True, host='0.0.0.0')
