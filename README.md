# TradeBoost

Перед вами утилита по накрутке обменов в Steam.
Используя два аккаунта Steam с shared_secret, identity_secret мы циклически отправляем трейды между двумя аккаунтами и принимаем их.

-------------------------
### Установка
```
💲 git clone https://github.com/dotX12/TradeBoost/
💲 cd TradeBoost
💲 pip3 install -r requirements.txt
```
### settings.py
В папке settings находятся JSON файлы аккаунтов, настройте их.
```
{
    "login": "", # Логин от стима
    "password": "", # Пароль от стима 
    "API": "", # API https://steamcommunity.com/dev/apikey
    "steamid": "", # STEAM ID 
    "shared_secret": "", # shared_secret из mafile
    "identity_secret": "" # identity_secret из mafile
}
```
### tokens.py
Через запятую мы указываем STEAM ID кому мы будем отправлять все наши трейды!
Т.е мы указываем STEAM ID нашего второго аккаунта!
```
account_1 = ['settings/account1.json', '7656119833XXXXXXX']
account_2 = ['settings/account2.json', '7656119835XXXXXXX']

```

    После настройки запустите файл main.py


Примерное количество обменов за 30 минут - 300-400 штук в зависимости от нагрузки Steam.



---
### А как же треды или асинк?
#### Стим очень нестабильная вещь и даже с двумя разными потоками я ловлю кучу ошибок начиная от попытки получить инвентарь, заканчивая попыткой принять трейд. После различных тестов выяснилось что обычная синхронная версия показала себя лучше всего для буста.

