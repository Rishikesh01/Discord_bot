import orm
from core.model.RepBotDB import BotTable

'''
Basic CURD operations for bot 
'''


async def createUser(user: str, RepPoints: int):
    await BotTable().objects.create(userName=user, points=RepPoints)


async def updateUser(user: str, RepPoints: int):
    get_row = await BotTable().objects.get(userName=user)
    await get_row.update(points=get_row.points + RepPoints)


async def findUser(user: str):
    try:
        await BotTable().objects.get(userName=user)
    except orm.exceptions.NoMatch:
        return 1


async def checkingUser(user: str, repPoints: int):
    if (await findUser(user)) != 1:
        await updateUser(user, repPoints)
    else:
        await createUser(user, repPoints)
