import telebot
import time
import psycopg2

def chek(message):
    connection = psycopg2.connect(user = "thzrixmbpxycue",
                                  password = "7184838441baf33aa0986afeca61e726ab610163a77c357087e3e826fc71fc5c",
                                  host = "ec2-54-210-128-153.compute-1.amazonaws.com",
                                  database = "d7tofl99vg7pq2")
    cursorr = connection.cursor()
    sql = "SELECT kanal FROM grs WHERE grid=message.chat.id"
    cursorr.execute(sql)
    resultt = cursorr.fetchone()
    if resultt is None:
    	return False
            
def getdata(message):
	chatid = message.chat.id
	chatidd = str(chatid)
	msg = ""
	connection = psycopg2.connect(user = "thzrixmbpxycue",password = "7184838441baf33aa0986afeca61e726ab610163a77c357087e3e826fc71fc5c",host = "ec2-54-210-128-153.compute-1.amazonaws.com",database = "d7tofl99vg7pq2")
	cursorr = connection.cursor()
	cursorr.execute("SELECT kanal FROM grs WHERE grid=" + chatidd)
	resultt = cursorr.fetchall()
	for x in resultt:
		msg += "{}\n".format(x)
	if msg is None:
		bot.send_message(message.chat.id, "Hech narsa yoq")
		connection.close()
	else:
		bot.send_message(message.chat.id, msg)
		connection.close()
		
def newchannel(message,chan):
    connection = psycopg2.connect(user = "thzrixmbpxycue",
                                  password = "7184838441baf33aa0986afeca61e726ab610163a77c357087e3e826fc71fc5c",
                                  host = "ec2-54-210-128-153.compute-1.amazonaws.com",
                                  database = "d7tofl99vg7pq2")
    channe = str(chan)
    cursor = connection.cursor()
    sql_select_query = """SELECT kanal FROM grs WHERE grid = %s"""
    cursor.execute(sql_select_query, (message.chat.id, ))
    record = cursor.fetchone()
    msg = str(record)
    if  channe not in record:
        sql_update_query = """INSERT INTO grs (grid, userid, kanal) VALUES (%s, %s, %s)"""
        cursor.execute(sql_update_query, (message.chat.id,message.from_user.id,channe))
        bot.send_message(message.chat.id, "Guruhingiz kanalingizga ulandi." + msg)
        connection.close()
    else:
        sql_update_query = """Update grs set kanal = %s where grid = %s"""
        cursor.execute(sql_update_query, (channe, message.chat.id))
        bot.send_message(message.chat.id, "Guruhingiz kanalingizga qayta ulandi." + msg)
        connection.close()

username = "thzrixmbpxycue"
password = "7184838441baf33aa0986afeca61e726ab610163a77c357087e3e826fc71fc5c"
hostname = "gdt"
database = "d7tofl99vg7pq2"

bot = telebot.TeleBot("931190511:AAEuhHmrIiN5Lc_lNQq-ANjeauytWH2i5Gc")

@bot.message_handler(commands=['start'])
def welcome(message):
	if message.chat.type == 'private':
	    chatid = str(message.from_user.id)
	    bot.send_message(message.from_user.id, "Assalomu alaykum." + chatid,parse_mode='html')

@bot.message_handler(commands=['dellall'])
def dellall(message):
    connection = psycopg2.connect(user = "thzrixmbpxycue",password = "7184838441baf33aa0986afeca61e726ab610163a77c357087e3e826fc71fc5c",host = "ec2-54-210-128-153.compute-1.amazonaws.com",database = "d7tofl99vg7pq2")
    cursorr = connection.cursor()
    cursorr.execute("TRUNCATE grs")
    connection.close()
@bot.message_handler(commands=['getall'])
def getall(message):
    getdata(message)
    
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'supergroup':
		if  '/set' in message.text:
			channel=message.text.replace('/set ','').split(" ",1)[0]
			status = ['creator', 'administrator']
			for chri in status:
				if chri == bot.get_chat_member(chat_id=channel, user_id=message.from_user.id).status:
					newchannel(message,channel)
					break
			else:
				bot.send_message(message.chat.id, "Botni kanalga admin qilmadingiz.")
		else:
		    pass

# Filter for words
def words_filter(msg, words):
    if not msg.text:
        return False
    for word in words:
        if word in msg.text:
            return True
    return False


bot.polling(none_stop=True)
