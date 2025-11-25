Drop database hospitaldb;
create database hospitaldb;

USE HospitalDB;

CREATE TABLE Doctors (
    doctor_id INT PRIMARY KEY,
    name VARCHAR(100),
    specialization VARCHAR(50),
    phone VARCHAR(15),
    email VARCHAR(100),
    joining_date DATE
);

INSERT INTO Doctors (doctor_id, name, specialization, phone, email, joining_date)
VALUES
(1, 'Satoru Gojo', 'Neurosurgery', '9001200001', 'gojo@hospital.jp', '2021-05-14'),
(2, 'Suguru Geto', 'Psychiatry', '9001200002', 'geto@hospital.jp', '2020-09-20'),
(3, 'Kento Nanami', 'Cardiology', '9001200003', 'nanami@hospital.jp', '2022-02-10'),
(4, 'Yuji Itadori', 'Emergency Medicine', '9001200004', 'itadori@hospital.jp', '2023-01-05'),
(5, 'Megumi Fushiguro', 'Orthopedics', '9001200005', 'megumi@hospital.jp', '2023-03-22'),
(6, 'Nobara Kugisaki', 'Dermatology', '9001200006', 'nobara@hospital.jp', '2022-07-17'),
(7, 'Maki Zenin', 'Ophthalmology', '9001200007', 'maki@hospital.jp', '2021-11-11'),
(8, 'Toge Inumaki', 'ENT Specialist', '9001200008', 'toge@hospital.jp', '2022-12-01'),
(9, 'Panda', 'Pediatrics', '9001200009', 'panda@hospital.jp', '2023-04-09'),
(10, 'Yuta Okkotsu', 'Oncology', '9001200010', 'yuta@hospital.jp', '2021-08-25');

CREATE TABLE Patients (
    patient_id INT PRIMARY KEY,
    name VARCHAR(100),
    gender VARCHAR(10),
    dob DATE,
    phone VARCHAR(15),
    address VARCHAR(255),
    blood_group VARCHAR(5),
    admission_date DATE
);

INSERT INTO Patients (patient_id, name, gender, dob, phone, address, blood_group, admission_date)
VALUES
(1, 'Tanjiro Kamado', 'Male', '2000-07-14', '9876501111', 'Tokyo, Japan', 'O+', '2025-01-10'),
(2, 'Nezuko Kamado', 'Female', '2002-12-28', '9876502222', 'Tokyo, Japan', 'B+', '2023-02-15'),
(3, 'Zenitsu Agatsuma', 'Male', '2001-09-03', '9876503333', 'Kyoto, Japan', 'A+', '2025-03-05'),
(4, 'Inosuke Hashibira', 'Male', '2001-04-18', '9876504444', 'Osaka, Japan', 'O-', '2024-01-25'),
(5, 'Kanao Tsuyuri', 'Female', '2002-05-19', '9876505555', 'Nagoya, Japan', 'AB+', '2025-04-02'),
(6, 'Giyu Tomioka', 'Male', '1995-02-08', '9876506666', 'Tokyo, Japan', 'B-', '2020-02-20'),
(7, 'Shinobu Kocho', 'Female', '1996-07-24', '9876507777', 'Yokohama, Japan', 'A+', '2025-03-18'),
(8, 'Kyojuro Rengoku', 'Male', '1994-05-10', '9876508888', 'Sendai, Japan', 'O+', '2025-01-30'),
(9, 'Tengen Uzui', 'Male', '1993-10-31', '9876509999', 'Osaka, Japan', 'AB-', '2021-02-25'),
(10, 'Mitsuri Kanroji', 'Female', '1997-06-01', '9876510000', 'Kobe, Japan', 'B+', '2025-04-15');

CREATE TABLE Appointments (
    appointment_id INT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    appointment_date DATE,
    appointment_time TIME,
    reason VARCHAR(255),
    status VARCHAR(20),
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
);

