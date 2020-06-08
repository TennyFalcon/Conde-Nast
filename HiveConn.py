from pyhive import presto
conn = presto.connect(host="presto.conde.io", port=8080, username="luigi")

print('connected')


cursor = conn.cursor()
cursor.execute("SELECT count(*) FROM hive.staq.appnexus WHERE dt between date '2019-01-01' AND date '2019-01-31' and revenue_type='PMP'")
result = cursor.fetchall()
print(result)

