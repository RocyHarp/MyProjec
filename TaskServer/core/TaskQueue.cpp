#include "TaskQueue.h"

void TaskQueue::push(Task task) {
    std::lock_guard<std::mutex> lock(mtx);
    queue.push(task);
    cv.notify_one();
}

Task TaskQueue::pop() {
    std::unique_lock<std::mutex> lock(mtx);
    cv.wait(lock, [&]{ return !queue.empty(); });

    Task task = queue.front();
    queue.pop();
    return task;
}