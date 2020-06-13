import telebot
import mysql.connector
import MyToken


from datetime import datetime
TOKEN = MyToken.TOKEN
myBot = telebot.TeleBot(TOKEN)
myDb = mysql.connector.connect(host='localhost',user='root',password='',database='apotek')
sql = myDb.cursor()
from telebot import apihelper
waktusekarang = datetime.now()

class Mybot:
    def __init__(self):
        self.message

    @myBot.message_handler(commands=['start', 'help'])
    def start(message):
        teks = MyToken.Jawab + "\n-- admin & developer @achmadsetiadji - Rumah Sendiri -- "+"\n" \
                        "Hari ini Tanggal "+str(waktusekarang)
        myBot.reply_to(message, teks)

    @myBot.message_handler(commands=['dataobat'])
    def menu_data_siswa(message):
        query = "select kode_obat,nama_obat,harga_obat from tabel_obat"
        sql.execute(query)
        data = sql.fetchall()
        jmldata = sql.rowcount
        kumpuldata=''
        if(jmldata>0):
            no = 0
            for x in data:
                no += 1
                kumpuldata =kumpuldata+ str(x)
                print(kumpuldata)
                kumpuldata = kumpuldata.replace('(', '')
                kumpuldata = kumpuldata.replace(')', '')
                kumpuldata = kumpuldata.replace("'", '')
                kumpuldata = kumpuldata.replace(",", '')
        else:
            print('Data Obat Kosong')
        myBot.reply_to(message,str(kumpuldata))

print(myDb)
print("-- Bot sedang berjalan --")
myBot.polling(none_stop=True)