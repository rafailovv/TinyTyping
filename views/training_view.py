import flet as ft
from flet import View, Container, Column, Text, TextField


class TrainingView(ft.View):
    """ Training view class """

    def __init__(self):
        """ Create view """
        
        self.content = View(
            route="/training",
            controls=[
                Column([
                    Container(
                        content=Text("Набери меня в поле", text_align=ft.TextAlign.CENTER),
                        alignment=ft.alignment.center
                    ),
                    Container(
                        content=TextField(),
                        alignment=ft.alignment.center
                    )
                ])
            ],
            horizontal_alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )
        
        
    def show(self):
        """ Show view """

        return self.content