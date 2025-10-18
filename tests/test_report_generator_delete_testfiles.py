import os
import csv
import pytest
from report_generator import calculate_average_rating, main
import argparse

def test_calculate_average_rating():
    # Создаем временные CSV-файлы для тестирования
    file1 = 'file1.csv'
    file2 = 'file2.csv'

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
    expected_result = [('google', 4.9), ('apple', 4.8), ('samsung', 4.7), ('xiaomi', 4.6)]
    
    assert average_ratings == expected_result


# Удаление тестовых файлов после завершения тестирования
def teardown():
    files_to_remove = ['file1.csv', 'file2.csv']
    for file in files_to_remove:
        if os.path.exists(file):
            os.remove(file)
            

if __name__ == '__main__':
    pytest.main()
