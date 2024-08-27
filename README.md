# Виджет успешных транзакций

## Содержание
+ Описание
+ Пример работы
+ Использование
+ Тестирование

## Описание
Виджет для банковского приложения, который отображает
несколько последних успешных банковских операций клиента.
Проект содержит модули:
+ masks.py
+ processing.py
+ widget.py
+ generators.py
+ decorators.py
+ utils.py
+ external_api.py

## Пример работы
![пример](https://my.sky.pro/5987ea2b7acbe5e5379157f8c4f0fb7f.svg)
## Использование
```
print("Hello, World!")
```
Научиться этим пользоваться [здесь](https://my.sky.pro/student-cabinet/stream/1912/lessons)

## Тестирование
Для проверки корректности работы всех функций программы предусмотрены 
модули для тестирования: 

- **test_masks.py** для функционального модуля **masks.py**
- **test_processing.py** для функционального модуля **processing.py**
- **test_widget.py** для функционального модуля **widget.py**
- **test_generators.py** для функционального модуля **generators.py**
- **test_decorators.py** для функционального модуля **decorators.py**
- **test_utils.py** для функционального модуля **utils.py**
- **test_external_api.py** для функционального модуля **external_api.py**

Вы можете выполнить проверку, запустив фреймворк pytest и запустив инструмент
Cove coverage с помощью команд:

`pytest --cov`
 — при активированном виртуальном окружении.
`poetry run pytest --cov`
 — через poetry.