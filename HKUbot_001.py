#HUK BOT using telebot module 

from urllib.request import urlopen
from telebot import apihelper
from bs4 import BeautifulSoup
from datetime import datetime  
from datetime import date
import threading
import time
import requests
import random
import math
import colorama
from colorama import Fore
import jellyfish
import random
import logging
import telebot
import random
import re
import sys
import os
from googlesearch import search
from translate import Translator
from googletrans import Translator
import logging
from telebot import apihelper

angry=['angry.webp',
       'black_pepe_angry.tgs'
       ]

wtf=['bobby-wtf.webp',
     'chicken_wtf.tgs',
     'yor_wtf.webp'
     ]

lol=['black_pepe_laugh.tgs',
     'bright_pepe_laugh.tgs',
     'minions_laugh.tgs'
     ]
please='please.webp'

pray='chicken_pray.tgs'

ban=['ninja_ban.webp',
     'ban.webp',
     ]
sad=['minions_cry.tgs',
     'dog_cry.webp'
     ]

foods=['subway',
              'cym',
              'su can',
              'Alfafa',
              'Super sandwich',
              'Cafe330',
              'Coffee academics',
              'Starfuck',
              '齋',
              ' Gourmet Asia',
              'U deli',
              'Swire',
              '學食',
              'Sandwich club',
              '平24',
              '水街',
              '香江冰室',
              '華御結',
              'kebab',
              '幸福 · 駅'
              ]
suicidestr=('[BOT]求助網站和熱線:\n\n香港撒瑪利亞防止自殺會熱線：23892222\n\n醫院管理局精神健康專線：24667350\n\n東華三院芷若園熱線︰18281\n\n撒瑪利亞會熱線︰28960000\n\n社會福利署熱線︰23432255\n\n生命熱線：23820000\n\n利民會《即時通》：35122626\n\n明愛向晴熱線﹕18288\n\n@baldheadADHDninja supports you.\nIn ninja you trust,乜都一定得.')#\n\n<Plz dm ninja if msg is unwanted.\nSorry for any inconvenience caused.>')
numbers=['0',
       '1',
       '2',
       '3',
       '4',
       '5',
       '6',
       '7',
       '8',
       '9'
       ]

small=['q',
       'w',
       'e',
       'r',
       't',
       'y',
       'u',
       'i',
       'o',
       'p',
       'a',
       's',
       'd',
       'f',
       'g',
       'h',
       'j',
       'k',
       'l',
       'z',
       'x',
       'c',
       'v',
       'b',
       'n',
       'm'
       ]
big=['Q',
     'W',
     'E',
     'R',
     'T',
     'Y',
     'U',
     'I',
     'O',
     'P',
     'A',
     'S',
     'D',
     'F',
     'G',
     'H',
     'J',
     'K',
     'L',
     'Z',
     'X',
     'C',
     'V',
     'B',
     'N',
     'M'
     ]

englishwords=alpha=small+big

listofprogram=['BENG',
               'BASC-FINTECH',
               'BENG-BME',
               'BENG-DSE-4',
               'BENG-ENGSC',
               'FAC5T','BBA',
               'BBA-ACCFIN',
               'BBA-BA',
               'BBA-IBGM',
               'BBA-IS',
               'BBA-LAW',
               'BBA-LAWLLB',
               'BECON',
               'BECON-FIN',
               'BFIN-AMPB',
               'BSC-MAT',
               'BSC-QFIN',
               'FACFT',
               'BASC-APPLIEDAI',
               'BEDBSC',
               'BSC',
               'BSCLLB',
               'BSCMRES',
               'BSC-ACTUARSC',
               'FAC2T',
               'BASC-GHD',
               'BBIOMEDSC',
               'BCHINMED',
               'BNURS',
               'BNURS-ALT',
               'BPHARM',
               'BSC-BIOINFORMATICS',
               'BSC-EXERCISEHEALTH',
               'MBBS',
               'FAC4T',
               'BDS',
               'FAC6T',
               'MPHIL',
               'FAC3T',
               'BSOCSC-GOVTLAWSLLB',
               'BSOCSC',
               'BSW',
               'BPSYCH',
               'BJ',
               'BEDBSS',
               'BASC',
               'LLB',
               'FAC8T',
               'BA-ARCHSTUD',
               'BA-CONSERVATION',
               'BA-LS',
               'BA-URBANSTUD',
               'BSC-SURV',
               'FAC9T',
               'BA',
               'BABED-LANGED-CHIN',
               'BABED-LANGED-ENG',
               'BALLB',
               'BA-HDT',
               'FAC1T',
               'BASC-SDS',
               'BED-ECESE',
               'BSC-SPHEARSC',
               'BSC-ACD',
               'BSC-IM']

