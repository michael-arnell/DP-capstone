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
    date_created TEXT NOT NULL
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
    date_taken TEXT NOT NULL,
    manager_id INTEGER,
    PRIMARY KEY (user_id, assessment_id),
    FOREIGN KEY (user_id) REFERENCES Users (user_id),
    FOREIGN KEY (assessment_id) REFERENCES Assessments (assessment_id),
    FOREIGN KEY (manager_id) REFERENCES Users (user_id)
);