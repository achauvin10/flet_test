import flet as ft
import timer as tm


def main(page: ft.Page):
    page.title = "pomodoro App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll=True
    page.update()

    # create application instance
    timer1 = tm.Timer(page)
    timer2 = tm.Timer(page,40)
    # add application's root control to the page
    page.add(timer1)
    page.add(timer2)
    page.update()

ft.app(target=main)