INSERT INTO Appointments (appointment_id, patient_id, doctor_id, appointment_date, appointment_time, reason, status)
VALUES
(1, 1, 3, '2025-10-20', '10:00:00', 'Chest pain and fatigue', 'Completed'),
(2, 2, 1, '2025-10-22', '11:30:00', 'Frequent headaches', 'Scheduled'),
(3, 3, 6, '2025-10-21', '09:45:00', 'Skin allergy and rashes', 'Completed'),
(4, 4, 4, '2025-10-23', '14:15:00', 'Minor injury checkup', 'Scheduled'),
(5, 5, 5, '2025-10-19', '16:00:00', 'Back pain and stiffness', 'Completed'),
(6, 6, 8, '2025-10-25', '12:00:00', 'Throat irritation', 'Scheduled'),
(7, 7, 2, '2025-10-24', '10:30:00', 'Stress and anxiety', 'Cancelled'),
(8, 8, 10, '2025-10-26', '15:00:00', 'Follow-up for tumor screening', 'Scheduled'),
(9, 9, 7, '2025-10-18', '09:15:00', 'Eye irritation and dryness', 'Completed'),
(10, 10, 9, '2025-10-27', '13:00:00', 'Pediatric vaccination', 'Scheduled');

select * from doctors;
select * from appointments;
select * from patients;

CREATE TABLE Rooms (
    room_id INT PRIMARY KEY,
    room_type VARCHAR(50), 
    status VARCHAR(20),    
    charges_per_day DECIMAL(10,2)
);

INSERT INTO Rooms (room_id, room_type, status, charges_per_day)
VALUES
(101, 'General', 'Occupied', 1500.00),
(102, 'General', 'Available', 1500.00),
(201, 'Private', 'Occupied', 3500.00),
(202, 'Private', 'Available', 3500.00),
(301, 'ICU', 'Occupied', 8000.00),
(302, 'ICU', 'Available', 8000.00);


CREATE TABLE Admissions (
    admission_id INT PRIMARY KEY,
    patient_id INT,
    room_id INT,
    admit_date DATE,
    discharge_date DATE,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id)
);

INSERT INTO Admissions (admission_id, patient_id, room_id, admit_date, discharge_date)
VALUES
(1, 1, 101, '2025-01-10', NULL),
(2, 3, 201, '2025-03-05', NULL),
(3, 5, 202, '2025-04-02', NULL),
(4, 7, 301, '2025-03-18', NULL),
(5, 10, 102, '2025-04-15', NULL);

CREATE TABLE Treatments (
    treatment_id INT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    diagnosis VARCHAR(255),
    prescribed_medicines VARCHAR(255),
    treatment_date DATE,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
);

INSERT INTO Treatments (treatment_id, patient_id, doctor_id, diagnosis, prescribed_medicines, treatment_date)
VALUES
(1, 1, 4, 'Fever & Weakness', 'Paracetamol, ORS', '2025-01-11'),
(2, 3, 2, 'Anxiety Episodes', 'Vitamin B Complex, Sleep Aid', '2025-03-06'),
(3, 5, 6, 'Seasonal Allergies', 'Cetirizine', '2025-04-03'),
(4, 7, 8, 'Respiratory Infection', 'Azithromycin, Steam Inhalation', '2025-03-19'),
(5, 10, 5, 'Muscle Cramps', 'Magnesium Supplements', '2025-04-16');

CREATE TABLE Billing (
    bill_id INT PRIMARY KEY,
    patient_id INT,
    admission_id INT,
    total_amount DECIMAL(10,2),
    payment_status VARCHAR(20), -- Paid / Pending
    payment_date DATE,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (admission_id) REFERENCES Admissions(admission_id)
);

INSERT INTO Billing (bill_id, patient_id, admission_id, total_amount, payment_status, payment_date)
VALUES
(1, 1, 1, 6500.00, 'Paid', '2025-01-15'),
(2, 3, 2, 12500.00, 'Pending', NULL),
(3, 5, 3, 9800.00, 'Paid', '2025-04-05'),
(4, 7, 4, 18500.00, 'Pending', NULL),
(5, 10, 5, 4500.00, 'Paid', '2025-04-17');

select * from Rooms;
select * from Admissions;
select * from Treatments;
select * from Billing;


-- 5 Baisc Queries on Hospital Management
-- Display all patients admitted after 2024-01-01.
SELECT *
FROM Admissions
WHERE admit_date > '2024-01-01';

