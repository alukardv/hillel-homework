from random import randint
from datetime import datetime
from fastapi import FastAPI, Request
from typing import Optional
from starlette.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory='templates/')


@app.get('/')
async def main(req: Request):
    return templates.TemplateResponse('main.html', context={
        'request': req,
        'active_page': 'main',
        'name_app': 'Homework 15 FastApi App',
        'link': {
            'whoami': '/whoami/',
            'source_code': '/source_code/',
            'random': '/random/?length=42&specials=1&digits=0',
        }
    })


@app.get('/whoami/')
async def whoami(req: Request):
    ip_address: str = str(req.client.host)
    user_agent: str = str(req.headers.get('User-Agent'))
    server_time: str = str(datetime.now().strftime('%Y.%m.%d %H:%M:%S'))
    return templates.TemplateResponse('whoami.html', context={
        'request': req,
        'active_page': 'whoami',
        'user_agent': user_agent,
        'ip_address': ip_address,
        'server_time': server_time,
    })


@app.get('/source_code/')
async def source_code(req: Request):
    with open(__file__, 'r') as fr:
        lines_file = fr.readlines()
    lines_of_code: list = [line.replace('\n', '') for line in lines_file]
    return templates.TemplateResponse('source_code.html', context={
        'request': req,
        'active_page': 'source_code',
        'lines_of_code': lines_of_code,
    })


@app.get('/random/')
async def random(length: Optional[int] = 16, specials: Optional[int] = 0,
                 digits: Optional[int] = 1, req: Request = None):
    english_letters: str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    spec: str = '!"№;%:?*()_+'
    num: str = '0123456789'
    result: str = ''
    if length > 100 or length <= 0:
        length = 16
    if specials != 0:
        specials = 1
        english_letters += spec
    if digits != 0:
        digits = 1
        english_letters += num
    for i in range(length):
        result += english_letters[randint(0, len(english_letters) - 1)]
    return templates.TemplateResponse('random.html', context={
        'request': req,
        'active_page': 'random',
        'length': length,
        'specials': specials,
        'digits': digits,
        'result': result,
    })

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
