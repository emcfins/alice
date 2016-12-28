import sys
import logging
import rds_config
import pymysql
#rds settings
rds_host  = "localhost"
#rds_host  = "wfd-db-cluster.cluster-co8ygranalho.us-west-2.rds.amazonaws.com"
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except:
    logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
    sys.exit()

logger.info("SUCCESS: Connection to RDS mysql instance succeeded")
def handler(event, context):
    """
    This function fetches content from mysql RDS instance
    """

    item_count = 0

    with conn.cursor() as cur:
        max_num = cur.execute('SELECT COUNT(*) FROM ' + str(db_name) + '.recipes')
        all_recipes = cur.execute('SELECT recipeName FROM ' + str(db_name) + '.recipes')
        print(max_num)
        print(all_recipes)

if __name__ == '__main__':
    handler('a','b')
