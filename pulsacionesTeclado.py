import ctypes

def press_capslock():
    # Código de teclas (Mayuscula)
    capslock_keycode = 0x14
    
    # Llama a la función de la API de Windows para simular la pulsación de tecla
    ctypes.windll.user32.keybd_event(capslock_keycode, 0, 0, 0)  # Pulsar la tecla
    ctypes.windll.user32.keybd_event(capslock_keycode, 0, 2, 0)  # Soltar la tecla

# Ejemplo de uso
press_capslock()
