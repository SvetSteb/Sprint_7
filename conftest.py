import pytest

from methods.courier_methods import Courier
from methods.order_methods import Order
from helpers import parse_courier_data


@pytest.fixture
def new_courier():
    login, password, first_name  = Courier.generate_couriers_data()
    courier_data = Courier.create_courier(login, password, first_name)
    yield courier_data

    login, password = parse_courier_data(courier_data)
    login = Courier.courier_login(login, password)   
    user_id = login.json()['id']
    Courier.delete_coutier(user_id)
    


@pytest.fixture
def login_courier():
    login, password, first_name  = Courier.generate_couriers_data()
    courier_data = Courier.create_courier(login, password, first_name)
    login, password = parse_courier_data(courier_data)
    login = Courier.courier_login(login, password)   
    yield login

    user_id = login.json()['id']
    Courier.delete_coutier(user_id) 


@pytest.fixture
def new_order():
    order = Order.create_order(["BLACK"])
    yield order
    
    track = order.json().get('track')
    Order.cancel_order(track)
