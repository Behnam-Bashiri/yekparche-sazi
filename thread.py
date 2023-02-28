from threading import Thread
import logging
import time

def printer(name,num):
    logging.info("thread    :start",name)
    time.sleep(2)
    logging.info("thread    :end",num)



if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format,level=logging.INFO,datefmt="%H:%M:%S")
    logging.info("MAIN  :before running")
    th = Thread(target=printer,args=('behnam',10,))
    th.start()
    logging.info("MAIN  :sleep ...")
    logging.info("MAIN  :all done !")
