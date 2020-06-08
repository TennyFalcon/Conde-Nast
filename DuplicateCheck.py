import prestodb
import pandas as pd

#Establishing connection to presto DB
conn = prestodb.dbapi.connect(host='presto.conde.io',port=8080,user='luigi',catalog='hive',schema='default')
#print('Connected to DB')
cur = conn.cursor()

#Reading SQL query from file
s_query_path = '/Users/tenny/Documents/Duplicate_query.txt'
s_read_query = open(s_query_path, 'r')
s_query = s_read_query.read()
#print(s_query)
print('Duplicate validation in progress')
cur.execute(s_query)

#Getting the query result in Dataframe
df = pd.DataFrame(cur.fetchall())
#print(df)
df_columns_len = len(df.columns)
#print(df_columns_len)

#Getting the column names to add it to the dataframe
def fields(cursor):
    results = {}
    columns = 0
    for x in cursor.description:
        results[x[0]] = columns
        columns = columns + 1
    return results

column_names = ()
column_names = fields(cur)
list_column_keys =[]
list_column_keys = list(column_names.keys())

#Renaming the Dataframe column names of the SQL column names
for x in range(df_columns_len):
    df.rename(columns={x:list_column_keys[x]},inplace=True)

#Checking duplicates
if df[list_column_keys[0]].count() == 0:
    print('No duplicates found')
else:
    print('Duplicates found.Duplicates are generated in the report "Duplicates_report.csv"')
    #writting the dataframe to csv file
    df.to_csv('/Users/tenny/Documents/Duplicates_report.csv',index=False)


