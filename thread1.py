from threading import Thread
import logging
import time

def sleeper(name,num,wh):
    logging.info("thread    :thread running{}".format(name))
    time.sleep(num)
    logging.info("thread    :end - {} - {}".format(num,wh))

def whitout_join():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format,level=logging.INFO,datefmt="%H:%M:%S")
    logging.info("whitout_join  :before running")
    th = Thread(target=sleeper,args=('thread 1',1,'whitout_join'))
    th.start()
    logging.info("whitout_join  :sleep ...")
    th1 = Thread(target=sleeper,args=('thread 2',2,'whitout_join'))
    th1.start()
    logging.info("whitout_join  :sleep ...")
    th2 = Thread(target=sleeper,args=('thread 3',3,'whitout_join'))
    th2.start()
    logging.info("Mwhitout_joinAIN  :sleep ...")
    th3 = Thread(target=sleeper,args=('thread 4',4,'whitout_join'))
    th3.start()
    logging.info("whitout_join  :sleep ...")
    th4 = Thread(target=sleeper,args=('thread 5',5,'whitout_join'))
    th4.start()
    logging.info("whitout_join  :all done !")

def whit_join():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format,level=logging.INFO,datefmt="%H:%M:%S")
    logging.info("whit_join  :before running")
    th = Thread(target=sleeper,args=('thread 1',1,'whit_join'))
    
    logging.info("whit_join  :sleep ...")
    th1 = Thread(target=sleeper,args=('thread 2',2,'whit_join'))
    
    logging.info("whit_join  :sleep ...")
    th2 = Thread(target=sleeper,args=('thread 3',3,'whit_join'))
    
    logging.info("whit_join  :sleep ...")
    th3 = Thread(target=sleeper,args=('thread 4',4,'whit_join'))
    
    logging.info("whit_join  :sleep ...")
    th4 = Thread(target=sleeper,args=('thread 5',5,'whit_join'))
    th.start()
    th.join()
    th1.start()
    th1.join()
    th2.start()
    th2.join()
    th3.start()
    th3.join()
    th4.start()
    th4.join()
    logging.info("MAIN  :all done !")


if __name__ == "__main__":
    print("whitout join : ....")
    whitout_join()
    time.sleep(10)
    logging.info("MAIN  :sleep program !")
    print("-------------------------------------------")
    print("whit join : ....")
    whit_join()