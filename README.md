{\rtf1\ansi\ansicpg1252\cocoartf1504\cocoasubrtf830
{\fonttbl\f0\fnil\fcharset0 Verdana;\f1\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red255\green255\blue255;}
{\*\expandedcolortbl;;\csgray\c0;\csgray\c100000;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\b\fs36 \cf2 \cb3 \CocoaLigature0 LOGS ANALYSIS
\b0\fs22 \
\
Logs Analysis a reporting tool for analysing the visitor activity on a newspaper website. The backend server database for the website creates a log each time a visitor tries to access a path on the server. Running this source file will analyse these logs and visitor trends and produce a report for the most popular articles, authors as well as an error log.\
\

\b\fs28 USAGE 
\b0\fs22 \
\
In order to use this tool, the user must be running PostgreSQL on a Linux Based Virtual Machine such as Virtual Box. This tool can only be used with python 3. \
\
After booting and logging into the Virtual Machine, place the source file, news.py and the newsdata.sql file inside the shared directory. Create and populate the database by running the SQL commands inside the newsdata.sql file.\
\

\b\fs28 STEPS 
\b0\fs22 \
\
This reporting tool makes use of views that must be created before running the source file. Using the command line, cd into the VM shared directory and connect to the news database using the command:\
\
$psql -d news\
\
After connecting run the following commands in order: \
\
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\fs24 \cf0 \cb1 \CocoaLigature1 => create view author_join_articles as 
\fs22 \cf2 \cb3 \CocoaLigature0 select authors.name, articles.title, articles.slug from authors, articles where authors.id = articles.author;\
=>create view path_aggregate as select path, count(*) as views from log group by path order by views desc;\
=>create view error_days as select count(*) as errors, to_char(time, 'YYYY-MM-DD') as date from log where status != '200 OK' group by date; \
=>create view total_days as select count(*) as requests, to_char(time, 'YYYY-MM-DD') as date from log group by date;\
=>create view error_percentage as select error_days.date, (cast(error_days.errors as decimal)/total_days.requests)*100 as error_percentage from error_days, total_days where error_days.date = total_days.date;\
\
Disconnect from the database and run the source file from the command line using python news.py or python3 news.py\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f1 \cf2 \
\
}