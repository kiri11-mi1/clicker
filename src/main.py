import pyautogui
import time
import logging
from config import Config
from bot import Bot
import os
import json


logging.basicConfig(
            format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
            level=logging.INFO,
            filename="clicker_working.log")


def make_json(content, filename='response.json'):
    """Делает json файл из словаря"""
    with open(filename, 'w') as wf:
        json.dump(content, wf, indent=2, ensure_ascii=False)


def main():
    cfg = Config()
    bot = Bot(cfg.TOKEN)

    # Устанавливаем курсор в левый верхний угол через 5 секунд после запуска скрипта
    time.sleep(5)
    pyautogui.moveTo(1, 1)

    while True:
        coord = pyautogui.locateOnScreen(cfg.button_image_path)
        if coord:
            mouse_coord = pyautogui.position()

            center = pyautogui.center(coord)
            pyautogui.click(center)
            logging.info('Нашёл цель!')
            pyautogui.screenshot(cfg.scrn_filename)

            bot.send_photo(cfg.CHAT_ID, cfg.scrn_filename, 'Нашёл цель!')

            os.remove(cfg.scrn_filename)

            pyautogui.moveTo(mouse_coord[0], mouse_coord[1])
            time.sleep(3)


if __name__ == '__main__':
    try:
        logging.info('Работа кликера началась')
        main()
    except KeyboardInterrupt:
        logging.info('Работа кликера завершена\n')
        exit()
