# BUILT BY 0xJOAT

import discord
from discord.ext import tasks
import yfinance as yf
from datetime import datetime

botToken = ' ' #ENTER YOUR BOT TOKEN INSIDE THE ' '
ethChan = 1 #<REPLACE THE 1 WITH YOUR ETH CHANNEL ID>
btcChan = 1 #<REPLACE THE 1 WITH YOUR BTC CHANNEL ID>

def getEthPrice():
  eth = yf.Ticker('ETH-USD')
  ethinfo = eth.history()
  last_quote = round(ethinfo['Close'].iloc[-1], 2)
  return last_quote

def getBtcPrice():
  btc = yf.Ticker('BTC-USD')
  btcinfo = btc.history()
  last_quote = round(btcinfo['Close'].iloc[-1], 2)
  return last_quote

class MyClient(discord.Client):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

  async def setup_hook(self) -> None:
    self.my_background_task.start()

  async def on_ready(self):
    print(f'Logged in as {self.user} (ID: {self.user.id})')
    print('------')

  @tasks.loop(seconds=605)
  async def my_background_task(self):
    try:
      channel = self.get_channel(ethChan)
      ethpr = str(getEthPrice())
      newname = f'ETH - ${ethpr}'
      print(ethpr)
      await discord.TextChannel.edit(channel, name=newname)

      channel = self.get_channel(btcChan)
      btcpr = str(getBtcPrice())
      newname = f'BTC - ${btcpr}'
      print(btcpr)
      await discord.TextChannel.edit(channel, name=newname)

    except:
      now = datetime.now()
      print(f'except triggered at {now}')

  @my_background_task.before_loop
  async def before_my_task(self):
    await self.wait_until_ready()

client = MyClient(intents=discord.Intents.default())
client.run(botToken)
