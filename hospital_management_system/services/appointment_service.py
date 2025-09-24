class AppointmentService:
    def __init__(self, appointments):
        self.appointments = appointments  # List to store appointments

    def schedule_appointment(self, appointment):
        if self.check_conflict(appointment):
            raise Exception("Appointment conflict detected.")
        self.appointments.append(appointment)  # Add appointment if no conflict

    def check_conflict(self, new_appointment):
        for appointment in self.appointments:
            if (appointment.doctor_id == new_appointment.doctor_id and
                appointment.date == new_appointment.date and
                appointment.time == new_appointment.time):
                return True  # Conflict found
        return False  # No conflict

    def get_appointments_by_doctor(self, doctor_id):
        return [appointment for appointment in self.appointments if appointment.doctor_id == doctor_id]

    def get_appointments_by_patient(self, patient_id):
        return [appointment for appointment in self.appointments if appointment.patient_id == patient_id]