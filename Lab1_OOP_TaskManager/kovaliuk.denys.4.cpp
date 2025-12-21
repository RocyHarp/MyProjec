#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

struct Task {
    string title;
    string dueDate;
    bool completed = false;
};

class TaskEvent {
public:
    string title;
    string dueDate;
    string type;

    TaskEvent(string type, string title = "", string dueDate = "")
        : type(type), title(title), dueDate(dueDate) {}
};

class ITaskEventListener {
public:
    virtual void OnTaskAdded(const TaskEvent& e) = 0;
    virtual void OnTaskCompleted(const TaskEvent& e) = 0;
    virtual void OnTaskDeleted(const TaskEvent& e) = 0;
    virtual void OnTaskListRequested() = 0;
    virtual ~ITaskEventListener() = default;
};

class EventBus {
private:
    vector<ITaskEventListener*> listeners;

public:
    void Subscribe(ITaskEventListener* listener) {
        listeners.push_back(listener);
    }

    void RaiseTaskAdded(const TaskEvent& e) {
        for (auto l : listeners) l->OnTaskAdded(e);
    }

    void RaiseTaskCompleted(const TaskEvent& e) {
        for (auto l : listeners) l->OnTaskCompleted(e);
    }

    void RaiseTaskDeleted(const TaskEvent& e) {
        for (auto l : listeners) l->OnTaskDeleted(e);
    }

    void RaiseTaskListRequested() {
        for (auto l : listeners) l->OnTaskListRequested();
    }
};

class TaskManager : public ITaskEventListener {
private:
    vector<Task> tasks;

public:
    void OnTaskAdded(const TaskEvent& e) override {
        tasks.push_back({e.title, e.dueDate, false});
        cout << "Завдання додано: " << e.title << "\n";
    }

    void OnTaskCompleted(const TaskEvent& e) override {
        for (auto& t : tasks) {
            if (t.title == e.title) {
                t.completed = true;
                cout << "Завдання виконано: " << t.title << "\n\n";
                return;
            }
        }
        cout << "Завдання не знайдено!\n\n";
    }

    void OnTaskDeleted(const TaskEvent& e) override {
        auto before = tasks.size();
        tasks.erase(remove_if(tasks.begin(), tasks.end(), [&](const Task& t) {
            return t.title == e.title;
        }), tasks.end());

        if (tasks.size() < before)
            cout << "Завдання видалено: " << e.title << "\n\n";
        else
            cout << "Завдання не знайдено!\n\n";
    }

    void OnTaskListRequested() override {
        cout << "\n====== Список завдань ======\n";
        if (tasks.empty()) {
            cout << "(порожньо)\n";
        } else {
            for (const auto& t : tasks) {
                cout << "- " << t.title
                     << " | До: " << t.dueDate
                     << " | Статус: " << (t.completed ? "Виконано" : "Не виконано")
                     << "\n";
            }
        }
        cout << "============================\n\n";
    }
};

int main() {
    EventBus bus;
    TaskManager manager;
    bus.Subscribe(&manager);

    bus.RaiseTaskAdded(TaskEvent("TaskAdded", "Зробити ООП", "2025-12-05"));
    bus.RaiseTaskAdded(TaskEvent("TaskAdded", "Поприбирати ", "2025-12-06"));

    while (true) {
        cout << "Меню\n";
        cout << "1. Додати завдання\n";
        cout << "2. Виконати завдання\n";
        cout << "3. Видалити завдання\n";
        cout << "4. Показати список\n";
        cout << "5. Вийти\n";
        cout << "Ваш вибір: ";

        int choice;
        cin >> choice;
        cin.ignore();

        if (choice == 1) {
            string title, date;
            cout << "Назва: ";
            getline(cin, title);
            cout << "Термін (YYYY-MM-DD): ";
            getline(cin, date);

            bus.RaiseTaskAdded(TaskEvent("TaskAdded", title, date));
        }
        else if (choice == 2) {
            string title;
            cout << "Назва завдання для виконання: ";
            getline(cin, title);

            bus.RaiseTaskCompleted(TaskEvent("TaskCompleted", title));
        }
        else if (choice == 3) {
            string title;
            cout << "Назва завдання для видалення: ";
            getline(cin, title);

            bus.RaiseTaskDeleted(TaskEvent("TaskDeleted", title));
        }
        else if (choice == 4) {
            bus.RaiseTaskListRequested();
        }
        else if (choice == 5) {
            cout << "Вихід...\n";
            break;
        }
        else {
            cout << "Невірний вибір!\n\n";
        }
    }

    return 0;
}
