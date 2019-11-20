from typing import Tuple, List
from src.Image import Image
from enum import Enum


class ContentType(Enum):
    TITLE = 1,
    TEXT = 2,
    IMAGE = 3


class Content:
    def __init__(self):
        self.content: List[Tuple[ContentType, object]] = []

    def add_title(self, title: str):
        self.content.append((ContentType.TITLE, title))

    def add_text(self, text: str):
        self.content.append((ContentType.TEXT, text))

    def add_image(self, img: Image):
        self.content.append((ContentType.IMAGE, img))
