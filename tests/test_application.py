from pydantic_ulid_mypy.application import code_use_something_id
from pydantic_ulid_mypy.models import Something


def test_application():
    data = {
        "id": "01BTGNYV6HRNK8K8VKZASZCFPE"
    }
    something = Something.model_validate(data)
    code_use_something_id(something.id)