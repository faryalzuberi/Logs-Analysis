# Logs-Analysis
<b>LOGS ANALYSIS</b><br><br>
Logs Analysis a reporting tool for analysing the visitor activity on a newspaper website. The backend server database for the website creates a log each time a visitor tries to access a path on the server. Running this source file will analyse these logs and visitor trends and produce a report for the most popular articles, authors as well as an error log.
<br><br><b>USAGE</b><br><br>
In order to use this tool, the user must be running PostgreSQL on a Linux Based Virtual Machine such as Virtual Box. This tool can only be used with python 3.

After booting and logging into the Virtual Machine, place the source file, news.py and the newsdata.sql file inside the shared directory. Create and populate the database by running the SQL commands inside the newsdata.sql file.


This reporting tool makes use of views that must be created before running the source file. Using the command line, cd into the VM shared directory and connect to the news database using the command:

$psql -d news

After connecting run the following commands in order:<br>
=> create view author_join_articles as select authors.name, articles.title, articles.slug from authors, articles where authors.id = articles.author;<br>
=>create view path_aggregate as select path, count(*) as views from log group by path order by views desc;<br>
=>create view error_days as select date(time), count(*) as error from log where status != '200 OK' group by date; <br>
=>create view total_days as select count(*) as requests, date(time) from log group by date;<br>
=>create view error_percentage as select to_char(error_days.date, 'FMMonth FMDD, YYYY'), (cast(error_days.error as decimal)/total_days.requests)*100 as error_percentage from error_days, total_days where error_days.date = total_days.date;<br>

Disconnect from the database and run the source file from the command line using python news.py or python3 news.py
