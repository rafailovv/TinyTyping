import flet as ft
from flet import View, Container, Column, Stack, Image, Text, ElevatedButton


class StartView(ft.View):
    """ Start view class """

    def __init__(self, page: ft.Page):
        """ Create start view """
        
        self.page = page
        
        background = Container(
            Image(
                src="../img/start background.png",
                width=self.page.window_width,
                height=self.page.window_height,
                fit=ft.ImageFit.FILL,
                filter_quality=ft.FilterQuality.HIGH,
                color=ft.colors.BLACK54,
                color_blend_mode=ft.BlendMode.DARKEN
            )
        )

        self.content = View(
                route="/",
                controls=[
                    Stack([
                        background,
                        Column([
                            Container(
                                content=Text("TinyTyping", size=32, selectable=True, color=ft.colors.GREEN_ACCENT_700),
                                alignment=ft.alignment.center),
                            Container(
                                content=Text("Welcome, Stranger!", size=26, selectable=True, color=ft.colors.GREEN_ACCENT_700),
                                alignment=ft.alignment.center),
                            Container( 
                                content=ElevatedButton(text="Start",color=ft.colors.RED_800, bgcolor=ft.colors.GREEN_600, width=120, on_click=lambda _: page.go("/training")),
                                alignment=ft.alignment.center)
                            ])
                    ])
                ],
                horizontal_alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.MainAxisAlignment.CENTER
            )
        self.content.padding = 0
    

    def show(self):
        """ Shows view """
        
        return self.content