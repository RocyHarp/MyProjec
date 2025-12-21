import torch
import torch.nn as nn
import torch.optim as optim


X = torch.rand(2000, 2) * 20 - 10  
ops = torch.randint(0, 2, (2000, 1)).float()
inputs = torch.cat([X, ops], dim=1)

y = torch.zeros(2000, 1)
for i in range(2000):
    if ops[i] == 1:
        y[i] = X[i, 0] + X[i, 1]
    else:
        y[i] = X[i, 0] - X[i, 1]

# === 2. Ділимо на навчальні та тестові ===
train_X, test_X = inputs[:1600], inputs[1600:]
train_y, test_y = y[:1600], y[1600:]

# === 3. Створюємо більшу нейромережу ===
class MathNet(nn.Module):
    def __init__(self):
        super(MathNet, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(3, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, 8),
            nn.ReLU(),
            nn.Linear(8, 1)
        )

    def forward(self, x):
        return self.net(x)

model = MathNet()

# === 4. Визначаємо функцію втрат і оптимізатор ===
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# === 5. Навчання (збільшено кількість епох) ===
epochs = 2000
for epoch in range(epochs):
    outputs = model(train_X)
    loss = criterion(outputs, train_y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 200 == 0:
        print(f"Епоха [{epoch + 1}/{epochs}], Втрата: {loss.item():.6f}")

# === 6. Збереження моделі ===
torch.save(model.state_dict(), "math_model.pth")
print("✅ Модель збережено у 'math_model.pth'")

# === 7. Завантаження моделі ===
loaded_model = MathNet()
loaded_model.load_state_dict(torch.load("math_model.pth"))
loaded_model.eval()

# === 8. Тестування на випадкових прикладах ===
print("\nТест на випадкових прикладах:")
random_X = torch.rand(5, 2) * 20 - 10
random_ops = torch.randint(0, 2, (5, 1)).float()
random_inputs = torch.cat([random_X, random_ops], dim=1)
random_pred = loaded_model(random_inputs).detach()

for i in range(len(random_inputs)):
    a, b, op = random_inputs[i]
    op_int = int(op.item())
    real = a + b if op_int == 1 else a - b
    op_str = '+' if op_int == 1 else '-'
    print(f"{a:.2f} {op_str} {b:.2f} = Реально: {real:.2f}, Модель ≈ {random_pred[i].item():.2f}")

# === 9. Ввід користувача ===
print("\nТепер ти можеш перевірити модель:")
while True:
    try:
        a = float(input("Введи перше число: "))
        b = float(input("Введи друге число: "))
        op = input("Оберіть дію (+ або -): ").strip()

        if op == "+":
            op_val = 1.0
        elif op == "-":
            op_val = 0.0
        else:
            print("❌ Невідома дія, введи '+' або '-'")
            continue

        x = torch.tensor([[a, b, op_val]])
        pred = loaded_model(x).item()

        real = a + b if op_val == 1.0 else a - b
        print(f"Реальний результат: {real:.2f}, модель передбачила ≈ {pred:.2f}")
    except KeyboardInterrupt:
        print("\n🚪 Вихід із програми.")
        break
    except Exception as e:
        print("⚠️ Помилка:", e)