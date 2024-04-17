from langchain.agents import create_spark_sql_agent
from langchain.agents.agent_toolkits import SparkSQLToolkit
from langchain.chat_models import ChatOpenAI
from langchain.utilities.spark_sql import SparkSQL
import os
import shutil
from pyspark.sql import SparkSession
table_name = "titanic"
schema = "langchain_example"
table_path = f"/home/liangdao_hanli/project/llm-local/spark-warehouse/{schema}.db/{table_name}"
spark = SparkSession.builder.getOrCreate()
spark.sql(f"CREATE DATABASE IF NOT EXISTS {schema}")
spark.sql(f"USE {schema}")
if os.path.exists(table_path):
    shutil.rmtree(table_path)
    print(f"Removed existing directory at {table_path}")

print(f"Using database: {schema}")
tables = spark.catalog.listTables()
print(f"Tables in {schema}: {[table.name for table in tables]}")
print("=========================================")

if spark.catalog.tableExists(schema + "." + table_name):
    spark.sql(f"DROP TABLE IF EXISTS {schema}.{table_name}")
    print(f"Table {table_name} has been dropped.")
else:
    print(f"Table {table_name} does not exist.")

csv_file_path = "data/titanic.csv"
spark.read.csv(csv_file_path, header=True, inferSchema=True).write.saveAsTable(table_name)
# spark.table(table).show()

from core.create_llm_model import create_ollama_model
spark_sql = SparkSQL(schema=schema)
llm = create_ollama_model()
toolkit = SparkSQLToolkit(db=spark_sql, llm=llm)

agent_executor = create_spark_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True
)

while True:

    input_query = input("\nYou: ")
    if input_query == "exit":
        break
    if input_query.strip() == "":
        continue
    
    agent_executor.run(input_query)
