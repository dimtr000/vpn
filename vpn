import flet as ft
import time
import re

def main(page: ft.Page):
    page.title = "Custom VPN Client"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#07090E"
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    state = {
        "is_connected": False,
        "current_config": None,
    }

    CARD_COLOR = "#0E1321"
    ACCENT_CYAN = "#00F0FF"
    GREEN_GLOW = "#00FFA3"
    RED_ALERT = "#FF2E93"
    TEXT_MUTED = "#475569"

    icon_text = ft.Text("✦", size=44, color=ACCENT_CYAN, weight=ft.FontWeight.BOLD)
    
    status_text = ft.Text(
        "S T A N D B Y", 
        size=14, 
        color=TEXT_MUTED, 
        weight=ft.FontWeight.BOLD
    )
    
    info_text = ft.Text(
        "Система готова к импорту ключа", 
        size=11, 
        color=TEXT_MUTED,
        text_align=ft.TextAlign.CENTER
    )

    glow_ring = ft.Container(
        content=icon_text,
        alignment=ft.Alignment(0, 0),
        width=120,
        height=120,
        shape=ft.BoxShape.CIRCLE,
        border=ft.border.all(3, ACCENT_CYAN),
        shadow=ft.BoxShadow(blur_radius=15, color=ACCENT_CYAN, spread_radius=-2)
    )

    url_entry = ft.TextField(
        hint_text="Вставьте VLESS / XRAY ссылку",
        hint_style=ft.TextStyle(color=TEXT_MUTED, size=12),
        text_style=ft.TextStyle(color="#F1F5F9", size=12),
        bgcolor="#151C30",
        border_color="#1E293B",
        focused_border_color=ACCENT_CYAN,
        border_radius=10,
        text_align=ft.TextAlign.CENTER,
        height=45,
        content_padding=10
    )

    server_name_text = ft.Text(
        "Узел: не авторизован", 
        size=11, 
        color=TEXT_MUTED, 
        weight=ft.FontWeight.BOLD
    )

    def parse_config(link):
        link = link.strip()
        if not link.startswith("vless://"):
            return None
        match = re.search(r'#(.*)$', link)
        if match:
            return match.group(1)
        return "Secure Node"

    def load_from_entry(e):
        raw_link = url_entry.value
        server_name = parse_config(raw_link)
        if server_name:
            state["current_config"] = raw_link
            server_name_text.value = f"Узел: {server_name.upper()}"
            server_name_text.color = ACCENT_CYAN
            info_text.value = "Конфигурация успешно верифицирована"
            info_text.color = "#F1F5F9"
        else:
            info_text.value = "Ошибка: неверный формат VLESS протокола"
            info_text.color = RED_ALERT
        page.update()

    def toggle_connection(e):
        if not state["current_config"]:
            info_text.value = "Авторизация невозможна: пустой токен"
            info_text.color = RED_ALERT
            page.update()
            return

        connect_btn.disabled = True
        page.update()

        if not state["is_connected"]:
            status_text.value = "C O N N E C T I N G . . ."
            status_text.color = ACCENT_CYAN
            page.update()
            time.sleep(0.8)

            status_text.value = "P R O T E C T E D"
            status_text.color = GREEN_GLOW
            icon_text.value = "🛡"
            icon_text.color = GREEN_GLOW
            glow_ring.border = ft.border.all(3, GREEN_GLOW)
            glow_ring.shadow = ft.BoxShadow(blur_radius=15, color=GREEN_GLOW, spread_radius=-2)
            
            connect_btn.content.controls[0].value = "РАЗОРВАТЬ СВЯЗЬ"
            connect_btn.gradient = ft.LinearGradient(colors=[RED_ALERT, "#70003F"])
            
            state["is_connected"] = True
        else:
            status_text.value = "S T A N D B Y"
            status_text.color = TEXT_MUTED
            info_text.value = "Защищенный туннель закрыт"
            info_text.color = "#F1F5F9"
            icon_text.value = "✦"
            icon_text.color = ACCENT_CYAN
            glow_ring.border = ft.border.all(3, ACCENT_CYAN)
            glow_ring.shadow = ft.BoxShadow(blur_radius=15, color=ACCENT_CYAN, spread_radius=-2)
            
            connect_btn.content.controls[0].value = "УСТАНОВИТЬ СОЕДИНЕНИЕ"
            connect_btn.gradient = ft.LinearGradient(colors=["#7000FF", ACCENT_CYAN])
            state["is_connected"] = False

        connect_btn.disabled = False
        page.update()

    connect_btn = ft.Container(
        content=ft.Row([ft.Text("УСТАНОВИТЬ СОЕДИНЕНИЕ", weight=ft.FontWeight.BOLD, size=12, color="#F1F5F9")], alignment=ft.MainAxisAlignment.CENTER),
        gradient=ft.LinearGradient(colors=["#7000FF", ACCENT_CYAN]),
        border_radius=25,
        height=55,
        alignment=ft.Alignment(0, 0),
        on_click=toggle_connection
    )

    apply_btn = ft.Container(
        content=ft.Text("Интегрировать ссылку", color="#F1F5F9", size=12, weight=ft.FontWeight.BOLD),
        bgcolor="#131A2E",
        border=ft.border.all(1, "#1E293B"),
        border_radius=20,
        height=45,
        alignment=ft.Alignment(0, 0),
        on_click=load_from_entry
    )

    main_card = ft.Container(
        bgcolor=CARD_COLOR,
        border=ft.border.all(1, "#1E293B"),
        border_radius=35,
        padding=ft.padding.only(top=35, left=25, right=25, bottom=25),
        width=340,
        height=580,
        content=ft.Column([
            ft.Row([glow_ring], alignment=ft.MainAxisAlignment.CENTER),
            ft.VerticalDivider(height=10, color=ft.colors.TRANSPARENT),
            status_text,
            ft.Row([info_text], alignment=ft.MainAxisAlignment.CENTER, height=30),
            ft.VerticalDivider(height=10, color=ft.colors.TRANSPARENT),
            connect_btn,
            ft.VerticalDivider(height=15, color=ft.colors.TRANSPARENT),
            ft.Row([ft.Text("⎯⎯⎯⎯   ИМПОРТ КОНФИГУРАЦИИ   ⎯⎯⎯⎯", size=9, color="#334155", weight=ft.FontWeight.BOLD)], alignment=ft.MainAxisAlignment.CENTER),
            ft.VerticalDivider(height=10, color=ft.colors.TRANSPARENT),
            url_entry,
            ft.VerticalDivider(height=5, color=ft.colors.TRANSPARENT),
            apply_btn,
            ft.VerticalDivider(height=10, color=ft.colors.TRANSPARENT),
            ft.Row([server_name_text], alignment=ft.MainAxisAlignment.CENTER)
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

    page.add(main_card)

ft.app(target=main)
