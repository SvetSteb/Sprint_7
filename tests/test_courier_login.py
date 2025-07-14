import pytest
import allure
import requests

from methods.courier_methods import Courier
from helpers import *
from data import Urls, Messages, Users


@allure.feature('Тестирование авторизации с УЗ курьера')
class TestCourierLogin:

    @allure.title('Авторизация курьера с корректными данными')
    @allure.description("""1. Генерируются рег.данные'
                           2. Отправляется запрос на создание УЗ курьера
                           3. Авторизация с корректными данными УЗ
                           ОР: код ответа 200, ответ содержит id 
                           Постусловие: удаление УЗ курьера""")
    def test_courier_login_sucsess(self, login_courier):
        status = login_courier.status_code
        message = login_courier.text
        assert status == 200 and "id" in message, f'Статус ответа {status}, текст ответа {message}'


    @allure.title('Авторизация с неполными данными в теле запроса')
    @allure.description("""1. Авторизация с неполными данными зарегистрированной УЗ
                           ОР: код ответа 400, ответ содержит  сообщение об ошибке""")
    @pytest.mark.parametrize('login_data', [{"login": Users.EXIST_COURIER_LOGIN, "password": ""}, 
                                            {"login": "", "password": Users.EXIST_COURIER_PASSWORD} ])
    def test_login_without_field(self, login_data):
        response = requests.post(Urls.COURIERS_LOGIN_EP, json=login_data)
        status = response.status_code
        message = response.json().get('message')                       
        assert status == 400 and message == Messages.LOGIN_NOT_ALL_FIELD, f'Статус ответа {status}, текст ответа {message}'

    @allure.title('Авторизация существующего пользователя с неверным паролем')
    @allure.description("""1. Генерируются рег.данные'
                           2. Отправляется запрос на создание УЗ курьера
                           3. Авторизация с корректным логином и неверным паролем
                           ОР: код ответа 404, ответ содержит сообщение об ошибке
                           Постусловие: удаление УЗ курьера""")
    def test_courier_password_incorrect(self, new_courier):
        login = new_courier[0][0]
        response = Courier.courier_login(login, 'fake_password')
        status = response.status_code
        message = response.json().get('message')                       
        assert status == 404 and message == Messages.LOGIN_INVALID_DATA, f'Статус ответа {status}, текст ответа {message}' 

    @allure.title('Авторизация с незарегистрированным логином')
    @allure.description("""1. Генерируется случайный login
                            2. Авторизация с полученным логином
                           ОР: код ответа 404, ответ содержит сообщение об ошибке""")
    def test_courier_login_not_exist(self):
        login = generate_random_string(10)
        response = Courier.courier_login(login, '12345')
        status = response.status_code
        message = response.json().get('message')                       
        assert status == 404 and message == Messages.LOGIN_INVALID_DATA, f'Статус ответа {status}, текст ответа {message}'
