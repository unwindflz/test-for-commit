import datetime


def generate_date_report(start_date, end_date):
    """Generates a report of dates between the start and end dates."""
    report = []
    current_date = start_date
    while current_date <= end_date:
        report.append(current_date.strftime('%Y-%m-%d'))
        current_date += datetime.timedelta(days=1)
    return report


def main():
    """Main function to execute the report generation."""
    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2023, 1, 10)
    report = generate_date_report(start_date, end_date)
    print("Generated Date Report:")
    for date in report:
        print(date)


if __name__ == '__main__':
    main()