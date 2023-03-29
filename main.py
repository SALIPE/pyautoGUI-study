import time
import pyautogui


def main(name):
    screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
    currentMouseX, currentMouseY = pyautogui.position()


    # pyautogui.click('./prints/spotify.png')
    # time.sleep(2)
    # pyautogui.click('./prints/spotify-search.png')

    # pyautogui.write('DOWNFALL', interval=0.25)
    # pyautogui.press('enter')

    # try:
    #     pyautogui.click('./prints/my-playlist.png')
    #     time.sleep(5)
    #     pyautogui.click('./prints/playlist-more-option.png')
    #     pyautogui.move(0, 500)
    #     time.sleep(2)
    #     pyautogui.click('./prints/share_btn.png')
    # except Exception as e:
    #     print('Playlist não encontrada!')
    #     return 0

    try:
        pyautogui.moveTo(10,screenHeight-10)
        pyautogui.click()
        time.sleep(3)
        pyautogui.write('whatsapp', interval=0.25)
        time.sleep(2)
        pyautogui.click('./prints/whats-btn-find.png')
    except Exception as e:
        print(e)
        print('Whatsapp não encontrado!')
        return 0
    
    try:
        time.sleep(3)
        pyautogui.click('./prints/whats-search.png')
        pyautogui.write(name, interval=0.25)
        pyautogui.press('down')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.keyDown('ctrl')
        pyautogui.press('v')
        pyautogui.keyUp('ctrl')
        pyautogui.press('enter')
    except Exception as e:
        print(e)   


if __name__ == '__main__':
    main('converse name')