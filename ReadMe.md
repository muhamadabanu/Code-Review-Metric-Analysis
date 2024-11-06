# Code Review Metric Analysis

## Introduction
This project aims to derive analytical insights from code review data stored in a MySQL database. The data is fetched from the database for analysis, and the dataset structure is outlined below. The following table order reflects the typical information flow in a code review or change management system, based on common relationships within the data.

- DataSet Source url : `https://www.dropbox.com/s/ywgdz03dpvs7n11/gerrithub20161121.rar?dl=0`
- DataSet Schema info : `https://github.com/kin-y/miningReviewRepo/wiki/Database-Schema`

        People (t_people):
        This table contains information on developers, reviewers, and other team members. It provides the foundation by defining who is involved in the process.

        Change (t_change):
        This table records individual changes made by people (from t_people). It typically includes information such as the author of the change, timestamps for when the change was created and updated, and whether it is mergeable.
        
        Revision (t_revision):
        Each change may go through multiple revisions. This table tracks different versions or iterations of a change, showing the progression of the change and updates over time.
        
        History (t_history):
        This table records actions or comments made on the changes and revisions. It could include timestamps of each action, comments, and updates by different users, helping to track the review and feedback process.
        
        File (t_file):
        This table lists files associated with each revision of a change. It provides detailed information on the specific files impacted by the revisions, including data like lines inserted, lines deleted, and other file-specific metrics.

## Objective
The objective of this project is to analyze code review data to uncover key metrics and insights that enhance understanding of development workflows, code quality, and contributor activity. By leveraging data on changes, revisions, comments, and developer contributions, this analysis aims to:
1. Evaluate Code Quality and Feedback Cycles: Track change and revision frequencies, comment volumes, and review status trends to assess quality control and feedback efficiency.

2. Identify Key Contributors and Activity Patterns: Highlight top contributors by changes and revisions, identify peak activity periods, and assess individual impact on projects.

3. Monitor Project and Branch Activity: Measure change distribution across projects and branches, pinpoint areas of intense development or frequent rework, and detect high-churn areas.

4. Improve Development Process Insights: Analyze metrics such as average revision counts per change, comment frequency, and code churn to uncover potential bottlenecks and streamline code review processes.

## Project Files and Setup Instruction

This project includes a total of 9 key files, each serving a specific purpose:

1. README.md - Provides an introduction and instructions for executing the project.
2. requirements.txt - Lists all libraries and dependencies used in the project.
3. logger_info.txt - Stores output messages generated during code execution in main.ipynb.
4. environment.ini - Stores input variables required to execute the program.
5. environment/ - Contains functions to retrieve variables from environment.ini.
6. logs/ - Contains functions to handle and format logger operations.
7. utils/ - Contains supporting functions essential for running main.ipynb.
8. Sql_Query_Solutions.ipynb - A Jupyter Notebook that fetches and analyzes data by executing SQL queries on the MySQL database.
9. main.ipynb - The main Jupyter Notebook containing the project’s core code.
10. main_dashboard.pbix - Provide an overview of key features and metrics covered by the dashboard

To get started, follow these steps:
(Make sure you have stored the data in your MySQL database)
* Used Python Version - `Python 3.12.4`
1. Create the virtual environment - Use the command `python -m venv env` to create a virtual environment.
2. Activate the virtual environment.
3. Install dependencies - Run `pip install -r requirements.txt` to install all necessary dependencies.
4. Configure environment variables - Open `environment.ini` and enter the database credentials and log file path as input variables.
5. Run the main notebook - Open `main.ipynb` and run each cell sequentially to execute the primary code and analyze the results.
6. Run the `Sql_Query_Solutions.ipynb` - To get the solutions using SQL queries.

## Key Activities Performed in this Project(main.ipynb)

* Data Retrieval: Fetch all five data tables from the MySQL database.
* Data Quality Assessment: Check data types and identify null or empty values in each table.
* Data Imputation: Fill null or empty values as follows:
    1. t_change table:
        * ch_topic: Empty values are replaced with "No topic."
        * ch_mergeable: Empty values are replaced with "1" (indicating mergeable by default).
    2. t_history table:
        * hist_message: Empty values are replaced with "No message."
        * hist_authorAccountId: Empty values are replaced with "Unknown."
    3. t_people table:
        * p_name: Empty values are replaced with "Unknown_name."
        * p_email: Empty values are replaced with "No_email_found."
        * p_userName: Empty values are replaced with "Unknown_username."
    4. t_revision table:
        * rev_subject: Empty values are replaced with "No_subject_info."
