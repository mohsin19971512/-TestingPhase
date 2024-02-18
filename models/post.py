from tortoise import fields
from tortoise.models import Model
from .user import User




class Post(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    content = fields.TextField()
    category = fields.CharField(max_length=255)
    author = fields.ForeignKeyField(f"models.{User.__name__}", related_name='posts')

    class Meta:
        table = "posts"
