-- Lists the number of recods with the same score in the table second_table.
--Records are ordered by descending count.
Select 'score', count(*) as 'number'
From 'second_table'
Order by 'number' desc;
