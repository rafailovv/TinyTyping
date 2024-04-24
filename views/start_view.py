import flet as ft
from flet import View, Container, Column, Text, ElevatedButton


class StartView(ft.View):
    """ Start view class """

    def __init__(self, page: ft.Page):
        """ Create start view """

        self.content = View(
                route="/",
                controls=[
                    Column([
                        Container(
                            content=Text("TinyTyping", size=26, selectable=True),
                            alignment=ft.alignment.center
                        ),
                        Container(
                            content=Text("Welcome, Stranger!", size=20, selectable=True),
                            alignment=ft.alignment.center
                        ),
                        Container( 
                            content=ElevatedButton(text="Start", on_click=lambda _: page.go("/training")),
                            alignment=ft.alignment.center
                        )
                    ])
                ],
                horizontal_alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.MainAxisAlignment.CENTER
            )
    

    def show(self):
        """ Shows view """
        
        return self.content