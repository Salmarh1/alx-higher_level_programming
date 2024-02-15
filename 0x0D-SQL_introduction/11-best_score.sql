-- Lists all records in the table second_table with a score >= 10.
-- Records are ordered by descending score.
Select 'score', 'name'
From 'second_table'
Where 'score' >= 10
Order by 'score' desc;