songlist=[
    'https://youtu.be/ZRtdQ81jPUQ',
    'https://youtu.be/S2mQDtpOFVI',
    'https://youtu.be/hAI-qjw6J-A',
    'https://youtu.be/a51VH9BYzZA',
    'https://youtu.be/1jPyWdBPVfI',
    'https://youtu.be/cTtBqzGI-HM',
    'https://youtu.be/wcbKTNGQaMo',
    'https://youtu.be/LYXkLRLlIck',
    'https://youtu.be/jMsLEGwARXY',
    'https://youtu.be/9lUIuUyOOVg',
    'https://youtu.be/SCDCDKCotng',
    'https://youtu.be/6_GPvvR7YAc',
    'https://youtu.be/LYFciXBcXIQ', 
    'https://youtu.be/pKZyszzmyeQ',
    'https://youtu.be/4d7a8jEW3K4'
    ]

triggerlol=['SLS',
            'LOL',
            'LMAO',
            '笑撚死',
            '笑死'
            ]

autogp=dict()

lollytalkstr='Lolly Talk & 各成員TG link(排名不分先後):\n\nLolly Talk：\nLolly Talk 大谷！！！ (https://t.me/lollytalktggroup)\n\nMui：\n黃敏蕎(牙妹)Official Fans Club (https://t.me/mankiu_fansgroup)\n\nElka：\n芷淇與夾心糖的天地🍬💜 (https://t.me/elkafansclub)\n\nEgg：\n💛BB蛋屋🥚💜 (https://t.me/eggwong_011011)\n\nMeimei：\n美軍 立正🔫💙 (https://t.me/meiarmy)\n\nSinnie：\nsin生的晚生學會（尾術部） (https://t.me/ambrosinnie)\n\nYanny：\nYanny隊長和她的啦啦隊友🪄✨ (https://t.me/yannyworldone)\n\nAh Yo：\n🧡🪀搖搖們的小天地🪀🧡 (https://t.me/+d1J5DbLTL-5jMjg1)\n\nTania：\n🤍TanTan與她的小澄人s天地🤍 (https://t.me/+0faHuD4q6w9hMzg1)'

bot = telebot.TeleBot('TOKEN')

# Disable logging for urllib3
logging.getLogger("urllib3").setLevel(logging.WARNING)

