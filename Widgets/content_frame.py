import customtkinter as ctk
import tkinter as tk
from typing import Tuple

from .datalist_frame import DataListFrame
from .info_frame import InfoFrame
from style_manager import FontSettings

    
# メインコンテンツのフレーム
class ContentFrame(ctk.CTkFrame):
    def __init__(self, master:tk.Frame, header_name:str="HeaderFrame", **kwargs):
        super().__init__(master, **kwargs)
        # ヘッダー名設定
        self.header_name = header_name
        #文字フォント設定
        self.title_font:Tuple = FontSettings.FRAME_TITLE.value
        # フォームのセットアップをする
        self.create_widgets()
        
    def create_widgets(self):
        # 行方向のマスのレイアウトを設定する。リサイズしたときに一緒に拡大したい行をweight 1に設定。
        self.grid_rowconfigure(1, weight=1)
        # 列方向のマスのレイアウトを設定する
        self.grid_columnconfigure(0, weight=2)
        
        # フレームのラベルを表示
        self.label = ctk.CTkLabel(self, text=self.header_name, font=self.title_font)
        self.label.grid(row=0, column=0, padx=0, pady=(10,0), sticky="w")
        
        # プロジェクト一覧
        values = ["value 1", "value 2", "value 3", "value 4", "value 5", "value 6"]
        self.datalist_frame = DataListFrame(self, title="Values", values=values)
        self.datalist_frame.grid(row=1, column=0, padx=5, pady=(10, 0), sticky="nsew")
        
        self.info_frame = InfoFrame(self, header_name="プロジェクト情報")
        self.info_frame.grid(row=1, column=1, padx=(10,20), pady=10, sticky="nwe")