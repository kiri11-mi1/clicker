import pyautogui
import time


PATH = 'img/button.png'

def main():
    while True:
        coord = pyautogui.locateOnScreen(PATH)
        if coord is not None:
            mouse_coord = pyautogui.position()

            center = pyautogui.center(coord)
            pyautogui.click(center)
            print('Нашёл цель!')

            pyautogui.moveTo(mouse_coord[0], mouse_coord[1])
            time.sleep(3)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
