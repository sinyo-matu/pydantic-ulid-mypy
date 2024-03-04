from pydantic import BaseModel
from pydantic_extra_types.ulid import ULID


class Something(BaseModel):
    id: ULID
