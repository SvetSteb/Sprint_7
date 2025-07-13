from datetime import datetime, timedelta
import random
import string
import faker as f
import allure


def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string


def parse_courier_data(data):
    login = data[0][0]
    password = data[0][1]
    return login, password

def future_date():
    today = datetime.now()
    future_date = today + timedelta(days=random.randint(1, 360))
    formatted_date = future_date.strftime('%Y-%m-%d')
    return formatted_date

@allure.step('Генерирование данных заказа')
def generate_order_data_by_color(color):
    fake = f.Faker(locale="ru_RU") 
    last_name, first_name = (fake.name().split(' '))[0:2] 
    order_data = {"firstName": first_name,
                    "lastName": last_name,
                    "address": fake.address(),
                    "metroStation": random.randint(1,200),
                    "phone": fake.phone_number(),
                    "rentTime": random.randint(1, 8),
                    "deliveryDate": future_date(),
                    "comment": "Привези любой ценой",
                    "color":color}
    return order_data

#Создание более статичных, корректных данных для тестов, не связанных с созданием
#самого заказа
@allure.step('Генерирование данных заказа')
def generate_correct_order_data():
    order_data = {"firstName": "Скарлет",
                    "lastName": "О'Хара",
                    "address": "Тара, Джорджия",
                    "metroStation": 4,
                    "phone": "+7 800 355 35 35",
                    "rentTime": 5,
                    "deliveryDate": future_date(),
                    "comment": "Комментарий",
                    "color":["BLACK"]}
    return order_data
