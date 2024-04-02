
from Utility.credentialsUtility import credentialsDB

import pytest
import logging as log
import os

@pytest.mark.tcid0
def test_healthcheck():
    log.info("Hello World")


@pytest.mark.tcid1
def test_check_ENV():
    cred_db = credentialsDB()
    env_db = cred_db['db_user']
    log.info(env_db)


