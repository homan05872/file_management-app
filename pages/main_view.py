import tkinter as tk
import customtkinter
import os

FONT_TYPE = "meiryo"

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # メンバー変数の設定
        self.fonts = (FONT_TYPE, 15)
        self.csv_filepath = None

        # フォームのセットアップをする
        self.setup_form()

    def setup_form(self):
        # CustomTkinter のフォームデザイン設定
        customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

        # フォームサイズ設定
        self.geometry("1200x650")
        self.title("ファイル管理くん")

        # 行方向のマスのレイアウトを設定する。リサイズしたときに一緒に拡大したい行をweight 1に設定。
        self.grid_rowconfigure(1, weight=1)
        # 列方向のマスのレイアウトを設定する
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=1)

        # 1つ目のフレームの設定
        # stickyは拡大したときに広がる方向のこと。nsew で4方角で指定する。
        self.header_frame = HeaderFrame(master=self, header_name="ファイル確認くん")
        self.header_frame.grid(row=0, column=0, columnspan=3, padx=20, pady=20, sticky="ew")
        
        # 左側のフレーム
        self.left_frame = LeftFrame(master=self, header_name="メニュー")
        self.left_frame.grid(row=1, column=0, padx=(20,10), pady=0, sticky="ns")
        
        # メインコンテンツフレーム
        self.content_frame = ContentFrame(master=self, header_name="プロジェクト一覧", fg_color="#242424")
        self.content_frame.grid(row=1, column=1, padx=10, pady=0, sticky="wsne")
        
        # 右側のフレーム
        self.content_frame = RightFrame(master=self, header_name="プロジェクト情報")
        self.content_frame.grid(row=1, column=2, padx=(10,20), pady=10, sticky="nwe")

class HeaderFrame(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="HeaderFrame", **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fonts = (FONT_TYPE, 15)
        self.header_name = header_name

        # フォームのセットアップをする
        self.setup_form()

    def setup_form(self):
        # 行方向のマスのレイアウトを設定する。リサイズしたときに一緒に拡大したい行をweight 1に設定。
        self.grid_rowconfigure(0, weight=1)
        # 列方向のマスのレイアウトを設定する
        self.grid_columnconfigure(2, weight=2)

        # フレームのラベルを表示
        self.label = customtkinter.CTkLabel(self, text=self.header_name, font=(FONT_TYPE, 20))
        self.label.grid(row=1, column=0, padx=(20,100), pady=30, sticky="w")

        # 検索の入力
        self.search_input = customtkinter.CTkEntry(master=self, placeholder_text="検索キーワードを入力してください。", width=120, font=self.fonts)
        self.search_input.grid(row=1, column=2, columnspan=2, padx=20, pady=30, sticky="ew")

        # 検索ボタン
        self.search_btn = customtkinter.CTkButton(master=self, 
            text_color=("gray10", "#DCE4EE"),   # ボタンを白抜きにする
            command=self.search_btn_callback, text="検索", font=self.fonts)
        self.search_btn.grid(row=1, column=4, padx=10, pady=30)
        
        # フィルターボタン
        self.filter_btn = customtkinter.CTkButton(master=self, command=self.filter_btn_callback, border_width=2, fg_color="transparent",
                                                  text="フィルター", font=self.fonts)
        self.filter_btn.grid(row=1, column=5, padx=(10,20), pady=30)

    def search_btn_callback(self, data):
        """
        検索ボタンが押されたときのコールバック。暫定機能として、ファイルの中身をprintする
        """
        print(self.search_input.get())

    def filter_btn_callback(self):
        """
        フィルターボタンが押されたときのコールバック。暫定機能として、ファイルの中身をprintする
        """
        print(self.search_input.get())
            
    @staticmethod
    def file_read():
        """
        ファイル選択ダイアログを表示する
        """
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = tk.filedialog.askopenfilename(filetypes=[("csvファイル","*.csv")],initialdir=current_dir)

        if len(file_path) != 0:
            return file_path
        else:
            # ファイル選択がキャンセルされた場合
            return None


class LeftFrame(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="LeftFrame", **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fonts = (FONT_TYPE, 15)
        self.header_name = header_name

        # フォームのセットアップをする
        self.setup_form()
        
    def setup_form(self):
        # フレームのラベルを表示
        self.label = customtkinter.CTkLabel(self, text=self.header_name, font=(FONT_TYPE, 17))
        self.label.grid(row=0, column=0, padx=70, pady=10, sticky="w")

# プロジェクト情報用（右側）のフレーム
class RightFrame(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="RightFrame", **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fonts = (FONT_TYPE, 15)
        self.header_name = header_name
        
        # フォームのセットアップをする
        self.setup_form()
        
    def setup_form(self):
        # フレームのラベルを表示
        self.label = customtkinter.CTkLabel(self, text=self.header_name, font=(FONT_TYPE, 17))
        self.label.grid(row=0, column=0, padx=20, pady=10, sticky="w")

# メインコンテンツのフレーム
class ContentFrame(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="HeaderFrame", **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fonts = (FONT_TYPE, 15)
        self.header_name = header_name
        
        # フォームのセットアップをする
        self.setup_form()
        
    def setup_form(self):
        # 行方向のマスのレイアウトを設定する。リサイズしたときに一緒に拡大したい行をweight 1に設定。
        self.grid_rowconfigure(1, weight=1)
        # 列方向のマスのレイアウトを設定する
        self.grid_columnconfigure(0, weight=2)
        
        # フレームのラベルを表示
        self.label = customtkinter.CTkLabel(self, text=self.header_name, font=(FONT_TYPE, 17))
        self.label.grid(row=0, column=0, padx=0, pady=(10,0), sticky="w")
        
        # # フレームのラベルを表示
        # self.label = customtkinter.CTkLabel(self, text=self.header_name, font=(FONT_TYPE, 17))
        # self.label.grid(row=0, column=0, padx=20, pady=30, sticky="w")
        
        values = ["value 1", "value 2", "value 3", "value 4", "value 5", "value 6"]
        self.datalist_frame = DataListFrame(self, title="Values", values=values)
        self.datalist_frame.grid(row=1, column=0, padx=5, pady=(10, 0), sticky="nsew")

# プロジェクト一覧表示のフレーム
class DataListFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.checkboxes = []

        for i, value in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(self, text=value)
            checkbox.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="nsew")
            self.checkboxes.append(checkbox)

if __name__ == "__main__":
    app = App()
    app.mainloop()
