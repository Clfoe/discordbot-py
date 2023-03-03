import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!') # 봇 생성

@client.event
async def on_ready():
    print('봇이 준비되었습니다!')

@client.command()
async def verify(ctx):
    user = ctx.author # 명령어를 실행한 유저
    role = discord.utils.get(user.guild.roles, name='인증 유저') # 역할 이름으로 역할 가져오기
    if role in user.roles: # 이미 인증된 경우
        await ctx.send(f'{user.mention}님은 이미 인증되었습니다.')
    else:
        await ctx.send(f'{user.mention}님, 로블록스 계정을 인증해주세요.')
        await user.send('로블록스 계정 인증 링크: https://www.roblox.com/account/settings/security%27)

@client.event
async def on_message(message):
    if message.content == '인증 완료':
        user = message.author # 인증 완료한 유저
        role = discord.utils.get(user.guild.roles, name='인증된 유저') # 역할 이름으로 역할 가져오기
        await user.add_roles(role) # 역할 추가
        await message.channel.send(f'{user.mention}님, 인증이 완료되었습니다!') # 메시지 보내기

client.run('MTA4MTEzMzc0MDM1NDQ0OTQyMA.GTN_Be.ZfI2BUTLaKNkNNK39AfzZQrTCA94NcqUz9NKJI
') # 봇 토큰 입력
