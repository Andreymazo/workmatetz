import os
import csv
from collections import defaultdict
from tabulate import tabulate
import pytest
from report_generator import calculate_average_rating, main
from unittest.mock import patch, MagicMock, call
from argparse import Namespace 
import re


# >>> thing = ProductionClass()
# >>> thing.method = MagicMock(return_value=3)
# >>> thing.method(3, 4, 5, key='value')
# 3
# >>> thing.method.assert_called_with(3, 4, 5, key='value')

def test_calculate_average_rating():
    # Создаем временные CSV-файлы для тестирования
    file1 = 'file1.csv'
    file2 = 'file2.csv'
    file3 = 'file3.csv'

    with open(file1, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['name', 'brand', 'price', 'rating'])
        writer.writeheader()
        writer.writerow({'name': 'iphone 15 pro', 'brand': 'apple', 'price': '999', 'rating': '4.8'})
    
    with open(file2, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['name', 'brand', 'price', 'rating'])
        writer.writeheader()
        writer.writerow({'name': 'redmi note 12', 'brand': 'xiaomi', 'price': '199', 'rating': '4.6'})

    with open(file3, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['name', 'brand', 'price', 'rating'])
        writer.writeheader()
        writer.writerow({'name': 'pixel 7 pro', 'brand': 'google', 'price': '899', 'rating': '4.9'})

    # Вычисляем средний рейтинг
    average_ratings = calculate_average_rating([file1, file2, file3])

    # Ожидаемые результаты
    expected_result = [('google', 4.9), ('apple', 4.8), ('xiaomi', 4.6)]
   
    print('average_ratings============== average_ratings',average_ratings)
    assert average_ratings == expected_result


def test_main_exit():
    from unittest.mock import patch
    with patch('sys.argv', [__file__, '--files', 'nonexistent.csv', '--report', 'output.txt']):
        with pytest.raises(FileNotFoundError):
            main()

if __name__ == '__main__':
    pytest.main()
