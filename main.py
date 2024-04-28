import flet as ft
from flet import Page, RouteChangeEvent

from views.start_view import StartView
from views.training_view import TrainingView


def main(page: Page) -> None:
    """ Function that start app file cycle """

    page.title = "TinyTyping"
    page.window_width = 900
    page.window_height = 500
    page.padding = 0
    page.window_resizable = False
    page.theme_mode = ft.ThemeMode.LIGHT
    
    start_view = StartView(page)
    training_view = TrainingView(page)
    
    def route_change(e: RouteChangeEvent) -> None:
        page.views.clear()

        # Routing
        if page.route == "/":
            page.views.append(start_view.show())
        elif page.route == "/training":
            page.views.append(training_view.show())

        page.update()

    page.on_route_change = route_change
    page.go(page.route)

    
# App start
if __name__ == "__main__":
    ft.app(target=main)