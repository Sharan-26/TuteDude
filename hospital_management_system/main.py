import datetime
from models.doctor import Doctor
from models.patient import Patient
from models.appointment import Appointment
from services.doctor_service import DoctorService
from services.patient_service import PatientService
from services.appointment_service import AppointmentService

class HospitalManagementSystem:
    def __init__(self):
        self.doctor_service = DoctorService()
        self.patient_service = PatientService()
        self.appointment_service = AppointmentService()

    def run(self):
        while True:
            print("\nWelcome to the Hospital Management System")
            print("1. Add Doctor")
            print("2. Add Patient")
            print("3. Schedule Appointment")
            print("4. View Appointments")
            print("5. Exit")
            choice = input("Select an option: ")

            if choice == '1':
                self.add_doctor()
            elif choice == '2':
                self.add_patient()
            elif choice == '3':
                self.schedule_appointment()
            elif choice == '4':
                self.view_appointments()
            elif choice == '5':
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_doctor(self):
        doctor_id = input("Enter Doctor ID: ")
        name = input("Enter Doctor Name: ")
        specialization = input("Enter Specialization: ")
        doctor = Doctor(doctor_id, name, specialization)
        self.doctor_service.add_doctor(doctor)
        print(f"Doctor {name} added successfully.")

    def add_patient(self):
        patient_id = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        age = input("Enter Patient Age: ")
        ailments = input("Enter Patient Ailments (comma separated): ").split(',')
        patient = Patient(patient_id, name, age, [ailment.strip() for ailment in ailments])
        self.patient_service.add_patient(patient)
        print(f"Patient {name} added successfully.")

    def schedule_appointment(self):
        appointment_id = input("Enter Appointment ID: ")
        doctor_id = input("Enter Doctor ID: ")
        patient_id = input("Enter Patient ID: ")
        date = input("Enter Date (YYYY-MM-DD): ")
        time = input("Enter Time (HH:MM): ")
        appointment_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        appointment_time = datetime.datetime.strptime(time, "%H:%M").time()
        
        appointment = Appointment(appointment_id, doctor_id, patient_id, appointment_date, appointment_time)
        if self.appointment_service.schedule_appointment(appointment):
            print("Appointment scheduled successfully.")
        else:
            print("Appointment could not be scheduled due to a conflict.")

    def view_appointments(self):
        doctor_id = input("Enter Doctor ID to view appointments (or press Enter to view all): ")
        patient_id = input("Enter Patient ID to view appointments (or press Enter to view all): ")
        appointments = self.appointment_service.get_appointments(doctor_id, patient_id)
        if appointments:
            for appointment in appointments:
                print(f"Appointment ID: {appointment.appointment_id}, Doctor ID: {appointment.doctor_id}, Patient ID: {appointment.patient_id}, Date: {appointment.date}, Time: {appointment.time}")
        else:
            print("No appointments found.")

if __name__ == "__main__":
    hospital_system = HospitalManagementSystem()
    hospital_system.run()