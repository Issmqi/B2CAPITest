from  multiprocessing import Process
import os

def info(tittle):
    print(tittle)
    print('moudle name:',__name__)
    if hasattr(os,'getppid'):
        print('parent process id:',os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello',name)

if __name__ == '__main__':
    info('main line')
    proclist=[]
    paralist=['test1','test2']
    # s=0
    for m in paralist:
        proc=Process(target=f,args=(m,))
        proclist.append(proc)

    # p1=Process(target=f,args=('test1',))
    # proclist.append(p1)
    # p2=Process(target=f,args=('test2',))
    # proclist.append(p2)
    for i in proclist:
        i.start()
    for i in proclist:
        i.join()
