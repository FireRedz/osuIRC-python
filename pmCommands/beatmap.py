from utils import osuApi

async def run(client,message,user):
    try:
        tempMsg = message.split()[1]
    except:
        await client.sendPM(user, 'Give me beatmap id >:)')

    '''
        todo
        
        * add error handler on osuApi.getBeatmap
        * add ripple api (not rly used, but might be useful in the future)
        * add osu api
        * finish this function
        * its a mirror command ok
    '''