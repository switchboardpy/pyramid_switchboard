from pyramid.wsgi import wsgiapp2

from switchboard import configure
from switchboard.admin import app
from switchboard.middleware import SwitchboardMiddleware


def includeme(config):
    """ Activate the switchboard; usually called via
    ``config.include('pyramid_switchboard')`` instead of being invoked
    directly. """
    settings = config.registry.settings
    # By setting nested to True, we're only looking for switchboard.* settings.
    configure(settings, nested=True)

    # Create the new application using the updated settings.
    switchboard = SwitchboardMiddleware(app)
    config.add_route('switchboard', '/_switchboard/*subpath')
    permission = settings.get('switchboard.permission', 'admin')
    config.add_view(wsgiapp2(switchboard), route_name='switchboard',
                    permission=permission)
