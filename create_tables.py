import sys
import logging
import rds_config
import pymysql
#rds settings
rds_host  = "localhost"
#rds_host  = "wfd-cluster.cluster-co8ygranalho.us-west-2.rds.amazonaws.com"
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
        cur.execute("CREATE TABLE recipes_list ( recipeId  int NOT NULL AUTO_INCREMENT, recipeName varchar(255) NOT NULL, mealType varchar(255), dateAdded datetime, PRIMARY KEY (recipeId))")  
    return "Created the recipes_list table" 

if __name__ == "__main__":
    handler('a','b')
