USE HospitalDB;

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
