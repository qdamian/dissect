import threading
from aa import aa_func
from ba import ba_func
from ab import ab_func
from bb import bb_func

def main():
    for func in (aa_func, ba_func, ab_func, bb_func):
        thread = threading.Thread(target=func)
        thread.start()
        thread.join()

if __name__ == '__main__':
    main()
