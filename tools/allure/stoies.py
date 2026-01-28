from enum import Enum


class AllureStory(str, Enum):
    COURSES = "Курсы"
    DASHBOARD = "Дашборд"
    REGISTRATION = "Регистрация"
    AUTHORIZATION = "Авторизация"
