
import pytest
import logging as log
import os

@pytest.mark.tcid0
def test_healthcheck():
    log.info("Hello World")


@pytest.mark.tcid1
def test_check_ENV():
    env_db = os.environ.get('DB_NAME')
    log.info(env_db)
    assert env_db == "ASK_DATABASE"

