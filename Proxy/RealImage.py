from Image import Image

class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self._load_image_from_disk()

    def _load_image_from_disk(self):
        print(f"Loading {self.filename}")

    def display(self):
        print(f"Displaying {self.filename}")
