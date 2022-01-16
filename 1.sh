
#Нужно заменить переменные и адреса на свои

#Старт основного скрипта
python3 /home/q/dwm/Alert.py

#Самоуничтожение
echo "Пароль_пользователя" | sudo -S shred -zvu -n 35 "/home/q/dwm/Alert.py"

#Выключить компьютер
echo "Пароль_пользователя" | sudo shutdown now
