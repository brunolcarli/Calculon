import graphene
from evaluator.types import DynamicScalar



class Query(object):
    _eval = DynamicScalar(
        description='Runs python eval bultin-function ',
        entry=graphene.String(required=True),
        globals=DynamicScalar(),
        locals=DynamicScalar()
    )

    def resolve__eval(self, info, **kwargs):
        return eval(
            kwargs.get('entry'),
            kwargs.get('globals', {}),
            kwargs.get('locals', {})
        )
