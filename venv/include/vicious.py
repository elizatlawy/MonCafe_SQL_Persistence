import sqlite3
import os

# connect to the database


# register a function to be called immediately when the interpreter terminates


if __name__ == '__main__':
    if not os.path.isfile('grades1.db'):
        _conn = sqlite3.connect('grades1.db')
        _conn.executescript("""
                CREATE TABLE students (
                    id      INT         PRIMARY KEY,
                    name    TEXT        NOT NULL
                );
    
                CREATE TABLE assignments (
                    num                 INT     PRIMARY KEY,
                    expected_output     TEXT    NOT NULL
                );
    
                CREATE TABLE grades (
                    student_id      INT     NOT NULL,
                    assignment_num  INT     NOT NULL,
                    grade           INT     NOT NULL,
    
                    FOREIGN KEY(student_id)     REFERENCES students(id),
                    FOREIGN KEY(assignment_num) REFERENCES assignments(num),
    
                    PRIMARY KEY (student_id, assignment_num)
                );
            """)
        _conn.execute("""
                INSERT INTO students (id, name) VALUES (?, ?)
            """, [1, "name"])

        _conn.commit()
        _conn.close()
