
import pyautogui
import time

## import time no es necesario, así como la linea 25. Corresponde a otro modulo o biblioteca
def press_capslock():

    pyautogui.click()          # Click the mouse.
    pyautogui.click(100, 200)  # Move the mouse to XY coordinates and click it.
    # Find where button.png appears on the screen and click it.
    pyautogui.click('button.png')
    # Move the mouse 400 pixels to the right of its current position.
    pyautogui.move(400, 0)
    pyautogui.doubleClick()     # Double click the mouse.
    # Use tweening/easing function to move mouse over 2 seconds.
    pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)
    
    # type with quarter-second pause in between each key
    pyautogui.write('Hello world!', interval=0.25)
    # Press the Esc key. All key names are in pyautogui.KEY_NAMES
    pyautogui.press('esc')
    # Make an alert box appear and pause the program until OK is clicked.
    pyautogui.alert('This is the message to display.')
    pyautogui.moveTo(100, 115) # Move the mouse to XY coordinates.
    time.sleep(1)  # Realiza una espera de 1 segundo
    pyautogui.click()
    pyautogui.position()
    pyautogui.dragTo(100, 200, 2, button='left')
    
    # Ejemplo de uso
press_capslock()
