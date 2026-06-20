from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.animation import Animation
from plyer import vibrator
from jnius import autoclass

# Определение UI
KV = '''
MDScreen:
    md_bg_color: "#090A0F"
    BoxLayout:
        orientation: 'vertical'
        MDIconButton:
            id: connect_btn
            icon: "power"
            icon_size: "64sp"
            pos_hint: {"center_x": .5, "center_y": .5}
            theme_icon_color: "Custom"
            icon_color: "#10B981"
            on_release: app.toggle_vpn()
'''

class VPNApp(MDApp):
    is_connected = False

    def build(self):
        return Builder.load_string(KV)

    def toggle_vpn(self):
        # 1. Вибрация
        vibrator.vibrate(0.1)
        
        # 2. Анимация
        btn = self.root.ids.connect_btn
        anim = Animation(size=(120, 120), d=0.1) + Animation(size=(100, 100), d=0.1)
        anim.start(btn)
        
        # 3. Логика VPN (заглушка для системного вызова)
        if not self.is_connected:
            self.start_vpn_service()
        else:
            self.stop_vpn_service()

    def start_vpn_service(self):
        # Здесь происходит обращение к Android VpnService
        # PythonActivity = autoclass('org.kivy.android.PythonActivity')
        # intent = Intent(PythonActivity.mActivity, MyVpnService.class)
        # PythonActivity.mActivity.startService(intent)
        print("VPN: Запрос авторизации системного туннеля")
        self.is_connected = True

    def stop_vpn_service(self):
        print("VPN: Отключение")
        self.is_connected = False

if __name__ == '__main__':
    VPNApp().run()
