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
    compentency_id INTEGER PRIMARY KEY AUTOINCREMENT,
    compentency_name TEXT NOT NULL,
    date_created TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Assessments (
    assessment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    compentency_id INTEGER NOT NULL,
    max_score INTEGER NOT NULL,
    FOREIGN KEY (compentency_id) REFERENCES Competencies (compentency_id)
);

CREATE TABLE IF NOT EXISTS Assessment_Results (
    user_id INTEGER,
    assessment_id INTEGER,
    score INTEGER,
    date_taken TEXT,
    manager_id INTEGER,
    PRIMARY KEY (user_id, assessment_id),
    FOREIGN KEY (user_id) REFERENCES Users (user_id),
    FOREIGN KEY (assessment_id) REFERENCES Assessments (assessment_id),
    FOREIGN KEY (manager_id) REFERENCES Users (user_id)
);

insert into Users (first_name,last_name,email,password,user_type) values ('Michael', 'Arnell', 'marnell@gmail.com','mipass','user');