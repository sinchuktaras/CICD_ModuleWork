def filter_file(input_file, keyword, output_file):
    """
    Зчитує вміст файлу, фільтрує рядки за ключовим словом
    і записує результат у новий файл.
    
    :param input_file: Шлях до вхідного файлу
    :param keyword: Ключове слово для фільтрації
    :param output_file: Шлях до файлу для запису результату
    """
    try:
        with open(input_file, 'r') as infile:
            lines = infile.readlines()
        
        filtered_lines = [line for line in lines if keyword in line]
        
        with open(output_file, 'w') as outfile:
            outfile.writelines(filtered_lines)

        print(f"Фільтрація завершена. Результат збережено в {output_file}.")
    
    except FileNotFoundError:
        print(f"Помилка: Файл {input_file} не знайдено.")
