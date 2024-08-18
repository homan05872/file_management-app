from enum import Enum


FONT_TYPE = "meiryo"

BASE_COLOR_DARK = "#242424"

class FontSettings(Enum):
    HEADER_TITLE = (FONT_TYPE, 20)
    FRAME_TITLE = (FONT_TYPE, 17)
    DEFAULT = (FONT_TYPE, 15)
    MENU = (FONT_TYPE, 13)
    
    def __init__(self, font_type:str, font_size:int):
        self.font_type = font_type
        self.font_size = font_size

    def get_font(self):
        return (self.font_type, self.font_size)
    
class StyleManager:
    INLINE_BTN_STYLE = {
        "font": FontSettings.DEFAULT.value,
        "text_color": ("gray10", "#DCE4EE"),
        "fg_color": "transparent",
        "border_width":2,
    }
    
    TRANSPARENT_FRAME_STYLE = {
        "fg_color": BASE_COLOR_DARK,
    }