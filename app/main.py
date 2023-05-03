from core.config import get_envs
from core.graph_ql import get_graphql_context
from endpoints.item import item_router
from fastapi import FastAPI
from schemas.graphql import Mutation, Query
from strawberry import Schema
from strawberry.fastapi import GraphQLRouter

env = get_envs()

app = FastAPI(title=env.PROJECT_NAME)

app.include_router(item_router)

schema = Schema(query=Query, mutation=Mutation)
graphql = GraphQLRouter(schema, graphiql=env.DEBUG, context_getter=get_graphql_context)
app.include_router(graphql, prefix="/graphql", include_in_schema=False)
