import flet as ft

from pages.start_page import StartPage


def main(page: ft.Page):
    """ Функция, запускающая жизненный цикл приложения """

    page.title = "TinyTyping"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 900
    page.window_height = 500
    page.window_resizable = False

    start_page = StartPage()

    page.add(start_page.show_page())
    page.update()

    
# Запуск приложения
if __name__ == "__main__":
    ft.app(target=main)