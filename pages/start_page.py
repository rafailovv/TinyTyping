import flet as ft


class StartPage(ft.Page):
    """ Класс, описывающий главную страничку приложения """

    def __init__(self):
        """ Создание главное странички приложения """

        self.greeting = ft.Column([
                ft.Container(
                    content=ft.Text("TinyTyping", size=26, selectable=True),
                    alignment=ft.alignment.center
                ),
                ft.Container(
                    content=ft.Text("Welcome, Stranger!", size=20, selectable=True),
                    alignment=ft.alignment.center
                )
            ])
        self.greeting.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def show_page(self):
        """ Показывает главную страничку приложения """
        return self.greeting