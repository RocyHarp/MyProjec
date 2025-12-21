#ifndef THREAD_POOL_H
#define THREAD_POOL_H

#include <vector>
#include <thread>
#include <atomic>
#include "TaskQueue.h"

class ThreadPool {
private:
    std::vector<std::thread> workers;
    std::atomic<bool> running;

    void workerLoop(TaskQueue& queue);
    void execute(const Task& task);

public:
    ThreadPool(TaskQueue& queue, int size = 4);
    ~ThreadPool();
};

#endif