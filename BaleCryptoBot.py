import requests
from bale import Bot, Message

get_token = input("Enter your token : ")
bale_bot = Bot(token=get_token)



@bale_bot.event
async def on_message(message : Message):
    response = requests.get('https://api.abantether.com/api/v1/manager/otc/ticker')
    if response.status_code == 200:
        js = response.json()
        symbol = message.content
        try : 
            if symbol.islower() or symbol[-1] != "T":
                symbol = symbol.upper() + "IRT" 
            result = js["data"]["markets"][symbol]["buy_price"]
            await message.reply("نرخ لحظه ای : " + result)
        except KeyError:
            await message.reply("ارز مورد نظر یافت نشد! لطفا ارز مورد نظر رو به انگلیسی و دقیق انتخاب کنید.")
    else:
        await message.reply("سرور به ارور برخورده!")

bale_bot.run()

