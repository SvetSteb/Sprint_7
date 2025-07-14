import allure

from methods.order_methods import Order

@allure.feature('Тестирование получения списка заказов')
class TestCreateOrder:

    @allure.title('Получение списка всех заказов без фильтрации')
    @allure.description("""1. Выполнить запрос списка заказов
                           ОР: код ответа 200, ответ содержит orders""")
    def test_get_list_of_orders(self):
        response = Order.get_list_of_all_orders()
        status = response.status_code
        message = response.text                      
        assert status == 200 and "orders" in message, f'Статус ответа {status}, текст ответа {message}'
    