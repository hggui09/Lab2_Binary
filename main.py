import urllib.request
from binary_re import find_binary, find_binary_strict, to_decimal

print('--- Анализатор логов ЧПУ ---')
print('1. Ввод текста | 2. Из файла | 3. По URL')
choice = input('Выберите источник (1/2/3): ').strip()
is_strict = input('/Строгий поиск (только 0b...)? (да/нет): ').strip().lower() == 'да'

text = ""

if choice == '1':
    text = input('Введите текст: ')
elif choice == '2':
    filepath = input('Путь к файлу: ')
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
elif choice == '3':
    url = input('Введите URL: ')
    with urllib.request.urlopen(url) as response:
        text = response.read().decode('utf-8')
else:
    print('Неверный выбор.')
    exit()

results = find_binary_strict(text) if is_strict else find_binary(text)

print(f'\nНайдено совпадений: {len(results)}')
for b in results:
    try:
        print(f'{b} -> в десятичной: {to_decimal(b)}')
    except ValueError:
        print(f'{b} -> ошибка конвертации')