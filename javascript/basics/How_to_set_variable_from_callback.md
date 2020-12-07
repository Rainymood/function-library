# How to set variable from callback 

This is something that you will have to do often so it makes sense to write
it down. How do you set a variable value based on the result of a callback?

The solution is to make the function async. 

Imagine you have 

```js
// Get value from cache
cache.get(key, (err, reply) => {
    if (err) {
        console.log(err)
    }
    const val = reply
})

// Use value from cache
doSomething(val)
```

This will behave like you won't expect. `val` will most likely be some weird
value like `null` or `undefined`. This is because JavaScript is asynchronous.
It just runs top down and doesn't stop for anything really.

## Solution 1 

Make the `get` function async and use `await`. 

## Solution 2

Turn it into a promise. 



