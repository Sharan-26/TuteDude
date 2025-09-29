class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization

    def get_details(self):
        return {
            "doctor_id": self.doctor_id,
            "name": self.name,
            "specialization": self.specialization
        }

    def is_available(self, appointments, date, time):
        for appointment in appointments:
            if appointment.doctor_id == self.doctor_id and appointment.date == date and appointment.time == time:
                return False
        return True
    
# Example usage:
if __name__ == "__main__":
    doc = Doctor(101, "Dr. Smith", "Cardiology")
    print(doc.get_details())
    appointments = [
        {"doctor_id": 101, "date": "2024-07-01", "time": "10:00"},
        {"doctor_id": 102, "date": "2024-07-01", "time": "11:00"}
    ]
    print("Is available on 2024-07-01 at 10:00:", doc.is_available(appointments, "2024-07-01", "10:00"))  # Should be False
    print("Is available on 2024-07-01 at 12:00:", doc.is_available(appointments, "2024-07-01", "12:00"))  # Should be True
    
    
    print("Is available on 2024-07-02 at 10:00:", doc.is_available(appointments, "2024-07-02", "10:00"))  # Should be True  
    print("Is available on 2024-07-01 at 11:00:", doc.is_available(appointments, "2024-07-01", "11:00"))  # Should be True
    print("Is available on 2024-07-01 at 09:00:", doc.is_available(appointments, "2024-07-01", "09:00"))  # Should be True
    print("Is available on 2024-07-01 at 10:30:", doc.is_available(appointments, "2024-07-01", "10:30"))  # Should be True
    