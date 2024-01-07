import json 
import discord
from discord.ext import commands
from datetime import datetime  # Import datetime module



intents = discord.Intents.all()
case_insensitive = True
bot = commands.Bot(command_prefix='!', intents=intents)


# ping
@bot.command(name='ping')
async def ping(ctx):
    start_time = datetime.now()  
    end_time = datetime.now()  
    latency = (end_time - start_time).microseconds / 1000
    embed = discord.Embed(
        title="Pong!",
        description=(f"{latency}ms"),
        color=0x00ff00
    )
    await ctx.send(embed=embed)
  
#clear
@bot.command(name='clear')
async def clear(ctx, quantidade=None):
    max_messages = 100
    if quantidade == 'all':
        await ctx.channel.purge(limit=None)
        await ctx.send("Todas as mensagens foram excluídas com sucesso!")
    else:
        try:
            quantidade = int(quantidade)
            if quantidade > max_messages:
                quantidade = max_messages
        except (TypeError, ValueError):
            quantidade = max_messages

        await ctx.channel.purge(limit=quantidade)
        await ctx.send(f"{quantidade} mensagens foram excluídas com sucesso!")


@bot.command(name="add")
async def add_todo(ctx, *, task: str):
          try:
              with open("afz.json", "r") as file:
                  todos = json.load(file)
          except (json.JSONDecodeError, FileNotFoundError):
              todos = []

          todos.append(task)

          with open("afz.json", "w") as file:
              json.dump(todos, file)

          await ctx.send(f'Tarefa "{task}" adicionada à lista de afazeres.')

@bot.command(name="remover")
async def remove_todo(ctx, index: int):
          try:
              with open("afz.json", "r") as file:
                  todos = json.load(file)
          except (json.JSONDecodeError, FileNotFoundError):
              todos = []

          if 1 <= index <= len(todos):
              removed_task = todos.pop(index - 1)
              with open("afz.json", "w") as file:
                  json.dump(todos, file)
              await ctx.send(f'Tarefa "{removed_task}" removida da lista de afazeres.')
          else:
              await ctx.send("Índice inválido. Use `!list` para ver a lista de afazeres e os índices.")

@bot.command(name="list")
async def list_todos(ctx):
          with open("afz.json", "r") as file:
              todos = json.load(file)
          if todos:
              embed = discord.Embed(title="Lista de Afazeres", color=0x00ff00)
              for index, task in enumerate(todos):
                  embed.add_field(name=f"{index}.", value=task, inline=False)
              await ctx.send(embed=embed)
          else:
              await ctx.send("A lista de afazeres está vazia.")

bot.run('MTE3NTk0NjQ5ODYxMDA0MDk4NA.GQrl8q.umST_-2OS2T7AFXhGb3IMRjBGOod2yz792xhVM')