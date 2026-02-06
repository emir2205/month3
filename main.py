import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    plain_text = ft.Text("Домашнее задание 2-3", size=20)

    def change_theme(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        page.update()

    icon_button = ft.IconButton(icon=ft.Icons.SMART_BUTTON, on_click=change_theme)

    def change(e):
        txt = user_input.value.strip()
        user_input.value = ""
        
        date = datetime.now().strftime("%Y:%m:%d - %H:%M:%S")

        if txt:
            plain_text.color = None
            plain_text.value = f"{date} - Привет, {txt}!"
        else:
            plain_text.value = "Введите правильное имя!"
            plain_text.color = ft.Colors.RED
        
        page.update()

    user_input = ft.TextField(label="Enter name", on_submit=change)
    btn = ft.TextButton("Отправить", on_click=change)

    page.add(
        plain_text,
        user_input,
        btn,
        icon_button
    )

ft.app(target=main)