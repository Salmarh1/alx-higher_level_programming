-- Lists all records of the table second_table having a name value.
-- Records are ordered bu descending score.
Select 'score', 'name'
From 'second_table'
Where 'name' != ""
Order by 'score' desc
