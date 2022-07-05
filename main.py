import os
from discord.ext import commands

token = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix="-")


@bot.event
async def on_ready():
    print(f"-----{bot.user.name} is logged in-----")


def load_ext(command):
    print(command)
    for file in os.listdir(f'./cogs/{command}'):
        if file.endswith(".py"):
            extension = file[:-3]
            print(extension)
            try:
                bot.load_extension(f"cogs.{command}.{extension}")
                print(f"-----Extension {extension} is loaded-----")


            except Exception as e:

                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")


if __name__ == "__main__":
    load_ext("command")

bot.run(token)
