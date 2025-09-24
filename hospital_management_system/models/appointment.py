class Appointment:
    def __init__(self, appointment_id, doctor_id, patient_id, date, time):
        self.appointment_id = appointment_id
        self.doctor_id = doctor_id
        self.patient_id = patient_id
        self.date = date
        self.time = time

    def conflicts_with(self, other):
        return self.doctor_id == other.doctor_id and self.date == other.date and self.time == other.time

    def get_details(self):
        return {
            "appointment_id": self.appointment_id,
            "doctor_id": self.doctor_id,
            "patient_id": self.patient_id,
            "date": self.date,
            "time": self.time
        }
        
# Example usage:
if __name__ == "__main__":
    appt1 = Appointment(1, 101, 201, "2024-07-01", "10:00")
    appt2 = Appointment(2, 101, 202, "2024-07-01", "10:00")
    appt3 = Appointment(3, 102, 203, "2024-07-01", "11:00")

    print(appt1.get_details())
    print("Conflict between appt1 and appt2:", appt1.conflicts_with(appt2))  # Should be True
    print("Conflict between appt1 and appt3:", appt1.conflicts_with(appt3))  # Should be False
    
    print(appt2.get_details())
    print(appt3.get_details())
    