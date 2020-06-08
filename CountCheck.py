import prestodb

#Establishing connection to presto DB
conn = prestodb.dbapi.connect(host='presto.conde.io',port=8080,user='luigi',catalog='hive',schema='default')
print('Connected to DB')
cur = conn.cursor()

#Getting source count
s_query_path = '/Users/tenny/Documents/Source_query.txt'
s_read_query = open(s_query_path, 'r')
s_query = s_read_query.read()
#print(s_query)
print('Count check in progress')
cur.execute(s_query)
s_rows = []
s_rows = cur.fetchall()
s_count = s_rows[0]
print(str('Source count: ') + str(s_count))

#Getting Target count
t_query_path = '/Users/tenny/Documents/Target_query.txt'
t_read_query = open(t_query_path, 'r')
t_query = t_read_query.read()
#print(t_query)
cur.execute(t_query)
t_rows = []
t_rows = cur.fetchall()
t_count = s_rows[0]
print(str('Target count: ') + str(t_count))

#Validating the record count
if s_count == t_count:
    print("Record count matches")
else:
    print("Record Count is not matching")

