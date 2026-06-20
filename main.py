import flet as ft

def main(page: ft.Page):
    # --- НАСТРОЙКИ СТРАНИЦЫ ---
    page.title = "VPN Client Pro"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0F0F13"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = 30

    # --- ЛОГИКА ---
    def on_connect_click(e):
        if connect_button.text == "ПОДКЛЮЧИТЬ":
            connect_button.text = "ОТКЛЮЧИТЬ"
            connect_button.bgcolor = ft.colors.RED_400
            status_text.value = "Статус: Соединение установлено"
            status_text.color = ft.colors.GREEN_400
        else:
            connect_button.text = "ПОДКЛЮЧИТЬ"
            connect_button.bgcolor = ft.colors.BLUE_400
            status_text.value = "Статус: Отключено"
            status_text.color = ft.colors.GREY_500
        page.update()

    # --- ИНТЕРФЕЙС ---
    # Заголовок
    header = ft.Text("VPN Dashboard", size=28, weight=ft.FontWeight.BOLD)
    
    # Статус
    status_text = ft.Text("Статус: Отключено", size=16, color=ft.colors.GREY_500)
    
    # Основная кнопка
    connect_button = ft.ElevatedButton(
        text="ПОДКЛЮЧИТЬ",
        on_click=on_connect_click,
        style=ft.ButtonStyle(
            bgcolor=ft.colors.BLUE_400,
            color=ft.colors.WHITE,
            padding=20,
            shape=ft.RoundedRectangleBorder(radius=15),
        ),
        width=300,
    )

    # Список серверов (пример)
    server_dropdown = ft.Dropdown(
        label="Выберите сервер",
        options=[
            ft.dropdown.Option("Netherlands"),
            ft.dropdown.Option("Germany"),
            ft.dropdown.Option("USA"),
        ],
        width=300,
        bgcolor=ft.colors.WHITE10,
    )

    # Собираем всё в колонку
    page.add(
        ft.Column(
            [
                header,
                ft.SizedBox(height=20),
                server_dropdown,
                ft.SizedBox(height=20),
                status_text,
                ft.SizedBox(height=40),
                connect_button,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

# --- ЗАПУСК ---
if __name__ == "__main__":
    ft.app(target=main)
