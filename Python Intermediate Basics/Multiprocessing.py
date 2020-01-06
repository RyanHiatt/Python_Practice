# import multiprocessing
#
# def spawn(num, num2):
#     print('Spawned! {} {}'.format(num, num2))
#
# if __name__ == '__main__':
#     for i in range(100):
#         p = multiprocessing.Process(target = spawn, args = (i, i+1))
#         p.start()
#         p.join()

#Remove p.join() to aloow processes to start simultaneously instead of sequentially



#Pulling data from multiprocessing
from multiprocessing import Pool

def job(num):
    return num * 2

if __name__ == '__main__':
    p = Pool(processes=20)
    data = p.map(job, [i for i in range(20)])
    data2 = p.map(job, [5, 2])
    p.close()
    print(data)
    print(data2)
