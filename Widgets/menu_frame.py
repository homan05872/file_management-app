import customtkinter as ctk
import tkinter as tk
from typing import Tuple
from functools import partial

from style_manager import FontSettings

# メニュー用フレーム
class MenuFrame(ctk.CTkFrame):
    def __init__(self, master:tk.Frame, header_name:str="MenuFrame", **kwargs):
        super().__init__(master, **kwargs)
        
        self.header_name:str = header_name
        self.title_font:Tuple = FontSettings.FRAME_TITLE.value
        self.menu_font:Tuple = FontSettings.MENU.value
        self.menu_items = ["プロジェクト一覧", "オプション"]

        # フォームのセットアップをする
        self.create_widgets()
        
    def create_widgets(self):
        # メニュー一覧を中央寄せ
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        # フレームのラベルを表示
        self.title = ctk.CTkLabel(self, text=self.header_name, font=self.title_font)
        self.title.grid(row=0, column=0, padx=65, pady=10, sticky="nsew")
        
        # メニュー一覧を表示
        self.menu_labels = []
        for idx, item in enumerate(self.menu_items):
            menu_label = ctk.CTkLabel(self, text=item, font=self.menu_font)
            row = idx + 1
            menu_label.grid(row=row, column=0, padx=0, pady=5, sticky="nsew")
            # ホバーイベントをバインド
            menu_label.bind("<Enter>", partial(self.on_enter, idx=idx))  # マウスがラベルに入ったとき
            menu_label.bind("<Leave>", partial(self.on_leave, idx=idx))  # マウスがラベルから出たとき
            menu_label.bind("<Button-1>", partial(self.menu_label_onclick, idx=idx))  # マウスがラベルから出たとき
            self.menu_labels.append(menu_label)  # ラベルをリストに追加

    def on_enter(self, event:tk.Event, idx:int):
        """マウスがラベルに入ったときに実行されるメソッド"""
        # IDを取得
        self.menu_labels[idx].configure(text_color="#51abf1")

    def on_leave(self, event:tk.Event, idx:int):
        """マウスがラベルから離れたときに実行されるメソッド"""
        self.menu_labels[idx].configure(text_color="#DCE4EE")
        
    def menu_label_onclick(self, event:tk.Event, idx:int):
        """ラベルがクリックされたときに実行されるメソッド"""
        self.menu_labels[idx].configure(text_color="#DCE4EE")
        if idx == 0:
            self.master.content_frame.destroy()
        label_text = self.menu_labels[idx].cget("text")
        