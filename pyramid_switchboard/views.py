from pyramid.view import view_config

from switchboard.admin.controllers import CoreAdminController

class SwitchboardAdminView(object):
    def __init__(self, request):
        self.request = request
        self.params = request.params
        self.c = CoreAdminController()

    @view_config(
        route_name='switchboard.main',
        renderer='switchboard:admin/templates/index.mak',
    )
    def index(self):
        return self.c.index(**self.params)

    @view_config(
        route_name='switchboard.add',
        renderer='json',
    )
    def add(self):
        return self.c.add(**self.params)

    @view_config(
        route_name='switchboard.update',
        renderer='json',
    )
    def update(self):
        return self.c.update(**self.params)

    @view_config(
        route_name='switchboard.status',
        renderer='json',
    )
    def status(self):
        return self.c.status(**self.params)

    @view_config(
        route_name='switchboard.delete',
        renderer='json',
    )
    def delete(self):
        return self.c.delete(**self.params)

    @view_config(
        route_name='switchboard.add_condition',
        renderer='json',
    )
    def add_condition(self):
        return self.c.add_condition(**self.params)

    @view_config(
        route_name='switchboard.remove_condition',
        renderer='json',
    )
    def remove_condition(self):
        return self.c.remove_condition(**self.params)

    @view_config(
        route_name='switchboard.history',
        renderer='json',
    )
    def history(self):
        return self.c.history(**self.params)
