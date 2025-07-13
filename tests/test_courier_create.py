import pytest
import allure
import requests

from methods.courier_methods import Courier
from helpers import *
from data import Urls, Messages


@allure.feature('Тестирование создания УЗ курьера')
class TestCreateCourier:

    @allure.title('Создание курьера с корректными данными')
    @allure.description("""1. Генерируются рег.данные'
                           2. Отправляется запрос на создание УЗ курьера
                           ОР: код ответа 201, сообщение о создании
                           3. Постусловие: удаление УЗ курьера""")
    def test_create_courier_sucsess(self, new_courier):
        assert new_courier[1].status_code == 201 and new_courier[1].text == Messages.OK, f'Статус ответа {new_courier[1].status_code}, текст ответа {new_courier[1].text}'


    @allure.title('Создание курьера c ранее зарегистрированным логином')
    @allure.description("""1. Генерируются рег.данные'
                           2. Отправляется запрос на создание УЗ курьера
                           3. Повторная отправка запроса на создание курьера с теми же рег.данными
                           ОР: код ответа 409, сообщение об ошибке
                           4. Постусловие: удаление УЗ курьера""")
    def test_create_same_courier(self, new_courier):
        login, password, first_name = new_courier[0]
        response = Courier.create_courier(login, password, first_name)
        status = response[1].status_code
        message = response[1].json().get('message')
        assert status == 409 and message == Messages.LOGIN_EXIST, f'Статус ответа {status}, текст ответа {message}'

        
    @allure.title('Создание курьера с неполными рег.данными (негативный)')
    @allure.description('''1. Отправляется запрос на создание УЗ курьера с неполными рег.данными
                        ОР: код ответа 400, сообщение об ошибке''')
    @pytest.mark.parametrize('courier_data', [{'password': generate_random_string(10), 'firstName': generate_random_string(10)},
                                         {'login': generate_random_string(10), 'firstName': generate_random_string(10)},
                                         {'firstName': generate_random_string(10)}])
    def test_create_courier_data_not_full(self, courier_data):
        response = requests.post(Urls.COURIERS_EP, data=courier_data)
        status = response.status_code
        message = response.json().get('message')                       
        assert status == 400 and message == Messages.CREATE_INVALID_DATA, f'Статус ответа {status}, текст ответа {message}'
