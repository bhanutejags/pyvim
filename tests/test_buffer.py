import random
from dataclasses import dataclass, field
import string

def random_unicode(length):
    """Creates a random string of unicode characters within the range 0000-D7FF"""

    random_unicodes = [chr(random.randrange(0xD7FF)) for _ in range(0, length)] 
    return u"".join(random_unicodes)

def random_ascii(length):
    """Creates a random string of ascii characters"""
    letters = string.ascii_letters + string.punctuation + string.whitespace
    random_letters = [letters[random.randrange(0,len(letters))] for i in range(length)]
    return u"".join(random_letters)

@dataclass()
class EditorBuffer(object):
    text: str = field(init=True, default="")
    cursor: int = field(init=True, default=0)
    text_length: int = field(init=False)

    def __post_init__(self):
        self.text_length = len(self.text)
    
    def move_cursor(new_cursor_position: int):
        if new_cursor_position > text_length:
            self.cursor = cursor
        else:
            self.cursor = new_cursor_position

    def add_text_at_end(new_text: str):
        self.text = text + new_text
        self.length = len(text)
    
    def delete_text_end(number_of_chars_removed: int):
        self.text = text[:-number_of_chars_removed]
        self.text_length = len(text)

    def add_text(new_text: str, cursor: int):
        self.text = f"{text[cursor:]}{new_text}{text[:cursor]}"
        self.cursor = cursor + len(new_text)
        self.text_length = len(text)
    
    def delete_text(start_point:int, end_point: int, cursor:int):
        self.text = f"{text[:start_point]}{text[end_point:]}"
        self.text_length = len(text)
    

def test_editor_speed():
    # input_string = random_unicode(1000)
    input_ascii_string = random_ascii(12)
    editor_buffer = EditorBuffer(text=input_ascii_string)
    editor_buffer.add_text(new_text="Hello my name is ninja", cursor=10)

if __name__ == "__main__":
    test_editor_speed()