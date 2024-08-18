import customtkinter as ctk
import tkinter as tk
from typing import Tuple

from style_manager import FontSettings

# プロジェクト情報用（右側）のフレーム
class InfoFrame(ctk.CTkFrame):
    def __init__(self, master:tk.Frame, header_name:str="InfoFrame", **kwargs):
        super().__init__(master, **kwargs)
        
        # フレームタイトル設定
        self.header_name = header_name
        # フォント設定
        self.title_font:Tuple = FontSettings.FRAME_TITLE.value
        # フォームのセットアップをする
        self.create_widgets()
        
    def create_widgets(self):
        # フレームのラベルを表示
        self.label = ctk.CTkLabel(self, text=self.header_name, font=self.title_font)
        self.label.grid(row=0, column=0, padx=20, pady=10, sticky="w")