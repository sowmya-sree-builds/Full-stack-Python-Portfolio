CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    age INT,
    department VARCHAR(50),
    cgpa DECIMAL(3,2)
);

ALTER TABLE students ADD email VARCHAR(100);
ALTER TABLE students MODIFY department VARCHAR(100);
ALTER TABLE students DROP COLUMN cgpa;
RENAME TABLE students TO student_info;
TRUNCATE TABLE student_info;
DROP TABLE student_info;
