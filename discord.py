import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    
    async def on_message(self,message):
        print()
        #
client =MyClient()
client.run('e016e3451e0c37cae5ad74032b5793b61d703ed0ef6c6ad555a7c51ac643518f')
