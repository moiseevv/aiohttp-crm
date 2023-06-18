from optparse import Option
from typing import Optional

from aiohttp.web import Application, run_app, View, Request

from app.store import setup_accessor
from app.store.crm.accessor import CrmAccessor
from app.web.middlewares import setup_middlewares
from app.web.routes import setup_routes
from aiohttp_apispec import setup_aiohttp_apispec


class Application_item(Application):
    config = None
    database: dict = {}
    crm_accessor = None


class Request_item(Request):
    @property
    def app(self) -> Application_item:
        return super().app()


class View_item(View):
    @property
    def request(self) -> Request_item:
        return super().request


app = Application_item()



def run():
    setup_routes(app)
    setup_aiohttp_apispec(app, title='CRM приложение', url='/docs/json', swagger_path='/docs')
    setup_middlewares(app)
    setup_accessor(app)
    run_app(app)
