import graphene
from evaluator.types import DynamicScalar



class Query(object):
    _eval = DynamicScalar(
        description='Runs python eval bultin-function ',
        code=graphene.String(required=True),
        globals=DynamicScalar(),
        locals=DynamicScalar()
    )

    def resolve__eval(self, info, **kwargs):
        return eval(
            kwargs.get('code'),
            kwargs.get('globals', {}),
            kwargs.get('locals', {})
        )
