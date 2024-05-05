import flet as ft
from flet import View, Container, Column, Row, Text, TextField, ElevatedButton
import lorem
import time
import keyboard


class TrainingView(ft.View):
    """ Training view class """

    def __init__(self, page: ft.Page):
        """ Create view """
        
        super().__init__()
        self.page = page
        self.info_text = Text("Проверишь свою скорость печати?", text_align=ft.TextAlign.CENTER) 
        self.text_field = TextField(text_align=ft.TextAlign.CENTER, width=self.page.window_width * 0.75)
        self.sub_text_container = Container(content=Text(text_align=ft.TextAlign.CENTER), alignment=ft.alignment.center)
        
        self.training_button = ElevatedButton(text="Training", on_click=lambda _: self._training())
        self.back_button = ElevatedButton(text="Main Menu", on_click=lambda _: self._back_button())
        
        self.buttons = Row(width=self.page.window_width, alignment=ft.MainAxisAlignment.CENTER,
                           controls=[
                               self.training_button,
                               self.back_button
                               ])
        
        self.content = View(
            route="/training",
            controls=[
                Column([
                    Container(
                        content=self.info_text,
                        alignment=ft.alignment.center
                    ),
                    Container(
                        content=self.text_field,
                        alignment=ft.alignment.center
                    )
                ]),
                self.buttons
            ],
            horizontal_alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER
        )
        
        self.state = "Menu"
    
    
    def _back_button(self):
        """ Main menu button """
        
        if self.state == "Training":
            self.words = []
        else:
            self.info_text.value = "Проверишь свою скорость печати?"
            self.text_field.value = ""
            self.training_button.disabled = False
            self.back_button.disabled = False
                
            if self.sub_text_container in self.content.controls:
                self.content.controls.remove(self.sub_text_container)
            
            self.page.go("/")
    
    
    def _training(self):
        """ Start typing test """
        
        self.state = "Training"
        self.back_button.text = "Stop"
        self.training_button.disabled = True
        self.back_button.disabled = True
        self.words = lorem.get_word(5).replace('.', '').split()
        
        if self.sub_text_container in self.content.controls:
            self.content.controls.remove(self.sub_text_container)
        
        # Add sub text
        self.content.controls.insert(-1, self.sub_text_container)
        self.page.update()
        
        # Countdown
        for i in range(3, 0, -1):
            self.sub_text_container.content.value = i
            self.page.update()
            time.sleep(1)
        
        self.sub_text_container.content.value = "START!"
        self.page.update()
        time.sleep(1)
        
        # Start test
        i = 0
        right_words_count = 0
        self.back_button.disabled = False
        while i < len(self.words):
            
            # Extending word list
            if i == len(self.words) - 1:
                self.words = self.words[i:i+1] + lorem.get_word((i+1) * 2).replace('.', '').split()
                print(self.words)
                i = 0
            
            self.info_text.value = self.words[i]
            self.sub_text_container.content.value = f"Правильные слова: {right_words_count}"
            self.page.update()
            
            if keyboard.is_pressed("enter"):
                self.text_field.focus()
                if self.text_field.value == self.info_text.value:
                    i += 1
                    right_words_count += 1
                    self.text_field.value = ""
                    
        self.sub_text_container.content.value = f"Правильные слова: {right_words_count}"
        self.info_text.value = "Отличный результат! Попробуете улучшить его?"
        self.training_button.disabled = False
        self.back_button.text = "Main Menu"
        self.state = "Menu"
        self.page.update()
        
        
    def show(self):
        """ Show view """
        
        return self.content