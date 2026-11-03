"""Модуль проверяет является ли текст двоичным числом."""

import re

BINARY_PATTERN = (r"(?<!\w)"  # слева нет цифры, буквы или знака подчеркивания
                  r"(?<!\d\.)"  # не дробная часть 
                  r"(?:"  # начало группы с двумя альтернативными вариантами
                  r"0[bB](?:_?[01])+"  # после префикса нужна мин 1 цифра, а _ допускается только перед цифрой  
                  r"|[01](?:_?[01])*)"  # альтернативная проверка без префикса
                  r"(?!\w)"  # справа нет цифры, буквы или знака подчеркивания
                  r"(?!\.\d)")  # не целая часть дроби

def is_binary(user_text):
    match = re.fullmatch(BINARY_PATTERN, user_text)  # проверка регулярным выражением
    return match is not None  # возвращаем только если двоичное


def find_binary(text):
    return re.findall(BINARY_PATTERN, text)

def to_decimal(binary: str) -> int:
    if not is_binary(binary):  # своя проверка чтоб не было пробелов и знаков
        raise ValueError(f'"{binary}" не является двоичным числом')
    return int(binary, 2)





