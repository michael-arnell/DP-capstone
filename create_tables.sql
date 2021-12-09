CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    city TEXT,
    state TEXT,
    postal_code TEXT,
    phone TEXT,
    user_type TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Competencies (
    competency_id INTEGER PRIMARY KEY AUTOINCREMENT,
    competency_name TEXT NOT NULL,
    date_created INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS Assessments (
    assessment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    competency_id INTEGER NOT NULL,
    assessment_name TEXT NOT NULL,
    FOREIGN KEY (competency_id) REFERENCES Competencies (competency_id)
);

CREATE TABLE IF NOT EXISTS Assessment_Results (
    user_id INTEGER NOT NULL,
    assessment_id INTEGER NOT NULL,
    score INTEGER NOT NULL,
    date_taken INTEGER NOT NULL,
    manager_id INTEGER,
    PRIMARY KEY (user_id, assessment_id),
    FOREIGN KEY (user_id) REFERENCES Users (user_id),
    FOREIGN KEY (assessment_id) REFERENCES Assessments (assessment_id),
    FOREIGN KEY (manager_id) REFERENCES Users (user_id)
);

INSERT INTO Users (first_name, last_name, email, password, user_type) VALUES (
    'Andrew', 'Fletcher', 'afletch', '$2b$12$609fYeYkyB5GVhjhcN4ZXu7OYUFX7Kp4CNQYxUyiHJGOis/Qxj1Va', 'user'
);

INSERT INTO Users (first_name, last_name, email, password, user_type) VALUES (
    'MollyKate', 'Greenhalgh', 'mkgreen', '$2b$12$609fYeYkyB5GVhjhcN4ZXu7OYUFX7Kp4CNQYxUyiHJGOis/Qxj1Va', 'user'
);

INSERT INTO Users (first_name, last_name, email, password, user_type) VALUES (
    'Andrew', 'Blonquist', 'ablon', '$2b$12$609fYeYkyB5GVhjhcN4ZXu7OYUFX7Kp4CNQYxUyiHJGOis/Qxj1Va', 'user'
);

INSERT INTO Users (first_name, last_name, email, password, user_type) VALUES (
    'Ammon', 'Roy', 'aroy', '$2b$12$609fYeYkyB5GVhjhcN4ZXu7OYUFX7Kp4CNQYxUyiHJGOis/Qxj1Va', 'user'
);

INSERT INTO Users (first_name, last_name, email, password, user_type) VALUES (
    'Jordan', 'Howard', 'jhow', '$2b$12$609fYeYkyB5GVhjhcN4ZXu7OYUFX7Kp4CNQYxUyiHJGOis/Qxj1Va', 'user'
);

INSERT INTO Competencies (competency_name, date_created) VALUES (
    'Computer Anatomy',1636614000
);
INSERT INTO Competencies (competency_name, date_created) VALUES (
    'Data Types',1636614000
);
INSERT INTO Competencies (competency_name, date_created) VALUES (
    'Variables',1636614000
);
INSERT INTO Competencies (competency_name, date_created) VALUES (
    'Functions',1636614000
);
INSERT INTO Competencies (competency_name, date_created) VALUES (
    'Boolean Logic',1636614000
);
INSERT INTO Competencies (competency_name, date_created) VALUES (
    'Conditionals',1636614000
);
INSERT INTO Competencies (competency_name, date_created) VALUES (
    'Loops',1636614000
);
INSERT INTO Competencies (competency_name, date_created) VALUES (
    'Data Structures',1636614000
);
INSERT INTO Competencies (competency_name, date_created) VALUES (
    'Lists',1636614000
);
INSERT INTO Competencies (competency_name, date_created) VALUES (
    'Dictionaries',1636614000
);
INSERT INTO Competencies (competency_name, date_created) VALUES (
    'Working witih Files',1636614000
);
INSERT INTO Competencies (competency_name, date_created) VALUES (
    'Exception Handling',1636614000
);
INSERT INTO Competencies (competency_name, date_created) VALUES (
    'Quality Assurance (QA)',1636614000
);
INSERT INTO Competencies (competency_name, date_created) VALUES (
    'Object-Oriented Programming',1636614000
);
INSERT INTO Competencies (competency_name, date_created) VALUES (
    'Recursion',1636614000
);
INSERT INTO Competencies (competency_name, date_created) VALUES (
    'Databases',1636614000
);

INSERT INTO Assessments (competency_id, assessment_name) VALUES (
    1,'Interview'
);
INSERT INTO Assessments (competency_id, assessment_name) VALUES (
    1,'Exam'
);INSERT INTO Assessments (competency_id, assessment_name) VALUES (
    1,'Project'
);INSERT INTO Assessments (competency_id, assessment_name) VALUES (
    1,'Presentation'
);
INSERT INTO Assessments (competency_id, assessment_name) VALUES (
    2,'Interview'
);
INSERT INTO Assessments (competency_id, assessment_name) VALUES (
    2,'Exam'
);INSERT INTO Assessments (competency_id, assessment_name) VALUES (
    2,'Project'
);INSERT INTO Assessments (competency_id, assessment_name) VALUES (
    2,'Presentation'
);
INSERT INTO Assessments (competency_id, assessment_name) VALUES (
    3,'Interview'
);
INSERT INTO Assessments (competency_id, assessment_name) VALUES (
    3,'Exam'
);INSERT INTO Assessments (competency_id, assessment_name) VALUES (
    3,'Project'
);INSERT INTO Assessments (competency_id, assessment_name) VALUES (
    3,'Presentation'
);
INSERT INTO Assessments (competency_id, assessment_name) VALUES (
    4,'Interview'
);
INSERT INTO Assessments (competency_id, assessment_name) VALUES (
    4,'Exam'
);INSERT INTO Assessments (competency_id, assessment_name) VALUES (
    4,'Project'
);INSERT INTO Assessments (competency_id, assessment_name) VALUES (
    4,'Presentation'
);
INSERT INTO Assessments (competency_id, assessment_name) VALUES (
    5,'Interview'
);
INSERT INTO Assessments (competency_id, assessment_name) VALUES (
    5,'Exam'
);INSERT INTO Assessments (competency_id, assessment_name) VALUES (
    5,'Project'
);INSERT INTO Assessments (competency_id, assessment_name) VALUES (
    5,'Presentation'
);
INSERT INTO Assessments (competency_id, assessment_name) VALUES (
    6,'Interview'
);
INSERT INTO Assessments (competency_id, assessment_name) VALUES (
    6,'Exam'
);INSERT INTO Assessments (competency_id, assessment_name) VALUES (
    6,'Project'
);INSERT INTO Assessments (competency_id, assessment_name) VALUES (
    6,'Presentation'
);
INSERT INTO Assessments (competency_id, assessment_name) VALUES (
    7,'Interview'
);
INSERT INTO Assessments (competency_id, assessment_name) VALUES (
    7,'Exam'
);INSERT INTO Assessments (competency_id, assessment_name) VALUES (
    7,'Project'
);INSERT INTO Assessments (competency_id, assessment_name) VALUES (
    7,'Presentation'
);