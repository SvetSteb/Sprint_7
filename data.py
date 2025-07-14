class Urls:

    URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'
    COURIERS_EP = f'{URL}courier/'
    COURIERS_LOGIN_EP = f'{COURIERS_EP}login/'
    ORDERS_EP= f'{URL}orders/'
    ORDER_CANCEL = f'{ORDERS_EP}cancel'

class Messages:

    OK = '{"ok":true}'
    LOGIN_EXIST = "Этот логин уже используется. Попробуйте другой."
    CREATE_INVALID_DATA = "Недостаточно данных для создания учетной записи"
    LOGIN_NOT_ALL_FIELD = "Недостаточно данных для входа"
    LOGIN_INVALID_DATA = "Учетная запись не найдена"

class Users:
    EXIST_COURIER_LOGIN =  "sssveta" 
    EXIST_COURIER_PASSWORD = "1234"
    