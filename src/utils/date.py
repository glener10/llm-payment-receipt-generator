from datetime import datetime


def get_formatted_date_for_nu(date: str) -> str:
    months_pt = [
        "JAN",
        "FEV",
        "MAR",
        "ABR",
        "MAI",
        "JUN",
        "JUL",
        "AGO",
        "SET",
        "OUT",
        "NOV",
        "DEZ",
    ]
    dt = datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
    day = dt.strftime("%d")
    month = months_pt[dt.month - 1]
    year = dt.strftime("%Y")
    time = dt.strftime("%H:%M:%S")
    return f"{day} {month} {year} - {time}"
