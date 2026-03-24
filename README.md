# Python Exam

**Загальний бал: 75 (65 основних + 10 бонусних)**

## Структура

```
src/
├── task_01.py      ← Типи, цикли, умови            (15 балів)
├── task_02.py      ← Функції + рядки               (10 балів)
├── task_03.py      ← Структури даних, comprehension (20 балів)
├── task_04.py      ← ООП: Stack, Shape, Temperature (20 балів)
├── task_05.py      ← Генератор простих + декоратор retry (10 балів)
└── task_bonus.py   ← TextAnalyzer — всі теми разом (+10 балів)
tests/
├── test_task_01.py
├── test_task_02.py
├── test_task_03.py
├── test_task_04.py
├── test_task_05.py
└── test_task_bonus.py
```

## Як отримати завдання (Fork)

1. Відкрий репозиторій на GitHub
2. Натисни кнопку **Fork** (вгорі праворуч) — це створить копію репо на твоєму акаунті
3. Клонуй свій форк локально:
   ```bash
   git clone https://github.com/<твій-юзернейм>/<назва-репо>.git
   cd <назва-репо>
   ```
4. Встанови залежності:
   ```bash
   pip install -r requirements.txt
   ```
5. Після виконання завдань зроби commit і push:
   ```bash
   git add .
   git commit -m "done"
   git push
   ```

## Запуск тестів

### Усі тести
```bash
python -m pytest tests/ -v
```

### Тільки один файл
```bash
python -m pytest tests/test_task_01.py -v
```

### Тільки один клас тестів
```bash
python -m pytest tests/test_task_01.py::TestFizzBuzz -v
```

### Тільки одна функція
```bash
python -m pytest tests/test_task_01.py::TestFizzBuzz::test_basic -v
```

## Чи можна використовувати print()?

Так, `print()` працює у твоїх функціях — але pytest **приховує** вивід за замовчуванням.
Щоб побачити його, додай прапор `-s`:

```bash
python -m pytest tests/test_task_01.py -v -s
```

Вивід `print()` з'явиться в терміналі прямо під відповідним тестом.

> Порада: `print()` зручний для дебагу, але прибери його з фінального коду — це зайвий шум.

## Правила

- Реалізуйте лише функції/класи позначені `# TODO`
- Не змінюйте сигнатури функцій і назви класів
- Бонусне завдання виконується після основних