logging.basicConfig(filename='bot.log', level=logging.DEBUG)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    global angry,wtf,lol,please,pray,ban,sad,foods,suicidestr,numbers,small,big,englishwords,listofprogram,songlist,lollytalkstr,triggerlol,autogp
    today = date.today()
    timee=str(f'{int(datetime.now().strftime("%H")):0>2}:{int(datetime.now().strftime("%M")):0>2}')#locate time and date
    sderid=str(message.from_user.id)
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    name = f"{first_name} {last_name}" if last_name else first_name
    original_message = message.reply_to_message
    gpid=message.chat.id

    if message.text=='.k' and str(sderid) == '5498765941':
        autoreply(message,'Bot terminated.')
        log(timee,message,f'COMMAND FORCE-STOP')
        os._exit(0)

    if message.reply_to_message:
        original_message = message.reply_to_message
        target_message=(message.reply_to_message.message_id)
        target_msg_text=str(original_message.text)
    else:
        target_message=None
    
    

    try:
        # Check if the message is a command
        if message.text.startswith('/'):
            handle_command(message,original_message,target_message,name,sderid,today,timee,songlist,lollytalkstr)

        elif re.match(r"\$[a-zA-Z]{4}\d{4}", message.text)and len(message.text)==9:#EXAM STAT
            log(timee,message,f'COMMAND EXAM STAT {toupper(str(message.text[1:]))}')
            #os.system(f"./exam {str(message.text[1:])}")
            exam(message,toupper(str(message.text[1:])))
      

        elif re.match(r"\$[aA]{1}[sS]{1}[Kk]{1}[Cc]{2}[a-zA-Z]{2}\d{4}", message.text) and len(message.text)==12: #COMMOM CORE FAST LINK
            cc=toupper(str(message.text[4:]))
            log(timee,message,f'COMMAND CC FAST LINK {cc}')
            autoreply(message,f'https://commoncore.hku.hk/{cc}/')

        elif re.match(r"\$[Ii]{1}[Nn]{1}[Ff]{1}[Oo]{1}[Cc]{2}[HUhuGLglCHchSTst]{2}[9]{1}[0]{1}[1-9]{2}",message.text) and len(message.text)==13: #COMMOM CORE ASSESMENT
            log(timee,message,f'COMMAND CC ASSESMENT {toupper(str(message.text[5:]))}')
            result=infocc(tolower(str(message.text[5:])))
            autoreply(message,result)

        elif message.text.startswith('$google'): #GOOGLE
            detail=' '.join(message.text.split(' ')[1:])
            log(timee,message,f'COMMAND GOOGLE {detail}')
            googleing(sderid,message,today,timee)

        elif str(message.text).startswith('勁'):#AUTO REPLY
            log(timee,message,f'TRIGGERED STICKER (勁)')
            sticker_fix(message,pray,original_message)
        else:
            info=toupper(message.text) if message.text!=None else 'NOTHING'
            for word in info.split(' '):
                if word in triggerlol:
                    sticker_random(message,lol,original_message)
                    break
                elif word=='WTF':
                    sticker_random(message,wtf,original_message)
                    break
        
    except apihelper.ApiException as e:
        sderid=sderid
        log(timee,message,e)

def handle_command(message,original_message,target_message,name,sderid,today,timee,songlist,lollytalkstr):
    if True:
        if message.text.startswith('/bob') and str(sderid)=='5498765941' and target_message:#GET USER ID
            detail=f"Username: {original_message.from_user.username}\nName: {original_message.from_user.first_name + ' ' + original_message.from_user.last_name if original_message.from_user.last_name else original_message.from_user.first_name}\nID: {original_message.from_user.id}\nGPID: {original_message.chat.id}\nChat Title: {message.chat.title}\nMessage: {str(original_message.text)}"
            write('bob',' '.join(detail.split('\n'))+'\n')
            autoreply(message,detail)

        elif message.text == '/start': #START BOT
            log(timee,message,'COMMAND START-BOT')
            autoreply(message,'DLLM! I am XGU大仙! Chat with me!') 

        elif message.text.startswith('/ping'):
            log(timee,message,'PING-PONG!')
            autoreply(message,'Pong!')

        elif message.text.startswith('/bible4angle'):
            log(timee,message,'COMMAND BIBLE')
            findbible(message)
            
        elif message.text.startswith('/mygpa'):#RANDOM GPA
            log(timee,message,'COMMAND RANDOM-GPA')
            result=round(random.uniform(0.0, 4.3), 2)
            autoreply(message,f"{result}!")
            if result < 1:
                sticker_random(message,lol,original_message)

        elif message.text.startswith('/song'):#RANDOM song
            log(timee,message,'COMMAND RANDOM-SONG')
            result=(random.choice(songlist))
            autoreply(message,f"{result}")

        elif message.text.startswith('/whattoeat'): #RANDOM FOOD IN HKU
            log(timee,message,'COMMAND WHAT-TO-EAT')
            autoreply(message,f"{random.choice(foods)}!!")

        elif message.text.startswith('/gpagod'): #GPA GOD
                log(timee,message,'COMMAND GPA-GOD')
                chance=str(random.randint(0,500))
                if chance == '69' or chance == '87' or chance == '487':
                    autoreply(message,f"GPA god & 光頭白卡女忍者 保佑 {name} 過三爆四.")
                elif chance == '1' or chance == '0' or chance == '357' or chance == '37' or chance == '357' or chance == '323' or chance == '76' or chance == '26' or chance == '456' or chance == '234' or chance == '345' or chance == '453' or chance == '46' or chance == '356':
                    autoreply(message,f"GPA god 保佑 {name} 過一爆二.")
                else:
                    autoreply(message,f"GPA god 保佑 {name} .")

        elif message.text.startswith('/nosuicide'): # NO SUICIDE
            log(timee,message,'COMMAND NO-SUICIDE')
            if message.reply_to_message:
                autoreply(message.reply_to_message, suicidestr)
            else:
                autoreply(message, suicidestr)

        elif message.text.startswith('/lollytalk'): # lolly talk!
            log(timee,message,'COMMAND LT')
            if message.reply_to_message:
                autoreply(message.reply_to_message, lollytalkstr)
            else:
                autoreply(message, lollytalkstr)
        elif message.text.startswith('/tc'):#translate to chinese
            translate(message,"en","zh-tw",sderid,timee)
        elif message.text.startswith('/te'):#translate to english
            translate(message,"zh-TW","en",sderid,timee)

