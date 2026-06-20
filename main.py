import flet as ft

def main(page: ft.Page):
    # Настройки страницы
    page.title = "VPN Client"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0B0E14"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Логика кнопки
    def on_connect_click(e):
        if btn.text == "ПОДКЛЮЧИТЬ":
            btn.text = "ОТКЛЮЧИТЬ"
            btn.style.bgcolor = ft.colors.RED
            status.value = "Статус: Подключено"
            status.color = ft.colors.GREEN
        else:
            btn.text = "ПОДКЛЮЧИТЬ"
            btn.style.bgcolor = ft.colors.BLUE
            status.value = "Статус: Отключено"
            status.color = ft.colors.RED
        page.update()

    status = ft.Text("Статус: Отключено", size=20, color=ft.colors.RED)
    
    btn = ft.ElevatedButton(
        text="ПОДКЛЮЧИТЬ",
        on_click=on_connect_click,
        style=ft.ButtonStyle(
            bgcolor=ft.colors.BLUE,
            color=ft.colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=20)
        ),
        width=200,
        height=60
    )

    page.add(
        ft.Icon(ft.icons.VPN_KEY, size=100, color=ft.colors.BLUE_200),
        ft.Container(height=20),
        status,
        ft.Container(height=20),
        btn
    )

ft.app(target=main)
