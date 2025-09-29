import datetime
class HospitalManagementSystem:
    def __init__(self, doctors,patients,appointments):
        self.doctors = [] # List to store doctors
        self.patients = []
        self.appointments = []
        
    def Doc_specialization(self,doctor_id):
        for doctor in self.doctors: # Iterate through doctors to find specialization
            if doctor.doctor_id == doctor_id: 
                return doctor.specialization 
        return None # Return None if doctor not found

    def Patient_ailments(self,patient_id):
        for patient in self.patients: # Iterate through patients to find ailments
            if patient.patient_id ==patient_id:
                return patient.ailments 
        return None # Return None if patient not found

    def Appointment(self,doctor_id = None, patient_id = None, date = None):
        results = []
        for appointment in self.appointments:
            if(doctor_id and appointment.doctor_id == doctor_id) or (patient_id and appointment.patient_id == patient_id): # Match based on doctor_id or patient_id
                results.append(appointment) # Add matching appointment to results
        return results # Return list of matching appointments
    
class Doctor:
    def __init__(self,doctor_id,name,specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        
class Patient:
    def __init__(self,patient_id,name,age,ailments):
        self.patient_id = []
        self.name = []
        self.age = []
        self.ailments = []
        
class Appointment:
    def __init__(self,appointment_id,doctor_id,patient_id,date,time):
        self.appointment_id = appointment_id
        self.doctor_id = doctor_id
        self.patient_id = patient_id
        self.date = date
        self.time = time
        

# Example usage
hospital = HospitalManagementSystem([],[],[]) # Initialize empty hospital system
doc1 = Doctor(1,"Dr. Smith","Cardiology")
doc2 = Doctor(2,"Dr. Jones","Neurology")
hospital.doctors.extend([doc1,doc2]) # Add doctors to the hospital
print(hospital.Doc_specialization(1)) # Output: Cardiology

pat1 = Patient(1,"Alice",30,["Flu","Cough"]) # Create patient with list attributes
pat2 = Patient(2,"Bob",45,["Diabetes"])
hospital.patients.extend([pat1,pat2]) # Add patients to the hospital
print(hospital.Patient_ailments(1)) # Output: ['Diabetes']

app1 = Appointment(1,1,1,datetime.date(2023,10,1),datetime.time(10,0))
app2 = Appointment(2,2,2,datetime.date(2023,10,2),datetime.time(11,0))
hospital.appointments.extend([app1,app2])
print(hospital.Appointment(doctor_id=1)) # Output: [app1]
print(hospital.Appointment(patient_id=2)) # Output: [app2]






