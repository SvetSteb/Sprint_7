from datetime import datetime

import requests
import allure

from helpers import *
from data import Urls


class Order:

    @staticmethod
    @allure.step("Создание нового заказа")
    def create_order(color):
        order_data = generate_order_data_by_color(color)
        response = requests.post(Urls.ORDERS_EP, json=order_data)
        return response

    @staticmethod
    @allure.step("Отмена заказа")
    def cancel_order(track):
        payload = {"track": track}
        response = requests.put(Urls.ORDER_CANCEL, payload)
        return response
    
    @staticmethod
    @allure.step("Получение списка заказов")
    def get_list_of_all_orders():
        response = requests.get(Urls.ORDERS_EP)
        return response