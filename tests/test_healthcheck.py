
import pytest
import logging as log
import os

@pytest.mark.tcid0
def test_healthcheck():
    log.info("Hello World")


@pytest.mark.tcid1
def test_check_ENV():
    # env_db = os.getenv('GITHUB_REPOSITORY_OWNER')
    log.info(os.getenv('DB_NAME'))
    log.info(os.getenv('GITHUB_JOB'))
    log.info(os.getenv('PERFLOG_LOCATION_SETTING'))