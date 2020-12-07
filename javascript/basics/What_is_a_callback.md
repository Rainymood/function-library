# What is a callback? 

Found [here](https://codeburst.io/javascript-what-the-heck-is-a-callback-aba4da2deced).

## Simple answer

A callback is a function that is executed after another function has finished executing, hence the name "call back". 

## Complex answer

>More complexly put: In JavaScript, functions are objects. Because of this, functions can take functions as arguments, and can be returned by other functions. Functions that do this are called higher-order functions. Any function that is passed as an argument is called a callback function.
k

* In JS, functions are objects. 
* Functions can take other functions as arguments
* Functions can return other functions (these are called higher-order functions)
* Any function passed as an argument is a callback function.

## Why do we need callbacks? 

Because JavaScript is an event driven language. Instead of waiting for a
response before moving on, JavaScript will continue listening to other
events while waiting for that particular command to finish, and then
continuing. 

# Example

This example returns `2` first before `1`. Why? Because it didn't wait on the function `first()` to be done executing before moving to `second()`.

```js
function first(){
  // Simulate a code delay
  setTimeout( function(){
    console.log(1);
  }, 500 );
}
function second(){
  console.log(2);
}
first();
second();

// Returns
// 2
// 1
```
