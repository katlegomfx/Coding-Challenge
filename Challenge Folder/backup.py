"""This module has the functions that get data from the database"""


import logging as log
#import io
from pandas import DataFrame


from test_database import (
    execute_queries_get_dataframes,
    exc_qrs_get_dfs)

log.basicConfig(level=log.DEBUG)
log.info('----- QRS_GETS.PY -----')

def get_table(table=None):
    """Gets all data needed to display map from the desk being scanned.

    Args:
        table=None (str): determines which table to return

    Return:
        response_object (obj): python object of returned dataframes of the following:
            "users_table" (df): if arg was user
            "data_table" (df): if arg was data"""
    log.info(">> get_table(table=None). table: %s", table)

    # ˅
    if table == "records":
        query = ("SELECT * FROM records")
    elif table == "data":
        query = ("SELECT * FROM data")

    log.info("query list: %s", query)

    try:
        # get the data
        response = exc_qrs_get_dfs(query)
        log.info("database responses: %s", response)

        # response_object = {
        #     "records_table":response_list[0],
        #     "data_table": response_list[1]}

    except Exception as error:
        log.info(error)
        return error

    # ˅
    if table == "records":
        response_object={
            "records_table":response}
        return response_object

    if table == "data":
        response_object={
            "data_table":response}
        return response_object

    # return response_object
