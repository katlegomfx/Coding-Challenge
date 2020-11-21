"""This module has the functions that get data from the database"""


import logging as log
#import io
from pandas import DataFrame


from test_database import (
    # execute_queries_get_dataframes,
    exc_qrs_get_dfs)

log.basicConfig(level=log.DEBUG)
log.info('----- QRS_GETS.PY -----')

def exec_it(query):
    log.info("query list: %s", query)
    try:
        # get the data
        response = exc_qrs_get_dfs(query)
        log.info("database responses: %s", response)

        return response

    except Exception as error:
        log.info(error)
        return error



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
        response_object={
            "records_table":exec_it("SELECT * FROM records")}
        return response_object

    if table == "data":
        response_object={
            "data_table":exec_it("SELECT * FROM data")}
        return response_object