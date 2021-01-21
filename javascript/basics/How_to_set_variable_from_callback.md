# How to set variable from callback 

If you try to "set a variable from a callback", like I once wanted to do.
Then you don't really *understand* JavaScript. This is not bad, you just need
someone to explain it to you. Because, MAN, this shit is confusing if you've
never worked with async.

## The problem

The problem is that we are dealing with asynchronous code. This means that
sending the request and retrieving the response are taken out of the normal
execution flow.

Consider the following example. 

```js
function foo() {
    var result;

    fs.readFile("path/to/file", function(err, data) {
        result = data;
        // return data; // <- I tried that one as well
    });

    return result; // It always returns `undefined`
}
```

The point is that the code runs everything top down: 

* It creates a variable `result`
* It sends off the function `fs.ReadFile()`
* It immediately continues to `return result`

Which of course, returns `undefined` because async doesn't wait! It returns
`result` before the callback was called. Which is... exactly how async works.

See this great stack overflow post: 

* https://stackoverflow.com/questions/14220321/how-do-i-return-the-response-from-an-asynchronous-call/14220323#14220323


