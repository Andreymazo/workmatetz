import argparse
import csv
from collections import defaultdict
from tabulate import tabulate

def calculate_average_rating(file_paths):
    brand_ratings = defaultdict(list)
    
    for file_path in file_paths:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                brand_ratings[row['brand']].append(float(row['rating']))

    average_ratings = {brand: sum(ratings) / len(ratings) for brand, ratings in brand_ratings.items()}
    print("88888888888888888888", sorted(average_ratings.items(), key=lambda x: x[1], reverse=True))
    return sorted(average_ratings.items(), key=lambda x: x[1], reverse=True)

def main():
    parser = argparse.ArgumentParser(description='Generate an average rating report.')
    parser.add_argument('--files', nargs='+', required=True, help='Paths to CSV files')
    parser.add_argument('--report', required=True, help='Name of the report file (not used for output)')
    
    args = parser.parse_args()
    
    # Calculate average ratings
    average_ratings = calculate_average_rating(args.files)
    
    # Print the report using tabulate
    headers = ['Brand', 'Average Rating']
    table_data = [[brand, round(rating, 2)] for brand, rating in average_ratings]
    print(tabulate(table_data, headers=headers, tablefmt='grid'))

if __name__ == '__main__':
    main()