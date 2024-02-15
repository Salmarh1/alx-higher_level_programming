-- Creates and filles a table second_table with attributess id, name and score.
Create table if not exists 'second_table'('id' INT, 'name' VARCHAR(256), 'score' INT);
Insert into 'second_table' ('id', 'name', 'score') values (1, “John”, 10);
Insert into 'second_table' ('id', 'name', 'score') values (2, “Alex”, 3);
Insert into 'second_table' ('id', 'name', 'score') values (3, “Bob”, 14);
Insert into 'second_table' ('id', 'name', 'score') values (4, “George”, 8);
