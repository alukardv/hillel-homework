class Url:
    """
    Text class URL
    """
    result_url = ''

    def __init__(self, scheme='', authority='', path=None, query=None, fragment=None):
        self.scheme = scheme
        self.authority = authority
        self.path = path
        self.query = query
        self.fragment = fragment

    # def check_scheme(self):
    #     type_scheme = ['ftp', 'http', 'rtmp', 'rtsp', 'https', 'gopher', 'mailto', 'news', 'nntp', 'irc', 'smb',
    #                    'prospero', 'telnet', 'wais', 'xmpp', 'file', 'data', 'tel', 'gopher', 'gopher']
    #     return self.scheme in type_scheme

    def __str__(self):
        if self.path is not None:
            path = '/'
            path += '/'.join(self.path)
        else:
            path = ''

        if self.query is not None:
            query1: str = '?'
            for key, value in self.query.items():
                query1 += f'{str(key)}={str(value)}&'
        else:
            query1 = ''

        if self.fragment is not None:
            fragment = '#'
            fragment += self.fragment
        else:
            fragment = ''

        result = f'{self.scheme}://{self.authority}{path}{query1[:-1]}{fragment}'
        return result

    def __eq__(self, other):
        if self.__str__() == other:
            return True


class HttpsUrl(Url):
    def __init__(self, schema='https', authority='', path=None, query=None, fragment=None):
        super().__init__(schema, authority, path, query, fragment)


class HttpUrl(Url):
    def __init__(self, schema='http', authority='', path=None, query=None, fragment=None):
        super().__init__(schema, authority, path, query, fragment)


class GoogleUrl(Url):
    def __init__(self, schema='https', authority='google.com', path=None, query=None, fragment=None):
        super().__init__(schema, authority, path, query, fragment)


class WikiUrl(Url):
    def __init__(self, schema='https', authority='wikipedia.org', path=None, query=None, fragment=None):
        super().__init__(schema, authority, path, query, fragment)


assert GoogleUrl() == 'https://google.com'
assert GoogleUrl() == HttpsUrl(authority='google.com')
assert GoogleUrl() == Url(scheme='https', authority='google.com')
assert GoogleUrl() == 'https://google.com'
assert WikiUrl() == str(Url(scheme='https', authority='wikipedia.org'))
assert WikiUrl(path=['wiki', 'python']) == 'https://wikipedia.org/wiki/python'
assert GoogleUrl(query={'q': 'python', 'result': 'json'}) == 'https://google.com?q=python&result=json'

print('######################################################')


class UrlCreator():

    def __init__(self, scheme='', authority=''):
        self.scheme = scheme
        self.authority = authority

    def __call__(self, *args, **kwargs):
        def _create():
            args1 = '/'
            args1 += '/'.join(args).replace(',','/')
            result = f'{self.scheme}://{self.authority}{args1}'
            return result
        return _create()

    def __getattr__(self, item):
        return item

    def __eq__(self, other):
        if self.__str__() == other:
            return True


url_creator = UrlCreator(scheme='https', authority='docs.python.org')

assert url_creator('api,v1,list') == 'https://docs.python.org/api/v1/list'

print(url_creator('api,v1,list'))
