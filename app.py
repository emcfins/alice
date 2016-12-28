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
        cur.execute("CREATE TABLE recipes ( recipeId  int NOT NULL AUTO_INCREMENT, recipeName varchar(255) NOT NULL, mealType varchar(255), PRIMARY KEY (recipeId))")  
        cur.execute('insert into recipes (recipeName, mealType) values("Buffalo Cauliflour", "entree")')
        cur.execute('insert into recipes (recipeName, mealType) values("Zuudles and Pesto", "entree")')
        cur.execute('insert into recipes (recipeName, mealType) values("Chickpeas and Spinach", "entree")')
        cur.execute('insert into recipes (recipeName, mealType) values("Seitan Buffalo Wings", "entree")')
        cur.execute('insert into recipes (recipeName, mealType) values("Tofu with Broccoli and Kale", "entree")')
	cur.execute('insert into recipes (recipeName, mealType) values("Veggie Moussaka With Puy Lentils", "entree")')
	cur.execute('insert into recipes (recipeName, mealType) values("Popeye\'s Fried Seitan", "entree")')
	cur.execute('insert into recipes (recipeName, mealType) values("Stuffed Acorn squash with quinoa and white beans", "entree")')
        conn.commit()
        cur.execute("select * from recipes")
        for row in cur:
            item_count += 1
            logger.info(row)
            #print(row)
    

    return "Added %d items from RDS MySQL table" %(item_count)

if __name__ == "__main__":
    handler('a','b')
