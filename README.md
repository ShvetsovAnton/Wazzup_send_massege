# Отправка сообщений через Wazzup

Для выполнения рассылки нам понадобиться:
* Id google sheet, у таблицы должны быть права "Редактор"
[![imageup.ru](https://imageup.ru/img286/3979243/chrome_4xgeyuxast.png)](https://imageup.ru/img286/3979243/chrome_4xgeyuxast.png.html)
* Номера должны быть добавлены в колонку A1:A1000
[![imageup.ru](https://imageup.ru/img200/3979250/chrome_lkykx7vzij.png)](https://imageup.ru/img200/3979250/chrome_lkykx7vzij.png.html)
* Id chanel Wazzup
[![imageup.ru](https://imageup.ru/img167/3979242/opera_xtuhqmw3q8.png)](https://imageup.ru/img167/3979242/opera_xtuhqmw3q8.png.html)
* Tokne Wazzup
[![imageup.ru](https://imageup.ru/img220/3979244/opera_ns8edpw5vm.png)](https://imageup.ru/img220/3979244/opera_ns8edpw5vm.png.html)
* Задать время для отправки одного сообщения в секундах

## Как установить


- Создайте файл  учётную запись на `console.cloud.google.com`
- Получив `.json` с данными, положить его в корневой каталог раядом с `main.py`


## Требования к окружению

Python3 должен быть уже установлен.
Затем используйте  pip  (или  pip3 , есть конфликт с Python2) для установки зависимостей:

`pip install -r requirements.txt`