-- Retrieve all doctors who specialize in Cardiology.
SELECT *
FROM Doctors
WHERE specialization = 'Cardiologist';

-- Find all available rooms of type ICU.
SELECT *
FROM Rooms
WHERE room_type = 'ICU'
  AND status = 'Available';

-- Show appointments scheduled for a given doctor (by doctor_id).
SELECT *
FROM Appointments
WHERE doctor_id = 3
  AND status = 'Scheduled';
  
 -- Joins

-- List all patients with their assigned doctor names from Appointments.
SELECT 
    P.name AS patient_name,
    D.name AS doctor_name,
    A.appointment_date,
    A.status
FROM Appointments A
JOIN Patients P ON A.patient_id = P.patient_id
JOIN Doctors D ON A.doctor_id = D.doctor_id;


-- Display patient names, room types, and admission dates from Admissions.

SELECT
    P.name AS patient_name,
    R.room_type,
    A.admit_date,
    A.discharge_date
FROM Admissions A
JOIN Patients P ON A.patient_id = P.patient_id
JOIN Rooms R ON A.room_id = R.room_id;



-- Get a list of patients along with their treatment diagnosis and the doctor’s specialization.
SELECT
    P.name AS patient_name,
    T.diagnosis,
    D.specialization AS doctor_specialization,
    T.treatment_date
FROM Treatments T
JOIN Patients P ON T.patient_id = P.patient_id
JOIN Doctors D ON T.doctor_id = D.doctor_id;

-- Show billing details with patient name, room charges, and total bill amount.
SELECT
    P.name AS patient_name,
    R.charges_per_day,
    B.total_amount,
    B.payment_status
FROM Billing B
JOIN Patients P ON B.patient_id = P.patient_id
JOIN Admissions A ON B.admission_id = A.admission_id
JOIN Rooms R ON A.room_id = R.room_id;

-- Find all patients discharged and the doctor who treated them.
SELECT
    P.name AS patient_name,
    A.discharge_date,
    D.name AS doctor_name,
    T.diagnosis
FROM Admissions A
JOIN Patients P ON A.patient_id = P.patient_id
JOIN Treatments T ON P.patient_id = T.patient_id
JOIN Doctors D ON T.doctor_id = D.doctor_id
WHERE A.discharge_date IS NOT NULL;


-- Aggregate Functions

-- Count the number of patients currently admitted.
SELECT 
    COUNT(*) AS currently_admitted_patients
FROM Admissions
WHERE discharge_date IS NULL;

-- Find the total revenue collected (sum of all paid bills).
SELECT 
    SUM(total_amount) AS total_revenue
FROM Billing
WHERE payment_status = 'Paid';

-- Get the average charges per day for ICU rooms.
SELECT 
    AVG(charges_per_day) AS avg_icu_charges
FROM Rooms
WHERE room_type = 'ICU';

-- List doctors along with the number of patients they have treated.
SELECT 
    D.name AS doctor_name,
    COUNT(T.patient_id) AS total_patients_treated
FROM Doctors D
LEFT JOIN Treatments T ON D.doctor_id = T.doctor_id
GROUP BY D.doctor_id, D.name;

-- Find the patient who has the highest total bill amount.
SELECT 
    P.name AS patient_name,
    B.total_amount
FROM Billing B
JOIN Patients P ON B.patient_id = P.patient_id
ORDER BY B.total_amount DESC
LIMIT 1;

--  Subqueries

-- Find patients who have never booked an appointment.
SELECT *
FROM Patients
WHERE patient_id NOT IN (
    SELECT patient_id FROM Appointments
);

-- Retrieve patients who stayed the longest duration in the hospital.
SELECT *
FROM Admissions
WHERE discharge_date IS NOT NULL
ORDER BY DATEDIFF(discharge_date, admit_date) DESC
LIMIT 1;

-- Get details of patients whose total bill is higher than the average bill amount.
SELECT 
    P.name,
    B.total_amount
FROM Billing B
JOIN Patients P ON B.patient_id = P.patient_id
WHERE B.total_amount > (
    SELECT AVG(total_amount) FROM Billing
);

