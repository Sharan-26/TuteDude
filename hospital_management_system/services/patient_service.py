class PatientService:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def get_patient_ailments(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                return patient.ailments
        return None

    def update_patient_ailments(self, patient_id, new_ailments):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                patient.ailments = new_ailments
                return True
        return False

    def get_all_patients(self):
        return self.patients