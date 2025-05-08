CREATE DATABASE rockclimbs;

CREATE TABLE styles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    style_name VARCHAR(100) NOT NULL
);

CREATE TABLE crags (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255),
    country VARCHAR(100)
);

CREATE TABLE climbs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    grade VARCHAR(20),
    crag_id INT,
    style_id INT,
    FOREIGN KEY (crag_id) REFERENCES crags(id),
    FOREIGN KEY (style_id) REFERENCES styles(id)
);

CREATE TABLE climb_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    climb_id INT,
    completed BOOLEAN DEFAULT FALSE,
    attempts INT DEFAULT 0,
    personal_grade_feeling VARCHAR(20),
    FOREIGN KEY (climb_id) REFERENCES climbs(id)
);

--INSERT INTO styles (style_name)
--VALUES 
--('Bouldering'),
--('Lead'),
--('Trad');

--INSERT INTO crags (name, location, country)
--VALUES 
--('Inishmore', 'Aran Islands', 'Ireland'),
--('Tamadaba', 'Canary Islands', 'Spain'),
--('Patones', 'Madrid', 'Spain');

--INSERT INTO climbs (name, grade, crag_id, style_id)
--VALUES 
--('Piercing Bamba', '7a+', 1, 2),  
--('Freight Train Boogie', '7b', 1, 2),     
--('Panico en Juncalillo', '6a+', 2, 2),      
--('Directo al techo', '6b', 3, 2);         

--INSERT INTO climb_log (climb_id, completed, attempts, personal_grade_feeling,date_climbed)
--VALUES 
--(1, TRUE, 15, '7a+','2022-08-14'),
--(2, TRUE, 4, '7b','2023-08-14'),
--(3, TRUE, 1, '6a+','2025-05-07'),
--(4, TRUE, 3, '6b','2021-02-14');

