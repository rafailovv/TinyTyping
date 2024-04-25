import flet as ft
from flet import View, Container, Column, Row, Text, TextField, ElevatedButton
import lorem
import time
import keyboard


class TrainingView(ft.View):
    """ Training view class """

    def __init__(self, page: ft.Page):
        """ Create view """
        
        self.page = page
        
        self.content = View(
            route="/training",
            controls=[
                Column([
                    Container(
                        content=Text("Проверишь свою скорость печати?", text_align=ft.TextAlign.CENTER),
                        alignment=ft.alignment.center
                    ),
                    Container(
                        content=TextField(text_align=ft.TextAlign.CENTER, width=self.page.window_width * 0.75),
                        alignment=ft.alignment.center
                    )
                ]),
                Row(width=self.page.window_width, alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ElevatedButton(text="Go", on_click=lambda _: self.start_test()),
                        ElevatedButton(text="Main Menu", on_click=lambda _: self._main_menu_button())
                    ])
            ],
            horizontal_alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER
        )
        
    
    def _main_menu_button(self):
        """ Main menu button """
        
        # Clear text field
        self.content.controls[0].controls[1].content.value = ""
        self.content.controls[0].controls[0].content.value = "Проверишь свою скорость печати?"
        
        self.page.go("/")
    
    
    def start_test(self):
        """ Start typing test """
        
        test_words = lorem.get_sentence(1).replace('.', '').split()
        
        # Delete buttons
        self.content.controls.pop(1)
        
        # Add timer
        self.content.controls.append(Container(content=Text("0", text_align=ft.TextAlign.CENTER),
                                               alignment=ft.alignment.center))
        
        # Countdown
        for i in range(3, 0, -1):
            self.content.controls[-1].content.value = i
            self.page.update()
            time.sleep(1)
        
        # Create async timer
        self.content.controls[-1].content.value = "START!"
        self.page.update()
        time.sleep(1)
        
        # Start test
        i = 0
        right_words_count = 0
        while i < len(test_words):
            self.content.controls[0].controls[0].content.value = test_words[i]
            self.content.controls[-1].content.value = f"Правильные слова: {right_words_count}"
            self.page.update()
            
            if keyboard.is_pressed("enter"):
                self.content.controls[0].controls[1].content.focus()
                if self.content.controls[0].controls[1].content.value == self.content.controls[0].controls[0].content.value:
                    i += 1
                    right_words_count += 1
                    self.content.controls[0].controls[1].content.value = ""
                    
        self.content.controls[-1].content.value = f"Правильные слова: {right_words_count}"
        self.content.controls[0].controls[0].content.value = "Отличный результат! Попробуете улучшить его?"
        self.content.controls.pop()
        self.content.controls.append(Row(wrap=True, spacing=10, run_spacing=10, width=self.page.window_width, alignment=ft.MainAxisAlignment.CENTER,
                    controls=[ElevatedButton(text="Go", on_click=lambda _: self.start_test()), ElevatedButton(text="Main Menu", on_click=lambda _: self._main_menu_button())]))
        self.page.update()
        
        
    def show(self):
        """ Show view """

        return self.content