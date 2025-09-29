class Patient:
    def __init__(self, patient_id, name, age, ailments):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.ailments = ailments

    def get_details(self):
        return {
            "patient_id": self.patient_id,
            "name": self.name,
            "age": self.age,
            "ailments": self.ailments
        }

    def update_ailments(self, new_ailments):
        self.ailments = new_ailments
        
        
# Example usage:
if __name__ == "__main__":
    patient = Patient(201, "John Doe", 30, ["Flu", "Cold"])
    print(patient.get_details())
    patient.update_ailments(["Flu", "Cold", "Allergy"])
    print("Updated ailments:", patient.get_details())

    # Example appointments and doctor object for demonstration
    appointments = []
    # doc = Doctor(...)  # You need to define a Doctor class and create an instance

    # Uncomment and define 'doc' and 'Doctor' class to use these lines:
    # print("Is available on 2024-07-02 at 10:00:", doc.is_available(appointments, "2024-07-02", "10:00"))  # Should be True
    # print("Is available on 2024-07-01 at 11:00:", doc.is_available(appointments, "2024-07-01", "11:00"))  # Should be True