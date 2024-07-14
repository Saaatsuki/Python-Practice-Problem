import csv
from prettytable import PrettyTable

districts = {}

with open('2024_std_num_high_school.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    # Check the column names
    column_names = reader.fieldnames
    print("Column names:", column_names)  # This will print the column names for verification

    for row in reader:
        if row["제외여부"] == "N":
            district = row['시도교육청']  # Make sure this column name exists in the CSV file
            if district not in districts:
                districts[district] = {
                    '1학년(남)': 0, '1학년(여)': 0,
                    '2학년(남)': 0, '2학년(여)': 0,
                    '3학년(남)': 0, '3학년(여)': 0,
                    '1학년 전채 학생 수': 0, '2학년 전채 학생 수': 0, '3학년 전채 학생 수': 0,
                    '전채 학생 수': 0
                }
            districts[district]['1학년(남)'] += int(row['1학년(남)'])
            districts[district]['1학년(여)'] += int(row['1학년(여)'])
            districts[district]['2학년(남)'] += int(row['2학년(남)'])
            districts[district]['2학년(여)'] += int(row['2학년(여)'])
            districts[district]['3학년(남)'] += int(row['3학년(남)'])
            districts[district]['3학년(여)'] += int(row['3학년(여)'])

    for district, data in districts.items():
        data['1학년 전채 학생 수'] = data['1학년(남)'] + data['1학년(여)']
        data['2학년 전채 학생 수'] = data['2학년(남)'] + data['2학년(여)']
        data['3학년 전채 학생 수'] = data['3학년(남)'] + data['3학년(여)']
        data['전채 학생 수'] = data['1학년 전채 학생 수'] + data['2학년 전채 학생 수'] + data['3학년 전채 학생 수']    

        if data['1학년 전채 학생 수'] != 0:
            data['1학년 남자 비율'] = data['1학년(남)'] / data['1학년 전채 학생 수'] * 100
            data['1학년 여자 비율'] = data['1학년(여)'] / data['1학년 전채 학생 수'] * 100
        else:
            data['1학년 남자 비율'] = data['1학년 여자 비율'] = 0

        if data['2학년 전채 학생 수'] != 0:
            data['2학년 남자 비율'] = data['2학년(남)'] / data['2학년 전채 학생 수'] * 100
            data['2학년 여자 비율'] = data['2학년(여)'] / data['2학년 전채 학생 수'] * 100
        else:
            data['2학년 남자 비율'] = data['2학년 여자 비율'] = 0

        if data['3학년 전채 학생 수'] != 0:
            data['3학년 남자 비율'] = data['3학년(남)'] / data['3학년 전채 학생 수'] * 100
            data['3학년 여자 비율'] = data['3학년(여)'] / data['3학년 전채 학생 수'] * 100
        else:
            data['3학년 남자 비율'] = data['3학년 여자 비율'] = 0

            
    table = PrettyTable()
    table.field_names = [
        '지역', '전채 학생 수',
        '1학년 전채 학생 수', '1학년(남)', '1학년(여)', '1학년 남자 비율', '1학년 여자 비율',
        '2학년 전채 학생 수', '2학년(남)', '2학년(여)', '2학년 남자 비율', '2학년 여자 비율',
        '3학년 전채 학생 수', '3학년(남)', '3학년(여)', '3학년 남자 비율', '3학년 여자 비율'
    ]

    for district, data in sorted(districts.items(), key=lambda x: x[1]['전채 학생 수'], reverse=True)[:5]:
        table.add_row([
            district,
            f"{data['전채 학생 수']:,} 명",
            f"{data['1학년 전채 학생 수']:,} 명", f"{data['1학년(남)']:3d} 명", f"{data['1학년(여)']:3d} 명", f"{data['1학년 남자 비율']:.2f} %", f"{data['1학년 여자 비율']:.2f} %",
            f"{data['2학년 전채 학생 수']:,} 명", f"{data['2학년(남)']:3d} 명", f"{data['2학년(여)']:3d} 명", f"{data['2학년 남자 비율']:.2f} %", f"{data['2학년 여자 비율']:.2f} %",
            f"{data['3학년 전채 학생 수']:,} 명", f"{data['3학년(남)']:3d} 명", f"{data['3학년(여)']:3d} 명", f"{data['3학년 남자 비율']:.2f} %", f"{data['3학년 여자 비율']:.2f} %"
        ])

print(table)
