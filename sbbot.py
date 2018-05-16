import discord, datetime, random, time
from discord.ext import commands

random.seed(time.monotonic())

def num_dp(a, b):
    return (float(int(a*(10.**b)))/(10.**b))

def get_q(cat):
    r=open('allsbq.txt', 'r')
    lines = r.readlines()
    r.close()
    cats=[["bio", "BIOLOGY"], 
    ["phys", "PHYSICS"],
    ["chem", "CHEMISTRY"],
    ["math", "MATH"],
    ["astro", "ASTRONOMY"],
    ["gen", "GENERAL"],
    ["earth", "EARTH"]]
    proo=""
    for lol in cats:
        if lol[0]==cat:
            proo=lol[1]
    if cat=="":
        proo=random.choice(cats)[1]
    main=[]
    if True:
        i = random.randint(1,2001)
        j=b=0
        while b==0:
            t=len(lines)
            for k in range(0, t):
                line=lines[k]
                if len(line.split())>1 and line.split()[1]==proo:
                    if j==i:
                        temp=""
                        i=0
                        c=0
                        while c==0:
                            if len(lines[k+i].split())>0:
                                if lines[k+i].split()[0] not in ["ANSWER:", "TOSS-UP", "BONUS"]:
                                    temp+=lines[k+i]
                                else: 
                                    if lines[k+i].split()[0]=="ANSWER:":
                                        main.append(lines[k+i])
                                    c=1
                            i=i+1
                        main.append(temp)
                        return list(reversed(main))
                        b=1
                        break
                    else: 
                        j=j+1
    else: return "haha"

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(datetime.datetime.now().strftime("%H:%M:%S"))
    print('------')
    await bot.change_presence(game=discord.Game(name="Science Bowl", type=0))
    w=open('temp.txt', 'w')
    w.close()

@bot.command(pass_context=True)
async def q(ctx):
    cat=ctx.message.content[3:]
    if cat=="h":
        embed = discord.Embed(title="Categories:", color=0xeee657)
        embed.add_field(name="math", value="math")
        embed.add_field(name="bio", value="bio")
        embed.add_field(name="chem", value="chem")
        embed.add_field(name="Anything else: random subject.", value="random")
        await ctx.send(embed=embed)
    else:
        answer=""
        pro = get_q(cat)
        await bot.say(pro[0].replace("Ő", "'").replace("L'", " degrees"))
        if len(pro)==2:
            w=open('temp.txt', 'w')
            w.write(pro[1])
            w.write(str(time.monotonic()))
            w.close()
        else:
            w=open('temp.txt', 'w')
            w.write("No answer available.")
            w.write(str(time.monotonic()))
            w.close()

#@bot.command(pass_context=True)
#async def r(ctx):
#    if "aryjordanicus#5322" in str(ctx.message.author):
#        os.execv(sys.executable, ['python'] + sys.argv)
#    else: await bot.say("Request denied.")


@bot.command()
async def a():
    r=open('temp.txt', 'r')
    t = r.readlines()
    r.close()
    if t!=[]:
        await bot.say(t[0])
        if num_dp(time.monotonic()-float(t[1]), 2)>40:
            await bot.say("Probably too late.")
        else:
            await bot.say("Time elapsed: "+str(num_dp(time.monotonic()-float(t[1]), 2)))
    else:
        await bot.say("Previous question not found.")

@bot.command(pass_context=True)
async def hi(ctx):
    await bot.say(":smiley: :wave: Hello, "+ctx.message.author.mention+"!")

@bot.command()
async def cat():
    await bot.say("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@bot.command()
async def h():
    embed = discord.Embed(title="Science Bowl Bot.", color=0xeee657)

    embed.add_field(name="!q [category]", value="Gives question in specified category (if field left blank, then picks random category)", inline=False)
    embed.add_field(name="Categories:", value="bio, math, phys, chem, earth, astro, gen", inline=False)
    embed.add_field(name="!a", value="Gives answer to previously asked question.", inline=False)
    embed.add_field(name="!hi", value="Greets you.", inline=False)
    embed.add_field(name="!cat", value="Cat gif.", inline=False)
    #embed.add_field(name="!r", value="Restarts the bot. [only accessible to admins]", inline=False)
    embed.add_field(name="!h", value="This page.", inline=False)

    await bot.say(embed=embed)

<<<<<<< HEAD
r=open('.config', 'r')
=======
r=open('config.txt', 'r')
>>>>>>> 4df113b7b928a06e6fd1ff60eb543dd72ded1f50
l=r.readlines()
TOKEN=l[0]
r.close()
bot.run(TOKEN)
