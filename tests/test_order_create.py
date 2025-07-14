import pytest
import allure

from methods.order_methods import Order
from helpers import *


@allure.feature('Тестирование запроса создания заказа')
class TestCreateOrder:

    @allure.title('Создание заказа с корректными данными')
    @allure.description("""1. Генерируются данные запроса'
                           2. Отправляется запрос на создание заказа
                           ОР: код ответа 201, ответ содержит track 
                           Постусловие: отмена заказа""")
    @pytest.mark.parametrize('color', [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_create_order_sucsess(self, color):
        response = Order.create_order(color)
        status = response.status_code
        message = response.text                      
        assert status == 201 and "track" in message, f'Статус ответа {status}, текст ответа {message}'
        
        #Постусловие выполняется в самом тесте для параметризованного теста заказа
        track = response.json().get('track')
        Order.cancel_order(track)
        