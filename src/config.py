import os


class Config:
    scrn_filename = 'screen.jpg'
    button_image_path = os.path.join('img', 'button.png')
    TOKEN = os.environ.get('TOKEN')
    CHAT_ID = int(os.environ.get('CHAT_ID'))
