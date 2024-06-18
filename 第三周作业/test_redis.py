import redis

# link redis
# 本地 Redis 服务器，端口 6379
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# 增
r.set('mykey', 'Hello, redis!')
print(r.get('mykey'))

# 查
value = r.get('mykey')
print(f"获取的值: {value}")

# 改
r.set('mykey', 'Hello, redis! (updated)')
print(f"更新的值: {r.get('mykey')}")

# 删
r.delete('mykey')
print(f"删除后的值: {r.get('mykey')}")


