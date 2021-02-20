import sys
import os
import time
import datetime

import multiprocessing as mp

def long_time_task(i):
    print('Process ID: {0}, Task: {1}'.format(os.getpid(), i))
    time.sleep(2)
    print('Task {0} - Result: {1}'.format(i, (2**20 + 3**30 + 4**40 + 5**50)))

def info(title):
    print(title)
    print("Module Name: {0}\n* Parent Process: {1}\n* Process ID: {2}\n".format(__name__, os.getppid(), os.getpid()))

def f1(name):
    info("Fuction f1")
    print("Hello {0}".format(name))

if __name__ == '__main__':
    # ----------------------------------------------------------------------------------------------------
    startTime = datetime.datetime.now()

    today = datetime.datetime.today().strftime('%F')
    parentProcessor = os.getpid()
    defaultEncoding = sys.getdefaultencoding()
    cpuCores = mp.cpu_count()

    print("\n----- BASIC INFO")
    print("* Default Encoing: {0}\n* CPU Cores: {1}\n* Main Process: {2}\n".format(defaultEncoding, cpuCores, parentProcessor))
    # ----------------------------------------------------------------------------------------------------

    # ====================================================================================================
    # TEST 1
    # long_time_task(1) # Normal, 1 core

    # subProcessor1 = mp.Process(target = long_time_task, args = (1,))
    # subProcessor2 = mp.Process(target = long_time_task, args = (2,))
    # print("Processing...")
    # subProcessor1.start()
    # subProcessor2.start()
    # subProcessor1.join()
    # subProcessor2.join()
    # ====================================================================================================

    # ====================================================================================================
    # TEST2
    # processorPool = mp.Pool()
    # for i in range(13):
    #     processorPool.apply_async(long_time_task, args = (i,))
    # print("Processing...")
    # processorPool.close()
    # processorPool.join()
    # ====================================================================================================

    # ====================================================================================================
    # TEST3
    info("Main Line")

    p = mp.Process(target = f1, args = ('Andy', ))
    p.start()
    p.join()
    # ====================================================================================================


    # ----------------------------------------------------------------------------------------------------
    endTime = datetime.datetime.now()
    runTime = str(endTime - startTime)
    print("\n----- RUN TIME INFO")
    print("* START: {0}\n* END: {1}\n* RUN TIM: {2}".format(startTime, endTime, runTime))