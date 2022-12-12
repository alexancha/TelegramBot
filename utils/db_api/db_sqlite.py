import requests
import json
from loader import bot
from .models import *
import emoji
import random

with db:
    db.create_tables([Coin, User])


async def update_data():
    r = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_"
                     "page=100&page=1&sparkline=true")
    a = json.loads(r.text)
    with db:
        for i in a:
            exists = Coin.select().where(Coin.symbol == i['symbol'])
            if bool(exists):
                Coin.update(
                    price=i['current_price'],
                    position=i['market_cap_rank'],
                    hiqh_price=i['high_24h'],
                    low_price=i['low_24h'],
                    price_change=i['price_change_24h']
                ).where(Coin.symbol == i['symbol']).execute()
            else:
                Coin.create(
                    name=i['name'].lower(),
                    symbol=i['symbol'],
                    price=i['current_price'],
                    position=i['market_cap_rank'],
                    hiqh_price=i['high_24h'],
                    low_price=i['low_24h'],
                    price_change=i['price_change_24h']
                )


async def user_add(message):
    with db:
        exists = User.select().where(User.user_id == message.from_user.id)
        if not bool(exists):
            User.create(user_id=message.from_user.id)


async def coin_info(message):
    with db:
        if bool(Coin.select().where(Coin.name == message.text.lower())):
            ret = Coin.get(Coin.name == message.text.lower())
            await bot.send_message(message.from_user.id,
                                   f'Имя: {ret.name.title()}\nСимвол: {ret.symbol}\nЦена: {round(ret.price, 6)}$'
                                   f'\nПозиция на маркете: {ret.position}\nСамая высокая цена за сутки: '
                                   f'{round(ret.hiqh_price, 6)}$\nСамая низкая цена за сутки:'
                                   f' {round(ret.low_price, 6)}$\nИзменение цены за сутки:'
                                   f' {round(ret.price_change, 6)}$')
        elif bool(Coin.select().where(Coin.symbol == message.text.lower())):
            ret = Coin.get(Coin.symbol == message.text.lower())
            await bot.send_message(message.from_user.id,
                                   f'Имя: {ret.name.title()}\nСимвол: {ret.symbol}\nЦена: {round(ret.price, 6)}$'
                                   f'\nПозиция на маркете: {ret.position}\nСамая высокая цена за сутки: '
                                   f'{round(ret.hiqh_price, 6)}$\nСамая низкая цена за сутки:'
                                   f' {round(ret.low_price, 6)}$\nИзменение цены за сутки:'
                                   f' {round(ret.price_change, 6)}$')
        else:
            await bot.send_message(message.from_user.id, "Введите корректное название валюты!")


async def top10(message):
    a = []
    with db:
        for top in Coin.select().where(Coin.position <= 10):
            a.append(':TOP_arrow:' + top.name.title())
        await bot.send_message(message.from_user.id, emoji.emojize('\n'.join(a)))


async def two_coins(message):
    coin1 = Coin.get(Coin.position == random.randint(1, 100))
    coin2 = Coin.get(Coin.position == random.randint(1, 100))
    await bot.send_message(message.from_user.id, f'Присмотрись к {coin1.name.title()}\n'
                                 f'Цена: {coin1.price}$\n'
                                 f'Или можешь попробовать {coin2.name.title()}\n'
                                 f'Цена: {coin2.price}$')


async def two_coins_schedule():
    with db:
        for user in User.select():
            coin1 = Coin.get(Coin.position == random.randint(1, 100))
            coin2 = Coin.get(Coin.position == random.randint(1, 100))
            await bot.send_message(user, f'Присмотрись к {coin1.name.title()}\n'
                                                  f'Цена: {coin1.price}$\n'
                                                  f'Или можешь попробовать {coin2.name.title()}\n'
                                                  f'Цена: {coin2.price}$')
