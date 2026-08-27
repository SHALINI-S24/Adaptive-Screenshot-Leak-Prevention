import keyboard
from datetime import datetime

from app.capture.screen_capture import capture_screen


def on_screenshot_attempt():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"[{timestamp}] Screenshot attempt detected")

    image_path = capture_screen()

    print(f"Screen captured: {image_path}")


print("======================================")
print(" Screenshot Leak Prevention System")
print(" Monitoring started...")
print(" Press ESC to stop")
print("======================================")

keyboard.add_hotkey("print screen", on_screenshot_attempt)

keyboard.wait("esc")

print("Monitoring stopped.")