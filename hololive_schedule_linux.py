#!/usr/bin/env python

# Required additional packages:
# 1. bs4 (html analyse)
# 2. requests (get webpage)

from bs4 import BeautifulSoup
import requests as req
import re
from requests.cookies import RequestsCookieJar
import os
import time
import datetime

start = time.time()


# English name of the members
en_name = {
    'ホロライブ': 'Hololive',
    'ときのそら': 'Tokino Sora',
    'ロボ子さん': 'Roboco',
    'さくらみこ': 'Sakura Miko',
    '星街すいせい': 'Hoshimachi Suisei',
    '夜空メル': 'Yozora Mel',
    '夏色まつり': 'Natsuiro Matsuri',
    '赤井はあと': 'Akai Haato',
    'アキロゼ': 'Aki Rosenthal',
    '白上フブキ': 'Shirakami Fubuki',
    '湊あくあ': 'Minato Aqua',
    '紫咲シオン': 'Murasaki Shion',
    '百鬼あやめ': 'Nakiri Ayame',
    '癒月ちょこ': 'Yuzuki Choco',
    '大空スバル': 'Oozora Subaru',
    '大神ミオ': 'Ookami Mio',
    '猫又おかゆ': 'Nekomata Okayu',
    '戌神ころね': 'Inugami Korone',
    '兎田ぺこら': 'Usada Pekora',
    '潤羽るしあ': 'Uruha Rushia',
    '不知火フレア': 'Shiranui Flare',
    '白銀ノエル': 'Shirogane Noel',
    '宝鐘マリン': 'Houshou Marine',
    '天音かなた': 'Amane Kanata',
    '桐生ココ': 'Kiryu Coco',
    '角巻わため': 'Tsunomaki Watame',
    '常闇トワ': 'Tokoyami Towa',
    '姫森ルーナ': 'Himemori Luna',
    'AZKi': 'AZKi',
    'Risu': 'Ayunda Risu',
    'Moona': 'Moona Hoshinova',
    'Iofi': 'Airani Iofifteen',
    '夕刻ロベル': 'Yukoku Roberu',
    '奏手イヅル': 'Kanade Izuru',
    '月下カオル': 'Tsukishita Kaoru',
    '花咲みやび': 'Hanasaki Miyabi',
    '鏡見キラ': 'Kagami Kira',
    'アルランディス': 'Arurandeisu',
    '律可': 'Rikka',
    'アステル・レダ': 'Astel Leda',
    '岸堂天真': 'Kishido Temma',
    '影山シエン': 'Kageyama Shien',
    '荒咬オウガ': 'Aragami Oga',
    'ホロスターズ': 'Holostars',
    '雪花ラミィ': 'Yukihana Lamy',
    '獅白ぼたん': 'Shishiro Botan',
    '尾丸ポルカ': 'Omaru Polka',
    '桃鈴ねね': 'Momosuzu Nene',
    '魔乃アロエ': 'Mano Aloe',
    'Ina': "Ninomae Ina'nis",
    'Gura': 'Gawr Gura',
    'Amelia': 'Watson Amelia',
    'Calli': 'Mori Calliope',
    'Kiara': 'Takanashi Kiara'
}


# Emoji of the members
emoji = {
    'ときのそら': '',
    'ロボ子さん': '🤖',
    'さくらみこ': '💮',
    '星街すいせい': '☄️',
    '夜空メル': '🌟',
    '夏色まつり': '🏮',
    '赤井はあと': '❤️',
    'アキロゼ': '🍎',
    '白上フブキ': '🌽',
    '湊あくあ': '⚓️',
    '紫咲シオン': '🌙',
    '百鬼あやめ': '😈',
    '癒月ちょこ': '🍫💋',
    '大空スバル': '🚑',
    '大神ミオ': '🌲',
    '猫又おかゆ': '🍙',
    '戌神ころね': '🥐',
    '兎田ぺこら': '👯',
    '潤羽るしあ': '🦋',
    '不知火フレア': '🔥',
    '白銀ノエル': '⚔',
    '宝鐘マリン': '🏴‍☠️',
    '天音かなた': '💫',
    '桐生ココ': '🐉',
    '角巻わため': '🐏',
    '常闇トワ': '👾',
    '姫森ルーナ': '🍬',
    'AZKi': '🎤',
    'Risu': '🐿',
    'Moona': '🔮',
    'Iofi': '🎨',
    '夕刻ロベル': '🍷',
    '奏手イヅル': '🎸',
    '月下カオル': '💅',
    '花咲みやび': '🌺',
    '鏡見キラ': '💙',
    'アルランディス': '🍕',
    '律可': '⚙',
    'アステル・レダ': '🎭',
    '岸堂天真': '🦔💨',
    '影山シエン': '🟣',
    '荒咬オウガ': '🐃',
    'ホロスターズ': '',
    '雪花ラミィ': '☃️',
    '獅白ぼたん': '♌',
    '尾丸ポルカ': '🎪',
    '桃鈴ねね': '🥟',
    '魔乃アロエ': '👅',
    'Ina': '🐙',
    'Gura': '🔱',
    'Amelia': '🔎',
    'Calli': '💀',
    'Kiara': '🐔'
}


# Designed UA header for HTTP-GET request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
}


# Get cookie from domain schedule.hololive.tv
cookie_local = {}
resp = req.get("https://schedule.hololive.tv/lives/all", headers=headers)
cookie_local = resp.cookies
# Set the timezone as UTC in cookie to get schedule in UTC timezone
cookie_local.set("timezone", "UTC", domain="schedule.hololive.tv")


