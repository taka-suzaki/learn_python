from inputimeout import inputimeout, TimeoutOccurred


def text_dialog():
    try:
        val = inputimeout(prompt='>>', timeout=5)
    except TimeoutOccurred:
        print('Timeout!')
        val= 'something'

if __name__ == '__main__':
    try:
        while(True):
            text_dialog()
    except KeyboardInterrupt:
        print("終了します。")
    except:
        print("予期せぬエラーが発生しました。")