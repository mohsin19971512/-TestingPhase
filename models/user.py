from tortoise import fields
from tortoise.models import Model




class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255)

    class Meta:
        table = "users"
