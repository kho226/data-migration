import psycopg2

from psycopg2.extras import execute_values

from dataReader import DataReader
from sqlStatements import SQLStatements


class dBTableWriter(object):
    def __init__(self, infile, table_name, config, batch_size):
        self.config = config
        self.data_reader = DataReader(infile)
        self.table_name = table_name
        self.sql_statements = SQLStatements(self.table_name)
        self.batch_size = batch_size

    def get_cursor(self, dbname, user, host, password):
        '''
            gets a cursor to postgres db
            ~ deprecated
        '''
        try:
            conn = psycopg2.connect("dbname='{}' user='{}' host='{}' password='{}'".format(
                dbname, user, host, password))
            return conn.cursor()
        except:
            print ("Unable to connect to the database")

    def prepare_args_list(self):
        '''
            prepares sequence of sequences with arguements to send to the query
        '''
        args_list = []
        for i in range(self.batch_size):
            args_list.append(self.data_reader.data[i])
        return args_list

    def execute_query(self, query, args_list):
        '''
            execute query with values_list
        '''
        try:

            conn = psycopg2.connect(**self.config)
            curr = conn.cursor()

            execute_values(
                self.c,
                query,
                args_list,
                template=None,
                page_size=100  # default_value
            )

            curr.close()
            curr.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def table_exists(self, table_name):
        '''
            checks if table exists
        '''
        try:

            conn = psycopg2.connect(**self.config)
            curr = conn.cursor()

            curr.execute(
                "select exists(select * from information_schema.tables where table_name=%s)", ('{}'.format(table_name),))

            return self.c.fetchone()[0]

            curr.close()
            curr.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def create_table(self, table_name):
        '''
            create table
        '''
        try:

            conn = psycopg2.connect(**self.config)
            curr = conn.cursor()

            curr.execute(self.sql_statements.create_table)

            curr.close()
            curr.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def backfill(self):
        '''
            write to db
        '''
        args_list = self.prepare_args_list(self.batch_size)
        sql = self, sql_statements.insert_into_db

        if not self.table_exists(self.table_name):
            self.create_table(self.table_name)

        self.execute_query(sql, args_list)
