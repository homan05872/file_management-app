import customtkinter as ctk
import tkinter as tk
from typing import Tuple

from services.style_manager import FontSettings,StyleManager

# プロジェクト情報用（右側）のフレーム
class InfoFrame(ctk.CTkFrame):
    def __init__(self, master:tk.Frame, title:str="InfoFrame", **kwargs):
        super().__init__(master, **kwargs)
        
        # フレームタイトル設定
        self.title = title
        # フォント設定
        self.title_font:Tuple = FontSettings.FRAME_TITLE.value
        # フォームのセットアップをする
        self.create_widgets()
        
    def create_widgets(self):
        # フレームのラベルを表示
        self.label = ctk.CTkLabel(self, text=self.title, font=self.title_font)
        self.label.grid(row=0, column=0, padx=20, pady=10, sticky="w")