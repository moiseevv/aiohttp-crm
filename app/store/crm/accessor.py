from typing import Optional

from app.crm.models import User


class CrmAccessor:
    def __init__(self):
        self.app = None

    async def connect(self, app):
        self.app = app
        try:
            self.app.database["users"]
        except KeyError:
            self.app.database["users"] = []
        print("connect to database")

    async def disconnect(self, app):
        self.app = None
        print("disconnect from database")

    async def add_user(self, user:User):
        self.app.database['users'].append(user)

    async def list_users(self) -> list[User]:
        return self.app.database['users']

    async def get_user(self, id_):
        for user in self.app.database['users']:
            if user.id_ == id_:
                return user
        return None

