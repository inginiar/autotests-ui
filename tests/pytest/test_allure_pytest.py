import allure


@allure.step("Открытие браузера")
def open_browser():
    with allure.step("Выбор браузера"):
        pass

    with allure.step("Старт браузера"):
        pass


@allure.step("Создание курса")
def create_course():
    pass

@allure.step("Закрытие браузера")
def close_browser():
    pass

def test_feature():
    open_browser()
    create_course()
    close_browser()

