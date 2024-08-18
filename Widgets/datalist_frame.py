import customtkinter as ctk
import tkinter as tk
from typing import List

# プロジェクト一覧表示用フレーム
class DataListFrame(ctk.CTkScrollableFrame):
    def __init__(self, master:tk.Frame, title:str, values:List[str], **kwargs):
        super().__init__(master, label_text=title, **kwargs)
        
        # チェックボックスの文字列の配列
        self.values = values
        
        self.create_widgets()
        
    def create_widgets(self):
        # 0行目を横へ広げる
        self.grid_columnconfigure(0, weight=1)
        # checkboxを保持する配列定義
        self.checkboxes = []
        
        # checkboxを一覧表示
        for i, value in enumerate(self.values):
            checkbox = ctk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="nsew")
            self.checkboxes.append(checkbox)