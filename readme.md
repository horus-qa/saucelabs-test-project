# UI Automation Test Suite for Saucedemo

Автоматизированные end-to-end тесты для  тестового магазина [Sauce Labs](https://www.saucedemo.com/).
Тесты охватывают ключевые пользовательские сценарии интернет-магазина.


## 📁 Структура проекта

<pre> <code>
saucelabs-test-project/
├── base/   - Базовый класс
├── pages/  —  Page Object Models (POM)
│    ├── login_page.py       - страница авторизации
│    ├── main_page.py        - главная страница каталога товаров
│    ├── checkout_page.py    - страница оформления заказа
│    ├── client_info_page.py - страница ввода персональных данных
│    ├── payment_page.py     - страница оплаты
│    └── finish_page.py      - страница подтверждения заказа
├── screen/          — скриншоты
├── tests/           — тесты
├── utilities/       — утилиты, логи
├── requirements.txt — зависимости
└── README.md</code> </pre>

## 📊Тест-кейсы

**test_buy_product_1()**

Полный цикл покупки товара:

* ✅ Авторизация стандартным пользователем
* ✅ Выбор товара #1 из каталога
* ✅ Переход в корзину и оформление заказа
* ✅ Заполнение персональной информации
* ✅ Прохождение процесса оплаты
* ✅ Подтверждение успешного завершения заказа

**test_buy_product_2()**

Сокращенный цикл покупки:

* ✅ Авторизация
* ✅ Выбор товара #2
* ✅ Добавление в корзину и переход к оформлению

**test_buy_product_3()**

Сокращенный цикл покупки:

* ✅ Авторизация
* ✅ Выбор товара #3
* ✅ Добавление в корзину и переход к оформлению


## 🚀 Как запустить

1. Клонировать репозиторий
````
git clone https://github.com/horus-qa/saucelabs-test-project.git
cd saucelabs-test-project
````
2. Создать и активировать виртуальное окружение
````
python -m venv venv
````
Для Windows:
````
venv\Scripts\activate
````

Для macOS/Linux:
````
source venv/bin/activate
````

3. Установить зависимости
````
pip install -r requirements.txt
````

4. Запустить тест
````
pytest tests/
````

## 🧰 Стек

* Python 3.8+
* Selenium WebDriver 4.35.0
* WebDriver Manager 4.0.2
* Pytest 8.4.1
* Pytest-order 1.3.0