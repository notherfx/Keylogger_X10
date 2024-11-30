import keyboard
import sys

current_word = ""

def on_key_event(e):
    global current_word

    if e.event_type == keyboard.KEY_DOWN:
        if e.name == 'space':
            guardar_palabra()
        else:
            current_word += e.name

def guardar_palabra():
    with open("output.txt", "a") as file:
        file.write(current_word + "\n")
    print(f'Palabra ingresada: {current_word}')
    resetear_palabra()

def resetear_palabra():
    global current_word
    current_word = ""

def detener_script():
    print("Script detenido por el usuario.")
    keyboard.unhook_all() 
    sys.exit()

keyboard.hook(on_key_event)

try:
    keyboard.wait('esc')
except KeyboardInterrupt:
    detener_script()
