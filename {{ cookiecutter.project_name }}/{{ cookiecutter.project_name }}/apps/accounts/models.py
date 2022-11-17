from uuid import uuid4

from esmerald.contrib.auth.tortoise.base_user import AbstractUser
from tortoise import fields


class HubUser(AbstractUser):
    uuid = fields.UUIDField(null=False, default=uuid4)
    created_at = fields.DatetimeField(null=False, auto_now_add=True)
    modified_at = fields.DatetimeField(null=False, auto_now=True)

    def __str__(self):
        return self.display_name
