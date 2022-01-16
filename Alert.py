

#Нужные модули раскомментировать и заменить переменные и адреса на свои


from telethon import TelegramClient
from telethon import sync, events
import os


#Оповестить друга
api_id = 1488
api_hash = "2вЫЫФВФЫВФЫВФЫВФЫВФЫВФ4ee08"
session = "black_triangle"

client = TelegramClient(session, api_id, api_hash)
client.start()

client.send_message('ник_друга', 'У нас сегодня АКВОДИСКОТЕКА!')

print("Отправлено!")

#Удалить сессию-оповещалку
#os.system('echo "Пароль_пользователя" | sudo -S shred -zvu -n 35 "/home/q/black_triangle.session"')

#Эвакуировать файлы на удаленный сервер
#os.system('sshpass -p "Пароль_сервера" scp -P1488 -r /home/q/Documents/Bottom/Test2 q@127.0.0.1:/home/q/Videos')

#Удалить все секретные файлы (Востановить невозможно)
#os.system('echo "Пароль_пользователя" | sudo -S find "/home/q/Documents/Bottom/Test2" -exec shred -zvu -n 35 -u {} \;') 

#Удалить пустые папки
#os.system('rm -rf "/home/q/Documents/Bottom/Test2"') 

#Удалить кэш браузера Firefox
#os.system('echo "Пароль_пользователя" | sudo -S find "~/.cache/mozilla/firefox/" -exec shred -zvu -n 35 -u {} \;') 

#Стереть все логи (ОПАСНО!!!)
#os.system('echo "Пароль_пользователя" | sudo -S find "/var/log" -exec shred -zvu -n 35 -u {} \;') 

#Очистить оперативную память
#os.system('echo "Пароль_пользователя" | sudo sdmem')


