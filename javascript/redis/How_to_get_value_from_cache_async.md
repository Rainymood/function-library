# How to get value from redis cache async

Use `async-redis` instead of `redis`. 

```js
const redis = require("async-redis");
const cache = redis.createClient()
const value = await cache.get(key);
```