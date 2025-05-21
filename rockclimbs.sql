-- Standard SQL

-- This SQL script creates a the database "rockclimbs"
-- which I have used on the final project of the Web Services and Applications course
-- The design of some of the tables was not well thought from the beggining
-- and thus some of the alter table statements are not necessary

CREATE DATABASE rockclimbs;

CREATE TABLE styles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    style_name VARCHAR(100) NOT NULL
);

CREATE TABLE crags (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255),
    country VARCHAR(100),
    lat DECIMAL(10,6),
    lon DECIMAL(10,6),
    more_info VARCHAR(500)
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
    FOREIGN KEY (climb_id) REFERENCES climbs(id),
    date_climbed DATE
);

INSERT INTO styles (style_name)
VALUES 
('Bouldering'),
('Lead'),
('Trad');

INSERT INTO crags (name, location, country, lat, lon, more_info)
VALUES 
('Inishmore', 'Aran Islands', 'Ireland', 53.107500, -9.699083, 'https://www.instagram.com/inismor_bolt_fund/?hl=es'),
('Tamadaba', 'Canary Islands', 'Spain', 28.057809, -15.695204, 'https://www.thecrag.com/es/escalar/spain/gran-canaria/tamadaba'),
('Patones', 'Madrid', 'Spain', 40.882628, -3.441240, 'https://www.thecrag.com/es/escalar/spain/patones');

INSERT INTO climbs (name, grade, crag_id, style_id)
VALUES 
('Piercing Bamba', '7a+', 1, 2),  
('Freight Train Boogie', '7b', 1, 2),     
('Panico en Juncalillo', '6a+', 2, 2),      
('Directo al techo', '6b', 3, 2);         

INSERT INTO climb_log (climb_id, completed, attempts, personal_grade_feeling,date_climbed)
VALUES 
(1, TRUE, 15, '7a+','2022-08-14'),
(2, TRUE, 4, '7b','2023-08-14'),
(3, TRUE, 1, '6a+','2025-05-07'),
(4, TRUE, 3, '6b','2021-02-14');