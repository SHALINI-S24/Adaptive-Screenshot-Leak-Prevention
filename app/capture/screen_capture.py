from PIL import ImageGrab
from datetime import datetime
from pathlib import Path


def capture_screen():
    """
    Captures the current screen and temporarily saves it.
    Returns the path of the captured image.
    """

    capture_directory = Path("data") / "temp_captures"
    capture_directory.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    image_path = capture_directory / f"screen_{timestamp}.png"

    screenshot = ImageGrab.grab()
    screenshot.save(image_path)

    return image_path


if __name__ == "__main__":
    path = capture_screen()
    print(f"Screen captured successfully: {path}")