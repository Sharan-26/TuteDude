def format_date(date):
    return date.strftime("%Y-%m-%d")

def format_time(time):
    return time.strftime("%H:%M")

def validate_date(date):
    if isinstance(date, datetime.date):
        return True
    return False

def validate_time(time):
    if isinstance(time, datetime.time):
        return True
    return False

def is_double_booking(appointments, new_appointment):
    for appointment in appointments:
        if (appointment.date == new_appointment.date and 
            appointment.time == new_appointment.time and 
            appointment.doctor_id == new_appointment.doctor_id):
            return True
    return False