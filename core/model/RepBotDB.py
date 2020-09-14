import databases
import orm
import sqlalchemy


database = databases.Database("sqlite:///RepBotDB.sqlite")
metadata = sqlalchemy.MetaData()


class BotTable(orm.Model):
    __tablename__ = "BotTable"
    __database__ = database
    __metadata__ = metadata
    '''
        id column
        userName column 
        points column
    '''

    id = orm.Integer(primary_key=True)
    userName = orm.String(unique=True, max_length=100)
    points = orm.Integer()


engine = sqlalchemy.create_engine(str(database.url))
metadata.create_all(engine)