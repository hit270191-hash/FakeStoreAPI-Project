from datetime import datetime


def validate_cart_dates_within_range(cart_dates, start_date, end_date):
    fmt = '%Y-%m-%d'
    start_date = datetime.strptime(start_date, fmt)
    end_date = datetime.strptime(end_date, fmt)
    for cart_date in cart_dates:
        dt= datetime.strptime(cart_date[:10], fmt)
        if not (start_date<=dt<=end_date):
            return False
    return True