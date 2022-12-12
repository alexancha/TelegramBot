import aioschedule
import asyncio
from utils import update_data
from utils import two_coins_schedule


async def scheduler():
    aioschedule.every().day.at("08:00").do(update_data)
    aioschedule.every().week.do(two_coins_schedule)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
