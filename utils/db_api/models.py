from peewee import *

db = SqliteDatabase('database.db')


class Coin(Model):
    name = CharField(primary_key=True)
    symbol = CharField()
    price = FloatField()
    position = IntegerField()
    hiqh_price = FloatField()
    low_price = FloatField()
    price_change = FloatField()

    class Meta:
        database = db
        db_table = 'coins'


class User(Model):
    user_id = CharField(primary_key=True)

    class Meta:
        database = db
        db_table = 'users'