-- Find doctors who have not treated any patients yet.
SELECT *
FROM Doctors
WHERE doctor_id NOT IN (
    SELECT doctor_id FROM Treatments
);

-- Show patients who had more than one admission.
SELECT 
    P.patient_id,
    P.name,
    COUNT(A.admission_id) AS admission_count
FROM Patients P
JOIN Admissions A ON P.patient_id = A.patient_id
GROUP BY P.patient_id, P.name
HAVING COUNT(A.admission_id) > 1;

-- Updates & Deletes

-- Update the status of a discharged patient’s room to Available.
UPDATE Rooms
SET status = 'Available'
WHERE room_id = (
    SELECT room_id 
    FROM Admissions
    WHERE patient_id = 3 
      AND discharge_date IS NOT NULL
);

-- Change the phone number of a doctor.
UPDATE Doctors
SET phone = '9001209999'
WHERE doctor_id = 2;

-- Delete all appointments that are marked as Cancelled.
SET SQL_SAFE_UPDATES = 0;
DELETE FROM Appointments
WHERE status = 'Cancelled';
SET SQL_SAFE_UPDATES = 1;

-- Update the payment status of a bill after receiving payment.
UPDATE Billing
SET payment_status = 'Paid',
    payment_date = CURDATE()
WHERE bill_id = 4;


-- Advanced (Triggers, Views, Procedures)

-- Create a trigger to update room status to "Occupied" when a patient is admitted.
DELIMITER $$

CREATE TRIGGER update_room_status_on_admission
AFTER INSERT ON Admissions
FOR EACH ROW
BEGIN
    UPDATE Rooms
    SET status = 'Occupied'
    WHERE room_id = NEW.room_id;
END$$

DELIMITER ;


-- Create a view to show patient name, doctor name, diagnosis, and bill amount in one place.
CREATE VIEW Patient_Treatment_Billing_View AS
SELECT 
    p.name AS patient_name,
    d.name AS doctor_name,
    t.diagnosis,
    b.total_amount AS bill_amount
FROM Treatments t
JOIN Patients p ON t.patient_id = p.patient_id
JOIN Doctors d ON t.doctor_id = d.doctor_id
LEFT JOIN Billing b ON b.patient_id = p.patient_id;

SELECT * FROM Patient_Treatment_Billing_View;


-- Write a procedure to generate a bill for a patient based on admission and room charges.

DROP PROCEDURE IF EXISTS GenerateBill;
DELIMITER $$

CREATE PROCEDURE GenerateBill(IN p_admission_id INT)
BEGIN
    DECLARE v_patient_id INT;
    DECLARE v_room_id INT;
    DECLARE v_days INT;
    DECLARE v_charge DECIMAL(10,2);
    DECLARE v_total DECIMAL(10,2);
    DECLARE v_new_bill_id INT;

    -- New bill ID
    SELECT IFNULL(MAX(bill_id),0)+1 INTO v_new_bill_id FROM Billing;

    -- Patient + room
    SELECT patient_id, room_id
    INTO v_patient_id, v_room_id
    FROM Admissions
    WHERE admission_id = p_admission_id;

    -- Days stayed
    SELECT DATEDIFF(IFNULL(discharge_date,CURDATE()), admit_date)
    INTO v_days
    FROM Admissions
    WHERE admission_id = p_admission_id;

    -- Room charges
    SELECT charges_per_day INTO v_charge
    FROM Rooms
    WHERE room_id = v_room_id;

    -- Total
    SET v_total = v_days * v_charge;

    -- Final bill insert
    INSERT INTO Billing
    VALUES (v_new_bill_id, v_patient_id, p_admission_id, v_total, 'Pending', NULL);
END $$

DELIMITER ;

CALL GenerateBill(1);


-- Create a transaction that inserts a bill record only if the admission exists.
DROP PROCEDURE IF EXISTS SafeInsertBill;

DELIMITER $$

