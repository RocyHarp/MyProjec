#include "ThreadPool.h"
#include <iostream>
#include <chrono>

ThreadPool::ThreadPool(TaskQueue& queue, int size)
    : running(true)
{
    for (int i = 0; i < size; i++) {
        workers.emplace_back(&ThreadPool::workerLoop, this, std::ref(queue));
    }
}

void ThreadPool::workerLoop(TaskQueue& queue) {
    while (running) {
        Task task = queue.pop();
        execute(task);
    }
}

void ThreadPool::execute(const Task& task) {
    if (task.type == TaskType::COMPUTE) {
        volatile long long sum = 0;
        for (int i = 0; i < task.payload * 100000; i++)
            sum += i;
    } else if (task.type == TaskType::SLEEP) {
        std::this_thread::sleep_for(
            std::chrono::milliseconds(task.payload));
    }
}

ThreadPool::~ThreadPool() {
    running = false;
    for (auto& t : workers)
        if (t.joinable()) t.join();
}