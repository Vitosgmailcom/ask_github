
import pytest
import logging as log
import os

@pytest.mark.tcid0
def test_healthcheck():
    log.info("Hello World")


@pytest.mark.tcid1
def test_check_ENV():
    env_db = os.getenv('db_user')
    log.info(os.environ.get('db_user'))
    log.info(env_db)
    log.info(os.getenv('PERFLOG_LOCATION_SETTING'))