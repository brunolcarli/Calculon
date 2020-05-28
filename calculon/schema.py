import graphene

import evaluator.schema as evaluator


class Query(evaluator.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
