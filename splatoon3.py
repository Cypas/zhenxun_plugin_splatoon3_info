import requests
from datetime import datetime, timedelta
from utils.message_builder import image


def get_json(url):
    # requests.get 自带 json.load
    page = requests.get(url)
    page = page.content
    # 将bytes转换成字符串
    page = page.decode('utf-8')
    return page


def UTCTimeToChinaTime(worldTime):
    worldTime = datetime.strptime(worldTime, '%Y-%m-%dT%H:%M:%SZ')
    worldTime = worldTime + timedelta(hours=8)
    ChinaTime = worldTime.strftime("%m.%d %H:%M")
    return ChinaTime


# 涂地模式
def RegularSchedules(data, i):
    data = data['data']['regularSchedules']['nodes'][i]
    startTime = UTCTimeToChinaTime(data['startTime'])
    endTime = UTCTimeToChinaTime(data['endTime'])
    turfData = data['regularMatchSetting']

    mapName1 = turfData['vsStages'][0]['name']
    mapImg1 = turfData['vsStages'][0]['image']['url']
    mapName2 = turfData['vsStages'][1]['name']
    mapImg2 = turfData['vsStages'][1]['image']['url']
    return f'{startTime}-{endTime}\n涂地地图为{mapName1}' + image(mapImg1) + f'{mapName2}' + image(
        mapImg2)


# 真格挑战模式
def BankaraChallengeSchedules(data, i):
    data = data['data']['bankaraSchedules']['nodes'][i]
    startTime = UTCTimeToChinaTime(data['startTime'])
    endTime = UTCTimeToChinaTime(data['endTime'])

    challengeData = data['bankaraMatchSettings'][0]
    challengemode = challengeData['vsRule']['rule']
    challengeMapName1 = challengeData['vsStages'][0]['name']
    challengeMapImg1 = challengeData['vsStages'][0]['image']['url']
    challengeMapName2 = challengeData['vsStages'][1]['name']
    challengeMapImg2 = challengeData['vsStages'][1]['image']['url']

    return (
            f'{startTime}-{endTime}\n真格挑战地图为{challengeMapName1}' + image(
        challengeMapImg1) + f'{challengeMapName2}' + image(challengeMapImg2) + f'\n模式为{challengemode}')


# 真格开放模式
def BankaraOpenSchedules(data, i):
    data = data['data']['bankaraSchedules']['nodes'][i]
    startTime = UTCTimeToChinaTime(data['startTime'])
    endTime = UTCTimeToChinaTime(data['endTime'])

    openData = data['bankaraMatchSettings'][1]
    openmode = openData['vsRule']['rule']
    openMapName1 = openData['vsStages'][0]['name']
    openMapImg1 = openData['vsStages'][0]['image']['url']
    openMapName2 = openData['vsStages'][1]['name']
    openMapImg2 = openData['vsStages'][1]['image']['url']

    return (
            f'{startTime}-{endTime}\n真格开放地图为\n{openMapName1}' + image(
        openMapImg1) + f'和{openMapName2}' + image(openMapImg2) + f'\n模式为{openmode}')


# X模式
def XSchedules(data, i):
    data = data['data']['xSchedules']['nodes'][i]
    startTime = UTCTimeToChinaTime(data['startTime'])
    endTime = UTCTimeToChinaTime(data['endTime'])
    XData = data['xMatchSetting']
    Xmode = XData['vsRule']['rule']
    mapName1 = XData['vsStages'][0]['name']
    mapImg1 = XData['vsStages'][0]['image']['url']
    mapName2 = XData['vsStages'][1]['name']
    mapImg2 = XData['vsStages'][1]['image']['url']
    return f'{startTime}-{endTime}\n涂地地图为{mapName1}{mapImg1}和{mapName2}{mapImg2}，模式为{Xmode}'


# 组排模式
def LeagueSchedules(data, i):
    data = data['data']['leagueSchedules']['nodes'][i]
    startTime = UTCTimeToChinaTime(data['startTime'])
    endTime = UTCTimeToChinaTime(data['endTime'])
    leagueData = data['leagueMatchSetting']
    leagueMode = leagueData['vsRule']['rule']
    mapName1 = leagueData['vsStages'][0]['name']
    mapImg1 = leagueData['vsStages'][0]['image']['url']
    mapName2 = leagueData['vsStages'][1]['name']
    mapImg2 = leagueData['vsStages'][1]['image']['url']
    return f'{startTime}-{endTime}\n组排地图为{mapName1}{mapImg1}和{mapName2}{mapImg2}，模式为{leagueMode}'


# 鲑鱼快跑
def CoopGroupingSchedule(data, i):
    data = data['data']['coopGroupingSchedule']['regularSchedules']['nodes'][i]
    startTime = UTCTimeToChinaTime(data['startTime'])
    endTime = UTCTimeToChinaTime(data['endTime'])
    coopGroupingData = data['setting']

    mapName = coopGroupingData['coopStage']['name']
    mapImg = coopGroupingData['coopStage']['image']['url']
    weaponsData = coopGroupingData['weapons']
    weapon1Name = weaponsData[0]['name']
    weapon1Img = weaponsData[0]['image']['url']
    weapon2Name = weaponsData[1]['name']
    weapon2Img = weaponsData[1]['image']['url']
    weapon3Name = weaponsData[2]['name']
    weapon3Img = weaponsData[2]['image']['url']
    weapon4Name = weaponsData[3]['name']
    weapon4Img = weaponsData[3]['image']['url']

    return (
            f'{startTime}-{endTime}\n打工地图为\n{mapName}' + image(
        mapImg) + f'武器为{weapon1Name}' + image(weapon1Img) + f'{weapon2Name}' + image(
        weapon2Img) + f'{weapon3Name}' + image(weapon3Img) + f'{weapon4Name}' + image(weapon4Img))