# Get HTML response of the schedule webpage
def get_html():
    resp = req.get("https://schedule.hololive.tv/lives/all",
                   cookies=cookie_local)
    return resp


# Get the nodes contain schedule info
# (The real live schedule is a div tag which class is 'tab-content')
def get_raw_schedule(html):
    soup = BeautifulSoup(html.text, "lxml")
    return soup.find_all(class_="tab-content")


# Traverse all tag nodes and classify them as tags contain date,
# time, VTuber's name and liveroom link, using class-id
def tag_classify(tag):
    if(tag.has_attr("class")):
        class_list = tag['class']
        # Tags contain date strings always with a class-id 'holodule navbar-text'
        if('holodule' in class_list
                and 'navbar-text' in class_list):
            return "date"
        # Tags contain time strings always with a class-id contains 'datetime'
        elif('datetime' in class_list):
            return "time"
        # Tags contain VTuber name always with a class-id contains 'text-right name'
        elif('col' in class_list and 'text-right' in class_list and 'name' in class_list):
            return "name"
        # Tags contain liveroom link always with a class-id contains 'thumbnail'
        elif('thumbnail' in class_list):
            return "link"
        else:
            return "others"
    else:
        return "others"


# Confirm if the VTuber is streaming now
# (The VTubers who are streaming will have a red border around the liveroom info card on the schedule webpage)
def is_streaming(tag):
    if(tag.has_attr("style")):
        style_list = tag['style']
        if('border: 3px red solid' in style_list):
            return True
        else:
            return False
    else:
        return False


# Format the strings from tag nodes
def format_string(string):
    return string.replace("\n", "").replace("\t", "").replace("\r", "").replace("None", "").replace(" ", "")


# Confirm if a VTuber's live is not started
# (The liveroom about to start will have strings contains 'scheduledStartTime' in their webpages)
def is_upcoming(tag):
    start = time.time()
    resp = req.get(tag['href'])
    upcoming_flag = re.search("scheduledStartTime", resp.text)
    if(upcoming_flag != None):
        end = time.time()
        print("module is_upcoming: ")
        print(end-start)
        return True
    else:
        end = time.time()
        print("module is_upcoming: ")
        print(end-start)
        return False


# Auto detect timezone and convert UTC time (on the webpage) to user's loacl time
def utc_2_localtime(utc):
    utc_t = datetime.datetime.strptime(utc, "%m/%d %H:%M")
    local_timestamp = time.time()
    local_time = datetime.datetime.fromtimestamp(local_timestamp)
    utc_time = datetime.datetime.utcfromtimestamp(local_timestamp)
    offset = local_time - utc_time
    local = utc_t + offset
    return (datetime.datetime.strftime(local, "%m/%d %H:%M"))


# Get current time
def get_current_time():
    timestamp = time.time()
    local = datetime.datetime.fromtimestamp(timestamp)
    return (datetime.datetime.strftime(local, "%m/%d %H:%M"))


# Get the tag nodes contain schedule info
raw_schedule = get_raw_schedule(get_html())
# Date status (changed when analyse new date)
date = "date_dummy_string"
schedule = []                                       # Blank schedule list
live = {}                                           # Blank liveroom dictionary
timezone = time.strftime("%z", time.localtime())    # User's timezone


# Analyse tag nodes
for tag in raw_schedule[0].find_all():
    # Tags contain date string detected (like '06/30(日)'), update date value
    if(tag_classify(tag) == "date"):
        date = format_string(tag.string)[0:5]       # Drop week info
    # Tags contain time string detected (like '14:00'),
    # combine date and time as a key in the dictionary
    elif(tag_classify(tag) == "time"):
        for time_string in tag.strings:
            if(time_string.replace("\n", "").replace("\t", "").replace("\r", "").replace("None", "").replace(" ", "") != ""):
                live['time'] = utc_2_localtime(
                    date+" "+format_string(time_string))
                # Streaming time is further than current time,
                # which means the stream is not beginning
                if(live['time'] > get_current_time()):
                    live['status'] = 'upcoming'
    # Tags contain VTuber's name string detected (like 'Risu'),
    # insert the name as a key in the dictionary
    elif(tag_classify(tag) == "name"):
        live['host'] = format_string(tag.string)
    # Tags contain liveroom link detected,
    # get the status of the liveroom (Stream over, Streaming now or Stream will start)
    # and insert different key in the dictionary
    elif(tag_classify(tag) == "link"):
        live['link'] = tag['href']
        if(is_streaming(tag) is True):
            live['status'] = 'streaming'
        else:
            live['status'] = 'over'
    # If all keys of a dictionary is inserted, append it into the schedule list
    if(len(live) == 4):
        schedule.append(live)
        live = {}   # Clear the dictionary for new info


end = time.time()
time_taken = str(end - start)

print(" ")
print("---")
print("---")
print("Streaming now")
print("---")
for stream_live in schedule:
    if(stream_live['status'] == 'streaming'):
        print("🔴 "+en_name.get(str(stream_live['host']), "")+" "
            + " | href=" + stream_live['link'])
print("---")
print("---")
print("Streaming later")
print("---")
for upcoming_live in schedule:
    if(upcoming_live['status'] == 'upcoming'):
        print(upcoming_live['time']+" "
                +en_name.get(str(upcoming_live['host']), "")+" "
                +" | href="+upcoming_live['link'])
    