* Data Type Conversion: Convert data types for necessary columns.
* Data Exploration and Transformation: Explore the data, transform it, and analyze its distribution and outliers. This process uncovers key insights into code review metrics, such as Total Changes and Changes Per Project, which help gauge overall activity and identify top projects. Metrics like Changes by Status and Revisions per Change track the code lifecycle, rework tendencies, and branch activity.
Developer Contribution Analysis: Highlight contributions through metrics such as Top Contributors by Change Count and Most Comments per Contributor. Additionally, Comment Count Trends and Peak Commenting Hours reveal engagement patterns. Code Churn by Project and Most Revised Changes spotlight areas of high modification, offering a holistic view of development workflow and review practices.
Recommendations and Optimization: To improve code review efficiency, we recommend implementing alerts for prolonged reviews where commit intervals exceed set thresholds, ensuring timely follow-ups on stalled changes. Analyzing revisions per change can help identify projects with high complexity, indicating potential areas for optimization. By targeting these projects for clearer requirements and code simplification, we can enhance workflow, reduce rework, and expedite the review process.
* Summary: In summary, this analysis not only underscores the strengths of the current development processes but also identifies areas for improvement, setting the stage for ongoing enhancements that will drive greater efficiency, collaboration, and success in future projects.

## Power Bi Dashboard

The dashboard consists of three pages: Executive_Overview, Changes_Merges, and Revisions_Commits.

Executive_Overview - Provides a high-level view of project metrics and code review status.
* KPI Cards: Displays total projects, total branches, total changes, developer count, and pending merge requests.
* Code Review Status: A donut chart showing the percentage distribution of changes categorized as MERGED, NEW, or ABANDONED.
* Total Projects by Developer and Status: Displays the count of projects contributed to by each developer.
* Total Changes Raised Over Time: A line and stacked column chart depicting the count of changes raised over the months.
* Filters: Date, month, year, project, and developer. Filters are synced between the Executive_Overview and Changes_Merges pages, allowing for dynamic visualization based on the selected filters.
* Navigation Buttons: Buttons to navigate to Changes_Merges and Revisions_Commits pages.

Changes_Merges - Analyzes branch modifications and merge request resolutions over time
* Branches Over Time: A line chart showing the count of branches modified over the months and years.
* Average Time to Resolve Merge Requests: A bar chart displaying the average time taken (in hours) to resolve merge requests by month and year.
* Monthly Merged Reviews: A line chart depicting the count of merged reviews completed each month.
* Top Projects by Change Count: A bar chart illustrating the count of changes occurring in each project.
* Top Contributors: A bar chart showing the count of changes made by each developer.

Revisions_Commits - Tracks revisions, comments, and commit activity by developer and code lines
* KPI Cards: Displays total lines inserted, total lines deleted, total lines modified, average comments per change, average revisions per change, and average comments per revision.
* Total Revisions: A line chart showing the total number of revisions raised for changes over the years and months.
* Total Comments: A line chart depicting the total number of comments raised for changes over the years and months.
* Total Revisions by Developer: A bar chart illustrating the count of revisions made by each developer.
* Total Commits by Developer: A bar chart showing the count of commits made by each developer.
* Codebase File Lines: A bar chart displaying the distribution of changes in code lines that are inserted and deleted.


### What more would I have done if provided with more time
If given more time, I would begin by concentrating more time in reviewing and enhance the dataset’s structure, quality and statistical analysis. This review would allow me to strengthen data accuracy, address distribution challenges, and refine correlations to draw more meaningful insights. Based on this feedback, I’d prioritize adding standardized metrics to align the analysis with industry benchmarks, uncovering deeper insights and ensuring that findings are relevant and actionable.

I would also focus on automating time-based reporting, setting up daily, monthly, and annual report cycles with detailed breakdowns by developer and project. This approach would facilitate tracking trends and performance over time, providing stakeholders with timely, clear insights. To support the ongoing value of these reports, I’d streamline the reporting process with automated updates, comprehensive documentation, and alignment with organizational objectives.

To elevate the analysis further, I’d apply advanced predictive analytics using Python, aiming to forecast likely merge times based on historical trends, developer workload, and project complexity. This would enable the team to identify and address potential delays proactively, improving resource allocation and project efficiency.

On the visualization side, I’d implement interactive drill-downs and role-specific filters in Power BI, allowing users to explore multi-level data specific to projects, developers, or timeframes. Additionally, I’d introduce dynamic KPI benchmarking against industry standards, leveraging Power BI’s DAX and alert features to monitor key metrics, such as average merge times or revision counts. This setup would notify users when these metrics exceed certain thresholds, allowing for quick responses to potential issues and fostering continuous improvement.