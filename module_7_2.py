def custom_write(file_name, strings):
    strings_positions = {}
    str_num = 1
    file = open(file_name, 'w',encoding= 'utf-8')
    for string in strings:
        line_byte = file.tell()
        file.write(f'{string}\n')
        strings_positions[(str_num, line_byte)] = string
        str_num += 1
    file.close()
    return strings_positions

if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
        ]
    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)