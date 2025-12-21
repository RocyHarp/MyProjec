#ifndef TASK_H
#define TASK_H

#include <string>

enum class TaskType {
    COMPUTE,
    SLEEP
};

struct Task {
    int id;
    TaskType type;
    int payload;
};

#endif