from concurrent.futures import ThreadPoolExecutor
from time import sleep

def main():
    texts = ["hello", "world", 'こんにちは']
    with ThreadPoolExecutor(100) as executor:
        # for i in range(20):
        #     executor.submit(foo, i)
        for t in texts:
            i = 0
            executor.submit(hello, i, t)
        print("AAAAAAA")
    print("jijiji")

def foo(i: int):
    sleep(3)
    print(f"{i + 1}回目")
    
def hello(i, text):
    print(i, text)

if __name__ == "__main__":
    main()