import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID
from starlette.applications import Starlette
from starlette.config import Config
from starlette.routing import Route
from starlette.responses import JSONResponse
from starlette.graphql import GraphQLApp
from graphene import Schema, ObjectType, List, String, ID, Field


# Configuration from environment variables or '.env' file.
config = Config('.env')
DATABASE_URL = config('DATABASE_URL')


# Database table definitions.
metadata = sqlalchemy.MetaData()

tbl_users = sqlalchemy.Table(
    "tbl_users",
    metadata,
    sqlalchemy.Column("id", UUID(as_uuid=False), primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String(50)),
    sqlalchemy.Column("first_name", sqlalchemy.String(50)),
    sqlalchemy.Column("last_name", sqlalchemy.String(50)),
)

engine = sqlalchemy.create_engine(DATABASE_URL)
dbConn = engine.connect()


def db_users():
    rows = dbConn.execute("select * from tbl_users")
    content = [
        {
            "id": str(row["id"]),
            "username": row["username"],
            "first_name": row["first_name"],
            "last_name": row["last_name"],
        }
        for row in rows
    ]
    return content


def user_row_to_type(row):
    return UserType(
        id=row["id"],
        username=row["username"],
        first_name=row["first_name"],
        last_name=row["last_name"],
    )

async def api_list_users(request):
    content = db_users()
    return JSONResponse(content)



# graphql entity type
class UserType(ObjectType):
    id = ID(required=True)
    username = String(required=True)
    first_name = String(required=True)
    last_name = String(required=True)

    def resolve_full_name(parent, info):
        return f"{parent.first_name} {parent.last_name}"

# end class


class Query(ObjectType):
    hello = String(name=String(default_value="stranger"))
    users = List(UserType)
    me = Field(UserType)

    def resolve_hello(self, info, name):
        return "Hello " + name

    def resolve_users(self, info):
        rows = db_users()
        users = [user_row_to_type(row) for row in rows]
        return users

    def resolve_me(parent, info):
        # returns an object that represents a Person
        return UserType(first_name="John", last_name="Smith")

# end class


schema = Schema(query=Query, auto_camelcase=False)

routes = [
    Route("/users", endpoint=api_list_users, methods=["GET"]),
    Route('/', GraphQLApp(schema)),
]

app = Starlette(routes=routes)
