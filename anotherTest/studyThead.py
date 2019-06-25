import threading
from time import ctime,sleep
# 进程时间
loops=[4,2]

def loop(loopid,wait_time,lock):
    print('start loop',loopid,'at:',ctime())
    sleep(wait_time)
    print('end loop', loopid, 'at:', ctime())
    lock.release()

def main():
    print('starting time at:',ctime())
    locks=[]
    loopids=range(len(loops))

    for i in loopids:
        # 创建锁对象
        lock=threading._allocate_lock()
        # 锁定
        lock.acquire()
        # 添加到locks数组
        locks.append(lock)

#     执行多线程
    for i in loopids:
        threading._start_new_thread(loop,(i,loops[i],locks[i]))

    for i in loopids:
        while locks[i].locked():
            pass

    print('all end at:',ctime())

if __name__ == '__main__':
    main()








