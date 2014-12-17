from pyramid.config import Configurator
from pyramid.wsgi import wsgiapp2

from switchboard import configure


def request_tween_factory(handler, registry):

    def request_tween(request):
        from switchboard import operator
        operator.get_request = lambda: request
        return handler(request)

    return request_tween


def includeme(config):
    """ Activate the switchboard; usually called via
    ``config.include('pyramid_switchboard')`` instead of being invoked
    directly. """
    settings = config.registry.settings
    # By setting nested to True, we're only looking for switchboard.* settings.
    configure(settings, nested=True)

    # Setup the tween for injecting the request into Switchboard's context.
    config.add_tween('pyramid_switchboard.request_tween_factory')

    # Create the new application using the updated settings.
    application = make_application(settings, config.registry)
    config.add_route('switchboard', '/_switchboard/*subpath')
    permission = settings.get('switchboard.permission', 'admin')
    config.add_view(wsgiapp2(application), route_name='switchboard',
                    permission=permission)


def make_application(settings, parent_registry):
    """ WSGI application for rendering the switchboard admin."""
    config = Configurator(settings=settings)
    # Setup routes and views.
    config.registry.parent_registry = parent_registry
    config.add_route('switchboard.main', '/')
    config.add_route('switchboard.add', '/add')
    config.add_route('switchboard.update', '/update')
    config.add_route('switchboard.status', '/status')
    config.add_route('switchboard.delete', '/delete')
    config.add_route('switchboard.add_condition', '/add_condition')
    config.add_route('switchboard.remove_condition', '/remove_condition')
    config.add_route('switchboard.history', '/history')
    config.include('pyramid_mako')
    config.scan('pyramid_switchboard.views')
    return config.make_wsgi_app()
