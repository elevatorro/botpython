import telebot
import requests
import json
import psycopg2 as pg

bot = telebot.TeleBot('1061275087:AAHlKAYej5lxbF_-KOpTTQhHBEDV3G919Hk')
global temp1
temp1=0




@bot.message_handler(commands=['start'])
def asd(message):
    """""
    if message.from_user.id==a:
        bot.send_message(message.chat.id,'admin'+str(message.from_user.id))
    else:
        bot.send_message(message.chat.id,'nonadmin'+str(message.from_user.id))
"""""
    bot.send_message(message.chat.id, "/newreg - регистрация\n/aboutme - посещение и рейтинг\n/visiting - проставление посещения")




@bot.message_handler(commands=['aboutme'])
def addition(message):
    conn = pg.connect(dbname='pytdb', user='postgres', password='321', host='127.0.0.1')
    cursor = conn.cursor()
    # cursor.execute('SELECT * FROM public.teltable')

    cursor.execute("SELECT * FROM public.pyt WHERE pyt.userid='%s'"%message.from_user.id)
    # cursor.fetchall()
    #cursor.execute('SELECT * FROM public.pyt')
    data = {}
    for i in cursor:
        data.update({i[3]: i[4]})


    bot.send_message(message.chat.id, str(data))

    cursor.close()


"""""
@bot.message_handler(commands=['register'])
def register(message):
    print("ya robu")
    temp={}
    data={}
    conn = pg.connect(dbname='pytdb', user='postgres', password='321', host='127.0.0.1')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.pyt WHERE pyt.userid='%s'" % message.from_user.id)
    for i in cursor:
        data.update({i[0]:i[1]})
    if data==temp:
        cursor.execute("insert into public.pyt (userid, name, zachetka, posesh, rating) values(%s,%s,%s,0,0)",(message.from_user.id,regist.asd(),regist.zach()))
"""""
@bot.message_handler(commands=['newreg'])
def newregist(message):
    global temp1
    temp1=0
    bot.send_message(message.chat.id,"Введите Фамилию, имя и номер зачетки")


@bot.message_handler(commands=['visiting'])
def visiting(message):
    global temp1
    temp1=1
    bot.send_message(message.chat.id, "Введите Номер зачетки студента, который был на занятии\n Номер зачетки можно узнать, выгрузив базу в EXCEL файл")

@bot.message_handler(content_types=['text'])

def regist(message):
        """""
            i=0
            for i in 2:
                try:
               # if int(message.text)>-1:
                    zach=int(message.text)
            #    else:

                except ValueError:
                    imya = message.text
            """""
        global temp1
        conn = pg.connect(dbname='pytdb', user='postgres', password='321', host='127.0.0.1')
        cursor = conn.cursor()
        if temp1==0:
            mass = message.text


            asd=token(mass)[0:2]
            asd=' '.join(asd)
            zach=token(mass)[2]

            print("ya robu")
            temp = {}
            data = {}
            #conn = pg.connect(dbname='pytdb', user='postgres', password='321', host='127.0.0.1')
            #cursor = conn.cursor()
            cursor.execute("SELECT * FROM public.pyt WHERE pyt.userid='%s'" % message.from_user.id)
            for i in cursor:
                data.update({i[0]: i[1]})
            if data == temp:
                cursor.execute("insert into public.pyt (userid, name, zachet, posesh, rating) values(%s,%s,%s,0,0)",
                           (message.from_user.id, str(asd), str(zach)))
                conn.commit()
                bot.send_message(message.chat.id, "регистрация прошла успешно(надеюсь)")
            else:
                bot.send_message(message.chat.id, "Твоя телега уже зарегана")
                conn.commit()
        if temp1==1:
            mass=message.text
            #mass=int(mass)
            cursor.execute("UPDATE pyt SET posesh=posesh+1 WHERE pyt.zachet=%s",(mass,))
            conn.commit()
      #  return asd,zach


def token(string):
        start, i = 0, 0
        token_list = []
        for x in range(0, len(string)):
            if " " == string[i:i+1]:
                token_list.append(string[start:i])
                start = i + 1
            i += 1
        token_list.append(string[start:i])
        return token_list







bot.polling()