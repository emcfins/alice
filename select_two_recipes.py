import sys
import logging
import rds_config
import pymysql
import random

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

#logger.info("SUCCESS: Connection to RDS mysql instance succeeded")
def get_total_recipes(event, context):
    """
    This function fetches content from mysql RDS instance
    """

    item_count = 0
    tot_recipes = []
    with conn.cursor() as cur:
        cur.execute("SELECT recipeName from recipes WHERE mealType = 'entree'")
	result=cur.fetchall()
	for meal in result:
	    tot_recipes.append(meal[0])
	return(tot_recipes)

def rando_num(total_recipes):
    return(random.randrange(0,len(total_recipes)))

def get_two_recipes(event, context):
    total_recipes = get_total_recipes('a','b')    
    meal_1 = rando_num(total_recipes)
    meal_2 = rando_num(total_recipes)
    if meal_2 == meal_1:
        meal_2 = rando_num(total_recipes)
    print(total_recipes[meal_1] + ' vs ' + total_recipes[meal_2] + "! NOW BATTLE!")

if __name__ == "__main__":
    get_two_recipes('a','b')
