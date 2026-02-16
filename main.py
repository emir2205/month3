from datetime import datetime
import flet as ft

def app(page: ft.Page):
    page.title = "Домашнее задание 4"
    
    plain_text = ft.Text(value="Введите имя ниже")
    history = []

    def clear_history(e):
        history.clear()
        history_text.value = ""
        page.update()

    delete_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)
    history_text = ft.Text()

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
            history.append(txt)
            history_text.value = "История имён: \n" + ", \n".join(history)
            plain_text.color = None
            plain_text.value = f"{date} - Привет, {txt}!"
        else:
            plain_text.value = "Введите правильное имя!"
            plain_text.color = ft.Colors.RED

        page.update()

    def delete_last(e):
        if history:
            history.pop()
            history_text.value = "История имён: \n" + ", \n".join(history)
        else:
            history_text.value = "История имён пуста"

    btn = ft.TextButton("Отправить", on_click=change)
    user_input = ft.TextField(label="Enter name", on_submit=change)
    delete_last_button = ft.TextButton("Удалить последнее имя", on_click=delete_last)   
    page.add(
        plain_text, 
        user_input, 
        btn, 
        history_text, 
        delete_last_button,
        icon_button, 
        delete_button
    )

ft.app(target=app)