from dbTableWriter import dBTableWriter as writer
import sys
import argparse

error_out =
'Correct usage: python main.py' \
    '--host <host>'\
    '--user <user> '\
    '--password <password>' \
    '--dbname <dbname>'\
    '--tablename <tablename>'\
    '--infile <infile>'\
    '--batchsize <batchsize>'


def get_args():
    '''
        parse command line args
    '''

    args = argparse.ArgumentParser()

    def prep_args():
        '''
            add command line args
        '''
        parser.add_argument("--host")
        parser.add_argument("--user")
        parser.add_argument("--password")
        parser.add_argument("--dbname")
        parser.add_argument("--tablename")
        parser.add_argument("--infile ")

    prep_args()

    args = args.parse_args()

    config = {
        "host": args.host,
        "user": args.user,
        "password": args.password,
        "dbname": args.dbname
    }

    return {
        "infile": args.infile,
        "table_name": args.tablename,
        "batch_size": args.batchsize
        "config": config
    }


def main():

    dbWriter = Writer(
        **get_args()
    )

    dbWriter.backfill()


if __name__ == "__main__":
    main()
