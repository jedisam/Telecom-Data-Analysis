CREATE TABLE Teleco
(
    id serial NOT NULL primary key,
    created_at TEXT DEFAULT NULL,
    msisdn TEXT DEFAULT NULL,
    user_engagment INT DEFAULT NULL,
    user_experience INT DEFAULT NULL
);