def report(message):
    autoreply(message, "[BOT]ERROR, incident reported to @baldheadADHDninja.")

def log(timee,message,attempt):
    #attempt=' '.join(attempt.split('\n'))
    name = message.from_user.first_name + ' ' + message.from_user.last_name if message.from_user.last_name else message.from_user.first_name
    stringing=f"{date.today()} {timee} UTC+8 | {message.from_user.id:^15} | {message.chat.id:^15} | {name:<35} | {message.chat.title} | {attempt}"
    if 'urllib3.connectionpool' not in stringing:
        logging.warning(stringing)

def write(filename,detail):
    with open(f'/root/hkubot/{filename}.txt', 'a') as f:
        f.write(detail)

def autoreply(message,bot_msg):
    bot.reply_to(message, bot_msg)

def sticker_random(message,set,original_message):
    send=random.choice(set)
    with open(f"LINK", 'rb') as f:
        bot.send_document(message.chat.id, f, reply_to_message_id=message.message_id)

def sticker_fix(message,cat,original_message):
    with open(f"LINK", 'rb') as f:
        bot.send_document(message.chat.id, f, reply_to_message_id=message.message_id)

def findbible(message):
    soup = BeautifulSoup(requests.get('https://dailyverses.net/random-bible-verse').content, "html.parser")
    page=str(soup.get_text().split("New Revised Standard Version (NRSV)")[2].split('Next verse!')[0])
    for element in range(len(page)):
        if page[-1]not in numbers:
            page=page[:-1]
        else: 
            autoreply(message,page)
            break

def toupper(string):
    returnword=''
    for element in string:
        sure=False
        for index in range(26):
            if small[index]==element:
                returnword+=big[index]
                sure=True
        if not sure:
            returnword+=element
    return returnword

def tolower(string):
    returnword=''
    for element in string:
        sure=False
        for index in range(26):
            if big[index]==element:
                returnword+=small[index]
                sure=True
        if not sure:
            returnword+=element
    return returnword

def infocc(cc):
    page=(str(BeautifulSoup(requests.get(f'https://commoncore.hku.hk/{cc}/').content, "html.parser").get_text()).split("Study Load")[-1]).split("Total:")[-1].split('\n')
    ans=[]
    final=''
    for element in range(len(page)+3):
        if page[element]==page[element+1] and page[element+2]==page[element+1] and page[element+3]==page[element+2] and page[element+4]==page[element+5] and page[element+5]==page[element+6] :
            break
        ans.append(page[element])
    while '' in ans:
        ans.remove('')
    ans = ans [ 4 : ]
    final=final+(toupper(cc))+'\n'
    for i in range( 0 , len(ans) , 2 ):
        final = final + ans[ i ] + ' ' + ans[ i + 1 ] + '\n'
    return(f'No course detail about {cc} is found.') if final == (toupper(cc))+'\n' else final

