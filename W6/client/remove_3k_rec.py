from __future__ import print_function
import aerospike

config = {
  'hosts': [("172.10.0.1", 3000,)]
}
try:
  client = aerospike.client(config).connect()
except Exception as t:
  print("Connection Error: {0} [{1}]".format(t.msg, t.code))

#add 3000 records to both sets 'buyers' & 'products'
try:
  client = aerospike.client(config).connect()
  buyer_bins = {
      'name': 'Risheeth',
      'expenditure': 4000,
  }
  prod_bins = {
      'product': 'Laptop',
      'cost': 80000,
  }
  for i in range(1,3001):
      key = ('orders', 'buyers', i)
      client.remove(key, buyer_bins, meta={'ttl':86400})
  for j in range(1,3001):
      key = ('orders', 'products', j)
      client.remove(key, prod_bins, meta={'ttl':86400})
    
except Exception as e:
  print("DB Write Error: {0} [{1}]".format(e.msg, e.code))