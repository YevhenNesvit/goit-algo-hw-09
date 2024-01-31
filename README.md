# Завдання з порівняння ефективності алгоритмів видавання решти

У цьому проекті ми порівняємо ефективність жадібного алгоритму та алгоритму динамічного програмування для задачі видавання решти покупцеві.

## Результати експериментів

| Алгоритм | Час для малої суми | Час для середньої суми | Час для великої суми |
| --------- | ------------------ | ---------------------- | -------------------- |
| Greedy    | 0.00002 сек       | 0.00001 сек            | 0.00001 сек          |
| Dynamic   | 0.00002 сек       | 0.00006 сек            | 0.00054 сек          |

## Висновки

На основі результатів експериментів можна зробити наступні висновки:

- **Час виконання:**

Для невеликих і середніх сум вхідних значень обидва алгоритми (жадібний і динамічний) показують ефективність, виконуючи операції миттєво (час виконання порядку 0.00001-0.00006 секунд).
Динамічний алгоритм може виявити зростання часу виконання при обробці великих сум (більше 0.0005 секунди), що може бути пов'язано зі зростанням обчислювальних витрат при великих обсягах даних.

- **Ефективність:**

Алгоритм жадібного вибору виявляється дуже ефективним для швидкого вирішення проблеми знаходження мінімальної кількості монет для невеликих і середніх сум.
Динамічний алгоритм надає оптимальне рішення, але може виявити збільшення часу виконання при обробці великих сум.

- **Рекомендації:**

*Жадібний алгоритм* може бути перевагою для швидкого вирішення проблем знайдення мінімальної кількості монет для невеликих сум.
*Динамічний алгоритм* підходить для ситуацій, коли потрібно гарантувати оптимальність рішення, навіть за рахунок трошки більшого часу виконання.

Загалом, вибір між алгоритмами повинен залежати від конкретних вимог проекту та характеристик вхідних даних. З урахуванням наданих даних, жадібний алгоритм виявився швидшим, але слід ураховувати індивідуальні особливості завдань та обмежень. 