import customtkinter as ctk
import tkinter as tk
from typing import Tuple
import os

from style_manager import FontSettings,StyleManager

class HeaderFrame(ctk.CTkFrame):
    def __init__(self, master:tk.Frame, header_name:str="HeaderFrame", **kwargs):
        super().__init__(master, **kwargs)
        
        self.header_font:Tuple = FontSettings.HEADER_TITLE.value
        self.font:Tuple = FontSettings.DEFAULT.value
        self.header_name = header_name

        # フォームのセットアップをする
        self.create_widgets()

    def create_widgets(self):
        # 行方向のマスのレイアウトを設定する。リサイズしたときに一緒に拡大したい行をweight 1に設定。
        self.grid_rowconfigure(0, weight=1)
        # 列方向のマスのレイアウトを設定する
        self.grid_columnconfigure(2, weight=2)

        # フレームのラベルを表示
        self.label = ctk.CTkLabel(self, text=self.header_name, font=self.header_font)
        self.label.grid(row=1, column=0, padx=(20,100), pady=30, sticky="w")

        # 検索の入力
        self.search_input = ctk.CTkEntry(master=self, placeholder_text="検索キーワードを入力してください。", width=120, font=self.font)
        self.search_input.grid(row=1, column=2, columnspan=2, padx=20, pady=30, sticky="ew")

        # 検索ボタン
        self.search_btn = ctk.CTkButton(master=self, 
            command=self.search_btn_callback, text="検索", font=self.font)
        self.search_btn.grid(row=1, column=4, padx=10, pady=30)
        
        # フィルターボタン
        self.filter_btn = ctk.CTkButton(master=self, text="フィルター", command=self.filter_btn_callback, **StyleManager.INLINE_BTN_STYLE)
        self.filter_btn.grid(row=1, column=5, padx=(10,20), pady=30)

    def search_btn_callback(self, data):
        """
        検索ボタンが押されたときのコールバック。暫定機能として、検索キーワードをprintする
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