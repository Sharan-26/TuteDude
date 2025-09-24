class DoctorService:
    def __init__(self):
        self.doctors = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def get_specialization(self, doctor_id):
        for doctor in self.doctors:
            if doctor.doctor_id == doctor_id:
                return doctor.specialization
        return None

    def check_availability(self, doctor_id, appointments):
        for appointment in appointments:
            if appointment.doctor_id == doctor_id:
                return False
        return True

    def get_doctor_details(self, doctor_id):
        for doctor in self.doctors:
            if doctor.doctor_id == doctor_id:
                return {
                    "id": doctor.doctor_id,
                    "name": doctor.name,
                    "specialization": doctor.specialization
                }
        return None