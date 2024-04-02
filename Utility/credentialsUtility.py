
import os
def credentialsDB():
    cred = os.environ['db_user']
    cred_info = {
        'db_user': cred
        }
    return cred_info

