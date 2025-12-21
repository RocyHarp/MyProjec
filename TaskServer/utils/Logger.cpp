#include "Logger.h"
#include <iostream>
#include <mutex>

static std::mutex logMutex;

void Logger::log(const std::string& msg) {
    std::lock_guard<std::mutex> lock(logMutex);
    std::cout << "[LOG] " << msg << std::endl;
}