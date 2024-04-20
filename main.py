import flet as ft
from flet import Page
from flet import RouteChangeEvent

from views.start_view import StartView
from views.training_view import TrainingView


def main(page: Page) -> None:
    """ Function that start app file cycle """

    page.title = "TinyTyping"
    page.window_width = 900
    page.window_height = 500
    page.window_resizable = False
    page.theme_mode = ft.ThemeMode.LIGHT

    start_view = StartView(button_event=lambda _: page.go("/training"))
    training_view = TrainingView()

    def route_change(e: RouteChangeEvent) -> None:
        page.views.clear()
        
        # Start page
        page.views.append(start_view.show())

        # Training page
        if page.route == "/training":
            page.views.append(training_view.show())

        page.update()

    page.on_route_change = route_change
    page.go(page.route)

    
# App start
if __name__ == "__main__":
    ft.app(target=main)