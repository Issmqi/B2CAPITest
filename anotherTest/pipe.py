import multiprocessing

def proc1(pipe):
    pipe.send('hello')
    print('proc1  rec:',pipe.recv())

def proc2(pipe):
    print('proc1  rec:',pipe.recv())
    pipe.send('hello')

pipe=multiprocessing.Pipe()

p1=multiprocessing.Process(target=proc1,args=(pipe[0],))
p2=multiprocessing.Process(target=proc2,args=(pipe[1],))

p1.start()
p2.start()
p1.join()
p2.join()