# Hospital Management System

This project is a Hospital Management System that tracks doctors, patients, and appointments. It includes functionality for managing doctors' specialties, patients' ailments, and appointment scheduling while preventing double bookings.

## Project Structure

```
hospital_management_system
├── main.py                  # Entry point of the application
├── models                   # Contains data models
│   ├── doctor.py           # Doctor class with details and availability
│   ├── patient.py          # Patient class with details and ailments
│   └── appointment.py       # Appointment class with scheduling details
├── services                 # Contains service classes for business logic
│   ├── doctor_service.py    # Manages doctor-related operations
│   ├── patient_service.py   # Manages patient-related operations
│   └── appointment_service.py # Manages appointment-related operations
├── utils                    # Contains utility functions
│   └── helpers.py          # Common utility functions for the project
└── README.md               # Documentation for the project
```

## Features

- **Doctor Management**: Add and manage doctors, retrieve their specialties, and check their availability.
- **Patient Management**: Add and manage patients, retrieve their details and ailments.
- **Appointment Scheduling**: Schedule appointments, check for conflicts, and retrieve appointments based on doctor or patient.
- **Utility Functions**: Common functions for date formatting and validation.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd hospital_management_system
   ```
3. Install any required dependencies (if applicable).

## Usage

- Run the application using:
  ```
  python main.py
  ```
- Follow the on-screen instructions to interact with the hospital management system.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.