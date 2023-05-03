from fastapi import FastAPI
from strawberry import Schema
from strawberry.fastapi import GraphQLRouter

from core.config import get_envs
from core.database import init
from core.graph_ql import get_graphql_context
from endpoints import author_router, item_router
from schemas.graphql import Mutation, Query

env = get_envs()

app = FastAPI(title=env.PROJECT_NAME)

app.include_router(item_router)
app.include_router(author_router)

schema = Schema(query=Query, mutation=Mutation)
graphql = GraphQLRouter(schema, graphiql=env.DEBUG, context_getter=get_graphql_context)
app.include_router(graphql, prefix="/graphql", include_in_schema=False)

init()
