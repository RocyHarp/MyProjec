#include "core/TaskQueue.h"
#include "core/ThreadPool.h"
#include "utils/Logger.h"

int main() {
    TaskQueue queue;
    ThreadPool pool(queue, 4);

    Logger::log("Server started");

    for (int i = 0; i < 10; i++) {
        queue.push({i, TaskType::COMPUTE, 50});
        queue.push({i + 100, TaskType::SLEEP, 500});
    }

    std::this_thread::sleep_for(std::chrono::seconds(5));

    Logger::log("Shutting down...");
    return 0;
}