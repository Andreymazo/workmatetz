import pytest
from report_generator import calculate_average_rating
import os
import csv

# Файл с недопустимыми данными (например, нечисловые значения)
@pytest.fixture
def invalid_data_file_content():
    return "name,brand,price,rating\napple,apple,a,b"

# Файл, которого нет в системе
@pytest.fixture
def missing_file_path(tmp_path):
    return tmp_path / 'non_existent_file.csv'


# Тест для файла с недопустимыми данными
def test_invalid_data_file(tmp_path, invalid_data_file_content):
    file_path = tmp_path / 'invalid_data.csv'
    with open(file_path, 'w') as f:
        f.write(invalid_data_file_content)
    
    with pytest.raises(ValueError):
        calculate_average_rating([str(file_path)])

# Тест для отсутствующего файла
def test_missing_file(tmp_path, missing_file_path):
    file_paths = [str(tmp_path / 'file1.csv'), str(missing_file_path), str(tmp_path / 'file2.csv')]
    
    with pytest.raises(FileNotFoundError):
        calculate_average_rating(file_paths)

# Дополнительный тест для корректной обработки
def test_valid_files(tmp_path, file_content):
    valid_file_path = tmp_path / 'valid.csv'
    with open(valid_file_path, 'w') as f:
        f.write(file_content)
    
    result = calculate_average_rating([str(valid_file_path)])
    # Добавьте проверку ожидаемых результатов
    assert len(result) > 0

# Пример контент файла для теста корректных данных
@pytest.fixture
def file_content():
    return "name,brand,price,rating\napple,Apple,100,4.5\nbanana,Banana,200,3.8"

# Параметризованный тест
@pytest.mark.parametrize(
  "file_list, expected_output",
    [
        (
            ['file1.csv', 'file2.csv', 'file3.csv'],
            
             [('apple', 4.9), ('google', 4.7), ('samsung', 4.5), ('xiaomi', 4.5),
              ('oneplus', 4.5), ('nokia', 4.4), ('oppo', 4.3), ('realme', 4.25),
               ('motorola', 4.2), ('huawei', 4.15), ('vivo', 4.1)]

        ),
    ]

)
def test_calculate_average_ratings_parametrize(file_list, expected_output):
    actual_output = calculate_average_rating([f"{file}" for file in file_list])
    
    assert actual_output == expected_output


def test_calculate_average_rating():
    # Создаем временные CSV-файлы для тестирования
    file1 = 'file_1.csv'
    file2 = 'file_2.csv'

    with open(file1, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['name', 'brand', 'price', 'rating'])
        writer.writeheader()
        writer.writerow({'name': 'iphone 15 pro', 'brand': 'apple', 'price': '999', 'rating': '4.8'})
        writer.writerow({'name': 'galaxy s23 ultra', 'brand': 'samsung', 'price': '1199', 'rating': '4.7'})
    
    with open(file2, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['name', 'brand', 'price', 'rating'])
        writer.writeheader()
        writer.writerow({'name': 'redmi note 12', 'brand': 'xiaomi', 'price': '199', 'rating': '4.6'})
        writer.writerow({'name': 'pixel 7 pro', 'brand': 'google', 'price': '899', 'rating': '4.9'})

    # Вычисляем средний рейтинг
    average_ratings = calculate_average_rating([file1, file2])

    # Ожидаемые результаты
    expected_result = [
        ('google', 4.9),
        ('apple', 4.8),
        ('samsung', 4.7),
        ('xiaomi', 4.6),
        
    ]

    assert average_ratings == expected_result