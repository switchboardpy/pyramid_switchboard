# -*- coding: utf-8 -*-
from pyramid.config import Configurator
from pyramid.response import Response
from wsgiref.simple_server import make_server

from switchboard import operator


def main_view(request):
    if operator.is_active('test1', request):
        message = 'The "test1" switch is active'
    else:
        message = 'The "test1" switch is not active'
    return Response(message)


def main():
    config = Configurator()
    config.add_route('main', '/')
    config.add_view(main_view, route_name='main')
    config.include('pyramid_mako')
    config.include('pyramid_switchboard')
    return config.make_wsgi_app()


if __name__ == '__main__':
    app = main()
    server = make_server('0.0.0.0', 8080, app)
    print('******************************************')
    print('Starting server at:')
    print('  http://localhost:8080/')
    print('Switchboard admin is at:')
    print('  http://localhost:8080/_switchboard/')
    print('******************************************')
    server.serve_forever()
