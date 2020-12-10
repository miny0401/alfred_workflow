import sys
query = sys.argv[1]
output = "select * from {0} limit 100;".format(query)
# sys.stdout.write(output)
print(output)
