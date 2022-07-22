from aiogram import Bot, Dispatcher, executor, types
import requests
from bs4 import BeautifulSoup


bot = Bot(token="5534683493:AAE8hJ1dZhWWzr8aIN5sd7ZV01PecYIFeDE")
dp = Dispatcher(bot)
url = 'https://app.astrodao.com/dao/human.sputnik-dao.near/proposals/human.sputnik-dao.near-155'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

soup = str(soup)

index = soup.find('"voteYes')
yesnotext = soup[index:index+22]

yes_amount = int(yesnotext[10])
no_amount = int(yesnotext[21])

@dp.message_handler(commands=['start', 'rating'])
async def start_handler(message: types.Message):
    if message.text[:6] == "/start":
        await bot.send_message(message.from_user.id,
                               "🤙 yes votes {}\n"
                               "🤢 no votes {}".format(yes_amount, no_amount))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
