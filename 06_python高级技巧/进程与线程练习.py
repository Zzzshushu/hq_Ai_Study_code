"""
1. 使用 threading 模块实现一个多线程下载器模拟程序：
要求：
（1）创建 5 个线程模拟下载任务
（2）每个线程下载一个文件，打印"正在下载文件 X..."（X 为线程编号）
（3）每个下载任务耗时 2 秒（使用 time.sleep 模拟）
（4）所有下载完成后，打印"所有文件下载完成！"
（5）使用 join() 确保主线程等待所有下载线程完成

2. 使用 ThreadPoolExecutor 实现一个线程池应用：
要求：
（1）创建一个包含 3 个线程的线程池
（2）提交 10 个任务到线程池，每个任务打印"任务 X 正在执行"（X 为任务编号）
（3）每个任务耗时 1 秒（使用 time.sleep 模拟）
（4）使用 submit() 方法提交任务
（5）使用 shutdown() 方法等待所有任务完成并关闭线程池
（6）观察线程池如何复用线程执行任务

"""
# import time
# from threading import Thread
#
# from adodbapi.process_connect_string import process
#
#
# def download(name):
#     print(f"正在下载文件{name}")
#     time.sleep(2)
#
#
#
# thread1 = Thread(target=download,args=("thread1",))
# thread1.start()
# thread2 = Thread(target=download,args=("thread2",))
# thread2.start()
# thread3 = Thread(target=download,args=("thread3",))
# thread3.start()
# thread4 = Thread(target=download,args=("thread4",))
# thread4.start()
# thread5 = Thread(target=download,args=("thread5",))
# thread5.start()
#
# print()
#
#
# thread1.join()
# thread2.join()
# thread3.join()
# thread4.join()
# thread5.join()
# print("所有文件打印完成")

import time
from concurrent.futures import ThreadPoolExecutor
import threading


def task(task_id):
    """任务函数，模拟耗时操作"""
    # 打印任务开始信息，同时显示当前线程名称以观察线程复用
    thread_name = threading.current_thread().name
    print(f"任务 {task_id} 正在执行，执行线程: {thread_name}")
    time.sleep(1)  # 模拟1秒耗时操作
    return f"任务 {task_id} 完成"


def main():
    # 创建一个包含3个线程的线程池
    with ThreadPoolExecutor(max_workers=3, thread_name_prefix="Worker") as executor:
        print(f"线程池已创建，最大工作线程数: 3")
        print(f"开始提交10个任务...\n")

        # 使用列表存储所有提交的任务
        futures = []

        # 提交10个任务到线程池
        for i in range(1, 11):
            # 使用submit()方法提交任务
            future = executor.submit(task, i)
            futures.append(future)
            print(f"任务 {i} 已提交")

        print(f"\n所有任务已提交，等待执行...\n")

    # 注意：当with块结束时，会自动调用executor.shutdown(wait=True)
    # 这会等待所有任务完成，然后关闭线程池

    print("\n所有任务已完成，线程池已关闭")
    print("\n任务执行详情：")

    # 获取任务执行结果
    for future in futures:
        result = future.result()  # 获取任务返回结果
        print(result)


if __name__ == "__main__":
    main()