def googleing(sderid,message,today,timee):
    try:
        looping=0;answer=[]
        if len(message.text.split(' '))>1:
            results = search(' '.join(message.text.split()[1:]))#,stop=10) 
        for url in results:
                looping+=1
                if looping == 1 or looping == 6 or looping == 7 or looping == 8 or looping == 2:
                    answer.append(url)
                if looping == 9:
                    break
        autoreply(message,'\n'.join(answer))
        
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 429 or e.response.status_code == 400:
            report(message)
        else:
            raise e
def exam(message,code):
    if message.text!='GOOG1001':
        x=' '+code+' '
        PT = False
        a=0
        openclose=0
        block=[]
        otuput=[]
        for degree in listofprogram:
            url = f"http://www.exam.hku.hk/timetable/{degree}.html"
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            page=soup.get_text().split('\n')
            if openclose!=0:
                break
            for i in range(0,len(page)-3):
                if page[i] == 'There are changes in time, venue or special note for those courses in red color and bold.  Details of the changes made can be found at the Examinations Office website (www.exam.hku.hk) under the section "amendments to timetable".':
                    break
                if page[i] == '' and page[i+1] == '' and page[i+2] != ' ' and PT==True:
                    PT=False
                    openclose+=1
                if str(x) == page[i]:
                    PT=True
                if PT==True:
                    if a==0:
                        for j in range(i-3,i+1):
                            otuput.append((page[j]))
                        a+=1
                    else:
                        otuput.append((page[i]))
                if openclose!=0:
                    break
        if otuput!=[]:
            while ( '' in otuput ):
                otuput.remove('')
            while ( ' ' in otuput ):
                otuput.remove(' ')
            for i in range(3,len(otuput)):
                if otuput[i] == otuput[2] :
                    block.append(i)
            block.reverse()
            if block != []:
                for element in block:
                    otuput=otuput[0:int(element)]+otuput[int(element+1):]
            for element in range(len(otuput)):
                otuput[element]=str(otuput[element].strip(' '))

            autoreply(message,'\n'.join(otuput))
        else:
            autoreply(message,f'BOT cannot find exam of {code}')
    else:
            if message.reply_to_message:
                message.reply_to_message.reply_text("https://www.google.com/search?q=how%20to%20google")
            else:
                message.reply_text("https://www.google.com/search?q=how%20to%20google")

def translate(message,flang,tlang,sderid,timee):
    ans=''
    translator = Translator()
    if len(message.text.split(' '))>1:
        (translated_text) = translator.translate(f"{' '.join(message.text.split(' ')[1:])}", dest=tlang)
        log(timee,message,f"COMMAND TRANSLATE {' '.join(message.text.split(' ')[1:])}")
        (ans)='('.join(str(translated_text).split('(')[1:])
        fromlan=str(str(ans.split(',')[0]).split('=')[1])
        tolan=str(str(ans.split(',')[1]).split('=')[1])
        text=''.join(str(ans.split(', pronunciation=')[0]).split('=')[3:])
        pron=str(str(ans.split(', pronunciation=')[1]).split(', extra_data="{')[0])
        #rpy=f'From {fromlan} To {tolan}\nTranslated text: {text}\nPronounce as: {pron}'
        autoreply(message,text)
    elif len(message.text.split(' '))==1:
        if message.reply_to_message:
            original_message = message.reply_to_message
            target_msg_id=str(message.reply_to_message.message_id)
            target_msg_text=str(original_message.text)
            log(timee,message,f'COMMAND TRANSLATE {target_msg_text}')
            (translated_text) = translator.translate(f"{message.reply_to_message.text}", dest=tlang)
            (ans)='('.join(str(translated_text).split('(')[1:])
            fromlan=str(str(ans.split(',')[0]).split('=')[1])
            tolan=str(str(ans.split(',')[1]).split('=')[1])
            text=''.join(str(ans.split(', pronunciation=')[0]).split('=')[3:])
            pron=str(str(ans.split(', pronunciation=')[1]).split(', extra_data="{')[0])
            #rpy=f'From {fromlan} To {tolan}\nTranslated text: {text}\nPronounce as: {pron}'
            autoreply(message,text)
        else:
            autoreply(message,'字都冇隻翻條毛？')
            log(timee,message,'COMMAND TRANSLATE BLANK')




# Start the bot
bot.polling(none_stop=True)
