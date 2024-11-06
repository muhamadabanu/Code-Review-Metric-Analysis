DataBase_SchemaQuery = "SHOW TABLES;"
Select_Query = "SELECT * FROM"
# Total Changes
TotalChangesQuery = '''SELECT COUNT(*) AS Total_Changes
FROM t_change'''

# Changes by Status
ChangesByStatusQuery = '''SELECT ch_status, COUNT(*) AS Changes_Count
FROM t_change
GROUP BY ch_status'''

# Distribution of Changes Across Branches
DistributionChangesBranchesQuery = '''SELECT ch_branch, COUNT(*) AS Changes_Count
FROM t_change
GROUP BY ch_branch
ORDER BY Changes_Count DESC'''

# Average Revisions per Change
AverageRevisionsPerChangeQuery = '''SELECT AVG(Revision_Count) AS Avg_Revisions_Per_Change
FROM (
    SELECT rev_changeId, COUNT(*) AS Revision_Count
    FROM t_revision
    GROUP BY rev_changeId
) AS RevisionCounts'''

# Top 5 Most Revised Changes
Top5MostRevisedChangesQuery = '''SELECT rev_changeId, COUNT(*) AS Revision_Count
FROM t_revision
GROUP BY rev_changeId
ORDER BY Revision_Count DESC
LIMIT 5'''

# Total Comments per Change
TotalCommentsPerChangeQuery = '''SELECT hist_changeId, COUNT(*) AS Total_Comments
FROM t_history
GROUP BY hist_changeId'''

# Average Lines Inserted per Revision
AverageLinesInsertedPerRevisionQuery = '''SELECT AVG(f_linesInserted) AS Avg_Lines_Inserted_Per_Revision
FROM t_file'''

# Average Lines Deleted per Revision
AverageLinesDeletedPerRevisionQuery = '''SELECT AVG(f_linesDeleted) AS Avg_Lines_Deleted_Per_Revision
FROM t_file'''

# Top 10 Contributors by Change Count
Top10ContributorsByChangeCountQuery = '''SELECT ch_authorAccountId, COUNT(*) AS Change_Count
FROM t_change
GROUP BY ch_authorAccountId
ORDER BY Change_Count DESC
LIMIT 10'''

# Top 10 Contributors by Revision Count
Top10ContributorsByRevisionCountQuery = '''SELECT rev_authorUsername, COUNT(*) AS Revision_Count
FROM t_revision
GROUP BY rev_authorUsername
ORDER BY Revision_Count DESC
LIMIT 10'''

# Contributors with the Most Comments
ContributorsWithMostCommentsQuery = '''SELECT hist_authorAccountId, COUNT(*) AS Comment_Count
FROM t_history
GROUP BY hist_authorAccountId
ORDER BY Comment_Count DESC
LIMIT 10'''

# Peak Hours for Commenting
PeakHoursForCommentingQuery = '''SELECT HOUR(hist_createdTime) AS Comment_Hour, COUNT(*) AS Comment_Count
FROM t_history
GROUP BY Comment_Hour
ORDER BY Comment_Count DESC'''

# Days with Highest Change Activity
DaysWithHighestChangeActivityQuery = '''SELECT DATE(ch_createdTime) AS Change_Date, COUNT(*) AS Change_Count
FROM t_change
GROUP BY Change_Date
ORDER BY Change_Count DESC'''

# Comment Count Trends over Time (monthly)
CommentCountTrendsOverTimeQuery = '''SELECT DATE_FORMAT(hist_createdTime, '%Y-%m') AS Month, COUNT(*) AS Comment_Count
FROM t_history
GROUP BY Month
ORDER BY Month'''

# Average Files Changed per Revision
AverageFilesChangedPerRevisionQuery = '''SELECT AVG(File_Count) AS Avg_Files_Changed_Per_Revision
FROM (
    SELECT f_revisionId, COUNT(*) AS File_Count
    FROM t_file
    GROUP BY f_revisionId
) AS FileCounts'''

# Projects with Highest Code Churn (Insertions + Deletions)
ProjectsWithHighestCodeChurnQuery = '''SELECT ch_project, SUM(f_linesInserted + f_linesDeleted) AS Total_Churn
FROM t_file
JOIN t_revision ON t_file.f_revisionId = t_revision.id
JOIN t_change ON t_revision.rev_changeId = t_change.id
GROUP BY ch_project
ORDER BY Total_Churn DESC'''

# Revisions with Most Comments
RevisionsWithMostCommentsQuery = '''SELECT hist_patchSetNum AS Revision_Number, COUNT(*) AS Comment_Count
FROM t_history
GROUP BY hist_patchSetNum
ORDER BY Comment_Count DESC
LIMIT 5'''