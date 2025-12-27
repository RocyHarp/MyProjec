****# Denis Kovalyuk Portfolio Projects / Портфоліо Дениса Ковалюка

Цей репозиторій містить декілька проектів на Python та C++, які демонструють мої навички в програмуванні, ООП, асинхронності та GUI.

---

## 🇺🇦 Українська

### 1. Ai.py — Нейромережа для математичних операцій
	- Проста нейромережа на PyTorch, яка вчиться виконувати **додавання та віднімання** двох чисел.
	- Генерує випадкові дані, тренує модель і дозволяє користувачеві вводити власні числа.

**Приклад роботи:**
plaintext
Введіть перше число: 4
Введіть друге число: 7
Оберіть дію (+ або -): +
Реальний результат: 11.00, модель передбачила ≈ 10.98

### 2. AsyncTaskPlatform — Асинхронна платформа задач
	•	REST API на FastAPI для створення та перегляду задач.
	•	Воркери для асинхронної обробки задач у фоновому режимі.
	•	Збереження задач у SQLite.
	•	Модульна архітектура.

Приклад роботи:
POST /tasks {"name": "Написати документацію"} → {"status": "created"}
GET /tasks → [{"id": 1, "name": "Написати документацію", "status": "pending"}]
Worker console:
Processing task: Написати документацію
Swagger UI: http://127.0.0.1:8000/docs
### 3. Lab1_OOP_TaskManager (C++) — Менеджер завдань
	•	Консольний додаток на C++ з EventBus і TaskManager.
	•	Додавання, виконання, видалення задач, перегляд списку задач із статусом.

Приклад роботи:
Меню
1. Додати завдання
2. Виконати завдання
3. Видалити завдання
4. Показати список
5. Вийти
Ваш вибір: 1
Назва: Купити продукти
Термін: 2025-12-22
Завдання додано: Купити продукти
###4. Lab_3_Tkinter — Графічний тест для студентів
	•	GUI на Tkinter для проходження тесту.
	•	Питання з RadioButton, Checkbutton та Entry.
	•	Підрахунок балів і вивід результату.

Приклад роботи:
Введіть прізвище: Ковалюк
Введіть групу: 4
Відправити результат → Повідомлення: "Ковалюк (4) набрав(ла) 10 балів із 10."
Кнопка Очистити → скидає відповіді

### 5. TaskServer (C++) — Консольний Task Server
	•	Багатопотоковий менеджер задач.
	•	ThreadPool для паралельного виконання задач.
	•	Логування через Logger.
	•	Модульна архітектура.

Приклад роботи:
Menu
1. Add task
2. Complete task
3. Delete task
4. Show task list
5. Exit

Added task: Do OOP
Processing task: Do OOP
Task completed: Do OOP
### 6. Instagram AI Auto-Poster — Бот для автопостингу

* **ШІ-генерація:** Використовує `Google Gemini 1.5 Flash` для створення унікальних описів англійською мовою з хештегами.
* **Авто-контент:** Завантажує випадкові високоякісні фото з сервісу Picsum.
* **Безпека:** Використовує змінні середовища (`.env`) для захисту ключів API.
* **Розумна авторизація:** Вхід через `Session ID` (без пароля) та збереження сесії для уникнення блокувань.

### 🛠️ Встановлення

1.  **Клонуйте репозиторій:**
    ```bash
    git clone [https://github.com/yourusername/insta-ai-bot.git](https://github.com/yourusername/insta-ai-bot.git)
    cd insta-ai-bot
    ```

2.  **Встановіть залежності:**
    ```bash
    pip install -r requirements.txt
    ```

### ⚙️ Налаштування

1.  Створіть файл `.env` у кореневій папці проєкту.
2.  Додайте туди ваші дані (без пробілів біля `=`):

    ```ini
    GEMINI_API_KEY=Ваш_Ключ_Gemini
    INSTA_SESSION_ID=Ваш_Instagram_Session_ID
    ```

> **Як отримати Session ID?**
> 1. Зайдіть в Instagram через браузер (Chrome/Edge).
> 2. Натисніть `F12` -> вкладка `Application` -> зліва `Cookies` -> `https://www.instagram.com`.
> 3. Знайдіть рядок `sessionid` і скопіюйте його значення (`Value`).

🚀 Запуск
python main.py

Цей код створено виключно для освітніх цілей. Використання ботів може порушувати правила спільноти Instagram.
Автор не несе відповідальності за можливе блокування акаунту.



### 🇬🇧 English

### 1. Ai.py — Neural Network for Math Operations
	•	A simple PyTorch neural network that learns addition and subtraction of two numbers.
	•	Generates random data, trains the model, and allows user input.

Example:
Enter first number: 4
Enter second number: 7
Choose operation (+ or -): +
Real result: 11.00, predicted by model ≈ 10.98

### 2. AsyncTaskPlatform — Async Task Platform
	•	FastAPI REST API for creating and retrieving tasks.
	•	Background workers for asynchronous task processing.
	•	SQLite database storage.
	•	Modular architecture.

Example:
POST /tasks {"name": "Write documentation"} → {"status": "created"}
GET /tasks → [{"id": 1, "name": "Write documentation", "status": "pending"}]
Worker console:
Processing task: Write documentation

Swagger UI: http://127.0.0.1:8000/docs


### 3. Lab1_OOP_TaskManager (C++) — Task Manager
	•	Console application with EventBus and TaskManager.
	•	Add, complete, delete tasks and view task list with status.

Example:
Menu
1. Add task
2. Complete task
3. Delete task
4. Show task list
5. Exit
Choice: 1
Title: Buy groceries
Due date: 2025-12-22
Task added: Buy groceries

### 4. Lab_3_Tkinter — Student Test GUI
	•	GUI using Tkinter for taking tests.
	•	Questions with RadioButton, Checkbutton, Entry.
	•	Calculates score and displays result.

Example:
Enter surname: Kovalyuk
Enter group: 4
Submit → Message: "Kovalyuk (4) scored 10/10."
Clear → Resets all answers

### 5. TaskServer (C++) — Multithreaded Task Server
	•	ThreadPool for parallel task execution.
	•	Logging via Logger.
	•	Modular architecture.

Example:
Menu
1. Add task
2. Complete task
3. Delete task
4. Show task list
5. Exit

Added task: Do OOP
Processing task: Do OOP
Task completed: Do OOP

6. Instagram AI Auto-Poster — Automation Bot

Python script for fully automating an Instagram account.

Integration with Google Gemini AI to generate creative captions and hashtags.

Uses Instagrapi to interact with Instagram's private API (via Session ID).

Automatic fetching of aesthetic images and processing with Pillow.

Secure credential management using environment variables (.env).


Example:
🚀 STARTING BOT...
✅ Success: Logged in as @user_name
🤖 Gemini is writing a caption...
📝 Generated: "Golden hour magic ✨ #sunset #vibes"
📸 Downloading photo...
📤 Posting...
🎉 Done! Post published. ID: 3265...
⚠️ Disclaimer

This project is for educational purposes only. Using automated bots may violate Instagram's Terms of Service. 
The author is not responsible for any account bans or restrictions.

💡 Tip:
	•	Tkinter and TaskServer demonstrate GUI and multithreading skills.
	•	Ai.py and AsyncTaskPlatform show Python ML and async backend experience.
	•	Lab1_OOP_TaskManager demonstrates OOP in C++.
  
