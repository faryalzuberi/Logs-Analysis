#!/usr/bin/env python3
#
# A reporting tool to analyse logs for a news website

import psycopg2
from datetime import datetime

DBNAME = "news"


# Returns three most viewed articles along with the view count
def get_popular_articles():
                db = psycopg2.connect(database=DBNAME)
                c = db.cursor()
                c.execute("select author_join_articles.title, "
                          "path_aggregate.views from path_aggregate,"
                          "author_join_articles where path_aggregate.path "
                          "like concat('%', author_join_articles.slug) "
                          "limit 3;")
                articles = c.fetchall()
                db.close()
                return articles


# Returns authors along with their respective views
def get_popular_authors():
                db = psycopg2.connect(database=DBNAME)
                c = db.cursor()
                c.execute("select author_join_articles.name, "
                          "sum(path_aggregate.views) as views from "
                          "path_aggregate, author_join_articles "
                          "where path_aggregate.path "
                          "like concat('%', author_join_articles.slug) "
                          "group by author_join_articles.name "
                          "order by views desc;")
                authors = c.fetchall()
                db.close()
                return authors


# Returns the dates where more than 1% of requests returned an error
def get_error_dates():
                db = psycopg2.connect(database=DBNAME)
                c = db.cursor()
                c.execute("select date, error_percentage from "
                          "error_percentage where error_percentage >=1;")
                dates = c.fetchall()
                db.close()
                return dates


def main():
                # print most popular articles
                print ("\nMost popular articles: ")
                articles = get_popular_articles()
                # loop through each row in result
                for row in articles:
                                article = row[0]
                                views = row[1]
                                r = "'%s', - %s views" % (article, views)
                                print(r)

                # print most popular authors
                print ("\nMost popular authors: ")
                authors = get_popular_authors()
                # loop through each row
                for row in authors:
                                author = row[0]
                                views = row[1]
                                r = "%s - %s views" % (author, views)
                                print(r)

                # print error prone days
                print ("\nError prone days: ")
                error = get_error_dates()
                # loop through each row
                for row in error:
                                date = row[0]
                                # convert the date string
                                # as a datetime object
                                date_obj = datetime.strptime(date, '%Y-%m-%d')
                                # format the datetime object
                                # appropriately e.g October 21, 2017
                                fdate = date_obj.strftime('%B %d, %Y')
                                percent = row[1]
                                # round off error percentage
                                # to 2 decimal places
                                percent = "{0:.2f}".format(percent)
                                r = "%s - %s %% errors" % (fdate, percent)
                                print(r)

if __name__ == '__main__':
                main()
