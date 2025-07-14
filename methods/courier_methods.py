from datetime import datetime

import requests
import allure

from helpers import *
from data import Urls


class Courier:

    @staticmethod
    @allure.step("Формирование набора тестовых рег.данных курьера")
    def generate_couriers_data():
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        return login, password, first_name
    
    
    @staticmethod
    @allure.step("Регистрация курьера")
    def create_courier(login, password, first_name):
        login_pass = []
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post(Urls.COURIERS_EP, data=payload)
        # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)
        return login_pass, response


    @staticmethod
    @allure.step("Удаление курьера по ID")
    def delete_coutier(id):
        delete_resp = requests.delete(f'{Urls.COURIERS_EP}{id}', json={"id": id})
        return delete_resp

    @staticmethod
    @allure.step("Авторизация курьера по  логин/пароль")
    def courier_login(login, password):
        payload = {"login": login, "password": password}
        login_resp = requests.post(Urls.COURIERS_LOGIN_EP, json=payload)
        return login_resp
    