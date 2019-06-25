from multiprocessing import Process

def fun(name):
    print('hello',name)

if __name__ == '__main__':
    p=Process(target=fun,args=('test',))
    p.start()
    p.join()