CREATE PROCEDURE SafeInsertBill(IN p_admission_id INT)
BEGIN
    DECLARE v_exists INT;
    DECLARE v_new_bill_id INT;

    START TRANSACTION;

    -- Check if admission exists
    SELECT COUNT(*) INTO v_exists
    FROM Admissions
    WHERE admission_id = p_admission_id;

    IF v_exists = 0 THEN
        ROLLBACK;
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Admission does not exist';
    END IF;

    -- Safely generate next bill_id (prevents duplicates)
    SELECT IFNULL(MAX(bill_id), 0) + 1
    INTO v_new_bill_id
    FROM Billing
    FOR UPDATE;

    -- Insert bill
    INSERT INTO Billing (bill_id, patient_id, admission_id, total_amount, payment_status, payment_date)
    VALUES (v_new_bill_id, p_admission_id, p_admission_id, 12000.00, 'Pending', NULL);

    COMMIT;
END$$

DELIMITER ;


CALL SafeInsertBill(3);

--  Reports / Analysis

-- Generate a report of top 5 patients with the highest medical expenses.
SELECT p.patient_id, p.name, SUM(b.total_amount) AS total_expense
FROM Patients p
JOIN Billing b ON p.patient_id = b.patient_id
GROUP BY p.patient_id, p.name
ORDER BY total_expense DESC
LIMIT 5;


-- List the most frequently prescribed medicine and the number of patients who received it.
-- Create Medicine Table
CREATE TABLE Medicine (
    med_id INT PRIMARY KEY,
    name VARCHAR(100),
    type VARCHAR(50)
);

-- Create Prescriptions Table
CREATE TABLE Prescriptions (
    prescription_id INT PRIMARY KEY,
    patient_id INT,
    med_id INT,
    date_prescribed DATE,
    dosage VARCHAR(100),

    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (med_id) REFERENCES Medicine(med_id)
);

-- Insert sample medicines
INSERT INTO Medicine VALUES
(1, 'Paracetamol', 'Tablet'),
(2, 'Amoxicillin', 'Capsule'),
(3, 'Ibuprofen', 'Tablet'),
(4, 'Cetrizine', 'Tablet'),
(5, 'Pantoprazole', 'Tablet');

-- Insert sample prescriptions
INSERT INTO Prescriptions VALUES
(1, 1, 1, '2024-10-01', '500mg'),
(2, 2, 2, '2024-10-04', '250mg'),
(3, 1, 3, '2024-10-10', '200mg'),
(4, 3, 1, '2024-10-06', '500mg'),
(5, 4, 1, '2024-10-09', '500mg'),
(6, 5, 4, '2024-10-12', '10mg');

SELECT m.med_id, m.name,
       COUNT(DISTINCT pr.patient_id) AS total_patients
FROM Medicine m
JOIN Prescriptions pr ON m.med_id = pr.med_id
GROUP BY m.med_id, m.name
ORDER BY total_patients DESC
LIMIT 1;

SHOW TABLES;
-- Show monthly revenue trends from billing data.
SELECT
    R.room_type,
    SUM(B.total_amount) AS total_room_revenue
FROM Billing B
JOIN Admissions A ON B.admission_id = A.admission_id
JOIN Rooms R ON A.room_id = R.room_id
WHERE B.payment_status = 'Paid'
GROUP BY R.room_type
ORDER BY total_room_revenue DESC
LIMIT 1;

-- Find which room type generates the maximum revenue.
SELECT 
    DATE_FORMAT(payment_date, '%Y-%m') AS month,
    SUM(total_amount) AS total_revenue
FROM Billing
WHERE payment_status = 'Paid'
GROUP BY month
ORDER BY month;


-- Report the doctor with the highest number of appointments.
SELECT d.doctor_id, d.name, COUNT(a.appointment_id) AS total_appointments
FROM Doctors d
JOIN Appointments a ON d.doctor_id = a.doctor_id
GROUP BY d.doctor_id, d.name
ORDER BY total_appointments DESC
LIMIT 1;

-- Identify patients who had both appointments and admissions within the last 6 months.
SELECT DISTINCT p.patient_id, p.name
FROM Patients p
JOIN Appointments a ON p.patient_id = a.patient_id
JOIN Admissions ad ON p.patient_id = ad.patient_id
WHERE a.appointment_date >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
  AND ad.admit_date >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH);