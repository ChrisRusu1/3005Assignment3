To start the database I ran 
CREATE TABLE students (
  student_id SERIAL PRIMARY KEY,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE,
  enrollment_date DATE
);

INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');


For the video and the instructions I have all the database information in the .ini file because I dont want to save my password to youtube and github.

This is the youtube link for my video submission
https://youtu.be/Rf4jgbAMjrY


The config.ini file looks like This
[postgresql]
dbname=postgres
user=postgres
password=pass
host=localhost
port=5432