import csv
import datetime


def get_file_length(file):
    with open(file, 'r') as file:
        return sum(1 for _ in file)


def get_working_days(from_date, add_days):
    business_days_to_add = add_days
    current_date = from_date
    result = {str(current_date): 0}
    while business_days_to_add > 0:
        current_date += datetime.timedelta(days=1)
        weekday = current_date.weekday()
        if weekday >= 5:
            continue
        result[str(current_date)] = 0
        business_days_to_add -= 1
    return result


def get_report(file):

    with open(file, 'r') as f:
        result = {}
        count_rows = get_file_length(file) - 5

        for _ in range(3):
            f.__next__()

        headers = [x.strip() for x in f.readline().split('|')]
        material_i = headers.index('Material')
        description_1 = headers.index('Material Description')
        position_i = headers.index('StorPos.')
        prs_i = headers.index('PRs')

        f.__next__()

        for _ in range(count_rows):
            row = [x.strip() for x in f.readline().split('|')]
            if len(row) == 1:
                break
            material = row[material_i]
            description = row[description_1]
            position = row[position_i]
            prs = row[prs_i]
            result[material] = {'description': description, 'position': position, 'prs': prs, 'stock': 0, 'coverage': 0}
            requirements = get_working_days(datetime.date.today(), 10)
            result[material]['requirements'] = requirements

        result = get_stock('stock.csv', result)
        result = get_requirements('requirements.csv', result)
        result = get_coverage(result)
        write_to_csv(result)


def get_stock(file, collection):

    with open(file, 'r') as f:
        count_rows = get_file_length(file) - 5

        f.__next__()
        headers = [x.strip() for x in f.readline().split('|')]
        material_i = headers.index('Material Number')
        stock_i = headers.index('Unrestricted')
        f.__next__()

        for _ in range(count_rows):
            row = [x.strip() for x in f.readline().split('|')]
            if len(row) == 1:
                break
            material = row[material_i]
            stock = int(row[stock_i].replace(' ', '').split(',')[0])
            collection[material]['stock'] = stock
    return collection


def get_requirements(file, collection):
    with open(file, 'r') as f:
        count_rows = get_file_length(file) - 3

        for _ in range(3):
            f.__next__()

        headers = [x.strip() for x in f.readline().split('|')]
        material_i = headers.index('Material')
        requirement_i = headers.index('Reqmt Qty')
        date_i = headers.index('Reqmt Date')
        f.__next__()
        for _ in range(count_rows):
            row = [x.strip() for x in f.readline().split('|')]
            if len(row) == 1:
                break
            material = row[material_i]
            requirement = int(row[requirement_i].replace(' ', '').split(',')[0])
            day, month, year = row[date_i].split('.')
            current_date = str(datetime.date(int(year), int(month), int(day)))
            collection[material]['requirements'][current_date] += requirement
    return collection


def get_coverage(collection):
    for material, mat_info in collection.items():
        sorted_req = sorted(mat_info['requirements'].items(), key=lambda x: x[0])
        total = sum(mat_info['requirements'].values())
        stock = mat_info['stock']
        if stock >= total or total < 100:
            mat_info['coverage'] = 10
            continue
        for date in sorted_req:
            if stock - date[1] > 0:
                stock -= date[1]
                mat_info['coverage'] += 1
    return collection


def write_to_csv(collection):
    with open('result.csv', 'w', newline='', encoding='UTF-8') as file:
        writer = csv.writer(file)
        headers = ['material', 'description', 'position', 'prs', 'stock', 'coverage']
        writer.writerow(headers)

        for number, material_info in collection.items():
            current_row = [number, material_info['description'], material_info['position'],
                           material_info['prs'], material_info['stock'], material_info['coverage']]
            writer.writerow(current_row)
