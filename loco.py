import discord
import asyncio
 


bot_channel_id = discord.Object(id='557917899881447463')
lo_channel_id_list = [ 
    "557439769106448406",
    "557601050190675973",
    "557439769106448406",
	"557917899881447463"
]

sent_new_message = False
answer_scores = {
    "1": 0,
    "2": 0,
    "3": 0,
}
answer_scores_last = {
    "1": 0,
    "2": 0,
    "3": 0,
}

apgscore = 150
nomarkscore = 80
markscore = 40

bot = discord.Client()
selfbot = discord.Client()
 
@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='Loco Games'))
    print("TRIVIA HUNGAMA")
    print("Connected to discord.")
    print("User: " + bot.user.name)
    print("ID: " + bot.user.id)
     
 

@bot.event
async def on_message(message):
    global sent_new_message
    global answer
    global answer_scores
    global answer_scores_last

    if message.server == None:
        return

    if message.content.lower() == "-lo":
        if "557816918673850369" in [role.id for role in message.author.roles]:
            
            sent_new_message = False
            answer_scores = {
                "1": 0,
                "2": 0,
                "3": 0,
            }
            answer = ""
            
        else:
            await bot.add_reaction(message=message, emoji='❌')

@selfbot.event
async def on_ready():
    print("Trivia Hungama Bot")
    print("======================")
    print("Connected to discord.")
    print("User: " + selfbot.user.name)
    print("ID: " + selfbot.user.id)

@selfbot.event
async def on_message(message):
    global answer_scores
    
    global answer

    if message.server == None:
        return

   
    if message.channel.id in oot_channel_id_list:
        content = message.content.lower().replace(' ', '').replace("'", "")
        if content == "1":
            answer_scores["1"] += nomarkscore
        elif content == "2":
            answer_scores["2"] += nomarkscore
        elif content == "3":
            answer_scores["3"] += nomarkscore
        elif content == "4":
            answer_scores["4"] += nomarkscore
        elif content.startswith("1?") or content.startswith("1apg?"):
            answer_scores["1"] += markscore
        elif content.startswith("2?") or content.startswith("2apg?"):
            answer_scores["2"] += markscore
        elif content.startswith("3?") or content.startswith("3apg?"):
            answer_scores["3"] += markscore
        elif content.startswith("4?") or content.startswith("4apg?"):
            answer_scores["4"] += markscore
        elif content == "1apg":
            answer_scores["1"] += apgscore
        elif content == "2apg":
            answer_scores["2"] += apgscore
        elif content == "3apg":
            answer_scores["3"] += apgscore
        elif content == "4apg":
            answer_scores["4"] += apgscore
        elif content in ["not1", "n1"]:
            answer_scores["1"] -= nomarkscore
        elif content in ["not2", "n2"]:
            answer_scores["2"] -= nomarkscore
        elif content in ["not3", "n3"]:
            answer_scores["3"] -= nomarkscore
        elif content in ["not4", "n4"]:
            answer_scores["4"] -= nomarkscore
        elif content.startswith("not1?") or content.startswith("n1?"):
            answer_scores["1"] -= markscore
        elif content.startswith("not2?") or content.startswith("n2?"):
            answer_scores["2"] -= markscore
        elif content.startswith("not3?") or content.startswith("n3?"):
            answer_scores["3"] -= markscore
        elif content.startswith("not4?") or content.startswith("n4?"):
            answer_scores["4"] -= markscore
        else:
            return

        allanswers = answer_scores.values()
        highest = max(allanswers)
        answer = list(allanswers).index(highest)+1

async def send_embed(client, embed):
    return await client.send_message(bot_channel_id, embed=embed)

async def edit_embed(client, old_embed, new_embed):
    return await client.edit_message(old_embed, embed=new_embed)

async def discord_send():
    global sent_new_message
    global answer
    global answer_scores_last

    await bot.wait_until_ready()
    await asyncio.sleep(3)

    answer_scores_last = {
        "1": 0,
        "2": 0,
        "3": 0,
        }

    answer_message = []
    
    while not bot.is_closed:
	    
        if answer_scores != answer_scores_last:
            if answer:
                one_check = ""
                two_check = ""
                three_check = ""
                if answer == 1:
                    one_check = " :white_check_mark:"
                if answer == 2:
                    two_check = " :white_check_mark:"
                if answer == 3:
                    three_check = " :white_check_mark:"
                if not sent_new_message:
                    embed=discord.Embed(title="TRIVIA HUNGAMA", description="**SEARCH RESULTS FOR LOCO**", color=0xadd8e7 )
                    embed.add_field(name="__**ANSWER 1**__", value=f"{answer_scores['1']}{one_check}", inline=False)
                    embed.add_field(name="__**ANSWER 2**__", value=f"{answer_scores['2']}{two_check}", inline=False)
                    embed.add_field(name="__**ANSWER 3**__", value=f"{answer_scores['3']}{three_check}", inline=False)
                    embed.set_footer(text=f"MADE WITH 💖 BY SHIVAM", icon_url="https://cdn.discordapp.com/attachments/558229870568669195/558229907394527232/JPEG_20190320_013032.jpg")
                     

                    answer_message = await send_embed(bot, embed)
                    sent_new_message = True
                else:
                    embed=discord.Embed(title="TRIVIA HUNGAMA", description="**SEARCH RESULTS FOR LOCO**", color=0xadd8e7 )
                    embed.add_field(name="__**ANSWER 1**__", value=f"{answer_scores['1']}{one_check}", inline=False)
                    embed.add_field(name="__**ANSWER 2**__", value=f"{answer_scores['2']}{two_check}", inline=False)
                    embed.add_field(name="__**ANSWER 3**__", value=f"{answer_scores['3']}{three_check}", inline=False)
                    embed.set_footer(text=f"MADE WITH 💖 BY SHIVAM", icon_url="https://cdn.discordapp.com/attachments/558229870568669195/558229907394527232/JPEG_20190320_013032.jpg")

                    await edit_embed(bot, answer_message, embed)
                answer_scores_last = answer_scores.copy()
                await asyncio.sleep(1.1)
                continue

        answer_scores_last = answer_scores.copy()
        await asyncio.sleep(0.05)

loop = asyncio.get_event_loop()
loop.create_task(bot.start("NTYxMDc2NTg1MzE5NDk3NzI4.D39WbA.1vatvhVuLSCEeIso8SWffZTVLEE"))
loop.create_task(selfbot.start("NDY5NDMyMTAzNDU3NzgzODA5.D0xupw.RmC60gD60hE8vkeLpH9Yt5xb-5A
", bot=False))
loop.create_task(discord_send())
loop.run_forever()