import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 0.1  # FIX: Ensure PAUSE is not None

# Wait 3 seconds to prepare window
time.sleep(3)

# Step 1: Click to focus the app
pyautogui.click(792, 1071)
time.sleep(1)

# Step 2: Drag to select text
pyautogui.moveTo(663, 235)
pyautogui.mouseDown()
pyautogui.moveTo(1214, 931, duration=0.5)
pyautogui.mouseUp()
time.sleep(0.5)

# Step 3: Copy selected text
pyautogui.hotkey('ctrl', 'c')
time.sleep(1.0)

# Step 4: Read clipboard
copied_text = pyperclip.paste()
print("Copied Text:\n", copied_text)
