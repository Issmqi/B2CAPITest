import threading
from time import ctime,sleep

loops=[4,2]
class ThreadFunc(object):

    def __init__(self,func,args):
        self.func=func
        self.args=args
        # self.name=name

    def __call__(self):
        self.func(*self.args)#代替apply函数
        # apply(self.func, self.args)



def loop(loopid,wait_time):
    print('start loop', loopid, 'at:', ctime())
    sleep(wait_time)
    print('end loop', loopid, 'at:', ctime())







def main():
    print('starting time at:', ctime())
    threads=[]
    loopids=range(len(loops))
    # 创建进程
    for i in loopids:
        # t=threading.Thread(target=loop,args=(i,loops[i]))
        t=threading.Thread(
            target=ThreadFunc(loop,(i,loops[i])))
        threads.append(t)

#     开始进程

    for i in loopids:
        threads[i].start()

    # 等待所有结束进程
    for i in loopids:
        threads[i].join()

    print('all end at:',ctime())

if __name__ == '__main__':
    main()


