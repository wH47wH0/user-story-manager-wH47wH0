from peewee import *

db = PostgresqlDatabase('postgres', user='miki', password='645464')


class BaseModel(Model):
    class Meta:
        database = db


class UserStoryManager(BaseModel):
    story_title = CharField()
    user_story = TextField()
    acceptance_criteria = TextField()
    business_value = IntegerField()
    estimation = FloatField()
    status = CharField()


def init_db():
    db.connect()
    db.create_tables([UserStoryManager], safe=True)
