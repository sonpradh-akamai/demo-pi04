import redis

myHostname = "redisCache-premium-priv-ep.redis.cache.windows.net"
myPassword = "nXG0h6vCzUTWnhwlHcIxxWrhqyqgletWFAzCaLs2jT4="

r = redis.StrictRedis(host=myHostname, port=6380,
                      password=myPassword, ssl=True)

result = r.ping()
print("Ping returned : " + str(result))

for i in range(2000):
    result = r.set("Message"+str(i), "Hello!, The cache is working with Python!" + str(i))
    print("SET Message returned : " + str(result))

for i in range(2000):
    result = r.get("Message" + str(i))
    print("GET Message returned : " + result.decode("utf-8"))

result = r.client_list()
print("CLIENT LIST returned : ")
for c in result:
    print(f"id : {c['id']}, addr : {c['addr']}")
