import customtkinter as ctk

from Widgets.header_frame import HeaderFrame
from Widgets import menu_frame
from Widgets import content_frame
 
class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        # フォームのセットアップをする
        self.create_widgets()

    def create_widgets(self):
        # CustomTkinter のフォームデザイン設定
        ctk.set_appearance_mode("light")  # Modes: system (default), light, dark
        ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

        # フォームサイズ設定
        self.geometry("1200x650")
        self.title("ファイル管理くん")

        # 行方向のマスのレイアウトを設定する。リサイズしたときに一緒に拡大したい行をweight 1に設定。
        self.grid_rowconfigure(1, weight=1)
        # 列方向のマスのレイアウトを設定する
        self.grid_columnconfigure(1, weight=1)

        # ヘッダーフレーム
        self.header_frame = HeaderFrame(self, header_name="ファイル確認くん")
        self.header_frame.grid(row=0, column=0, columnspan=3, padx=20, pady=20, sticky="ew")
        
        # メニューバーフレーム
        self.menu_frame = menu_frame.MenuFrame(self, header_name="メニュー")
        self.menu_frame.grid(row=1, column=0, padx=(20,10), pady=(0,20), sticky="wsne")
        
        # メインコンテンツフレーム
        self.content_frame = content_frame.ContentFrame(self, header_name="プロジェクト一覧", fg_color="#242424")
        self.content_frame.grid(row=1, column=1, padx=10, pady=(0,20), sticky="wsne")

if __name__ == "__main__":
    app = App()
    app.mainloop()
