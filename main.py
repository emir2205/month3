import flet as ft

def app(page: ft.Page):
    button.content = "Другая кнопка"
    button.color = ft.Colors.GREEN_900
    btn = ft.TextButton("Flet")
    user_input = ft.TextField(label="Enter name")
    page.add(button, btn, user_input)

ft.run(app)