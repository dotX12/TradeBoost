# TradeBoost [RU/EN]

Перед вами утилита по накрутке обменов в Steam.
Используя два аккаунта Steam с shared_secret, identity_secret мы циклически отправляем трейды между двумя аккаунтами и принимаем их.

-------------------------
### Установка

Просто клонируйте этот репозиторий.

В папке settings находятся JSON файлы аккаунтов, настройте их.

После настройки запустите файл main.py

Наслаждайтесь!

Примерное количество обменов за 30 минут - 300-400 штук в зависимости от нагрузки Steam.

-------------------------
### А как же треды или асинк?
#### Стим очень нестабильная вещь и даже с двумя разными потоками я ловлю кучу ошибок начиная от попытки получить инвентарь, заканчивая попыткой принять трейд. После различных тестов выяснилось что обычная синхронная версия показала себя лучше всего для буста.

-------------------------


Here is a utility for boost exchanges on Steam.
Using two Steam accounts with shared_secret, identity_secret, we cyclically send trades between the two accounts and receive them.

-------------------------
### Installation

Just clone this repository.

The settings folder contains JSON files of accounts, configure them.

Once configured, run the main.py file

Enjoy!

The approximate number of exchanges in 30 minutes is 300-400, depending on the load of Steam.

-------------------------
### But what about threads or async?
#### Steam is a very unstable thing and even with two different threads, I catch a bunch of errors ranging from trying to get inventory to trying to accept a trade. After various tests, it turned out that the regular synchronous version performed best for boosting.

-------------------------
