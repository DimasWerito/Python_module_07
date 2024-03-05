"""
Напишіть функцію to_indexed(source_file, output_file), 
яка зчитуватиме вміст файлу, додаватиме до прочитаних рядків порядковий номер 
і зберігати їх у такому вигляді у новому файлі.

Кожний рядок у створеному файлі повинен починатися з його номера, 
двокрапки та пробілу, після чого має йти текст рядка з вхідного файлу.

Нумерація рядків іде від 0.
"""


def to_indexed(source_file, output_file):
    with open(source_file, "r") as f:
        lines = f.readlines()
    with open(output_file, "w") as f:
        counter = 0
        for line in lines:
            new_line = f"{counter}: {line}"
            f.write(new_line)
            counter += 1