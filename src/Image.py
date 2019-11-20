class Image:
    def __init__(self, src: str = None, width: str = None, height: str = None):
        self.src: str = ""
        self.width: str = ""
        self.height: str = ""

        if src is not None:
            self.src = src
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height

