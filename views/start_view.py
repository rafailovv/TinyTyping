import flet as ft
from flet import View, Container, Column, Text, ElevatedButton


class StartView(ft.View):
    """ Start view class """

    def __init__(self, button_event):
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
                            content=ElevatedButton(text="Start", on_click=button_event),
                            alignment=ft.alignment.center
                        )
                    ])
                ],
                horizontal_alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            )
    

    def show(self):
        """ Shows view """
        
        return self.content