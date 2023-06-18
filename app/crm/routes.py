import typing



if typing.TYPE_CHECKING:
    from app.web.app import Application_item


def setup_routes(app):
    from app.crm.views import index, AddUserView
    from app.crm.views import ListUsersView
    from app.crm.views import GetUserView

    app.router.add_get('/index', index)
    app.router.add_view('/add_user', AddUserView)
    app.router.add_view('/list_users', ListUsersView)
    app.router.add_view('/get_user', GetUserView)
