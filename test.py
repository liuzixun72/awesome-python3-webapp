from orm import Model, StringField, IntegerField
import asyncio

class User(Model):
    __table__ = "users"
    id = IntegerField(primary_key = True)

@asyncio.coroutine
def runTest():
    user = User(id = 123, name = "王大锤")
    yield from user.save()
    yield from user.findAll("王大锤")
    print(user)

runTest()