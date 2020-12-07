# How to disable CORS

This is how you disable Cross-Origin Resource Sharing (CORS) error. 

**DONT DO THIS IN A PRODUCTION BUILD**

As far as I am aware. CORS is a security measure that basically tells your server to not load things that are unsafe. What can happen is that if CORS is disabled on your server that you on accident end up on a malicious server. This server then downloads something onto your computer and can execute it. This is possible if CORS is disabled. If CORS is enabled then your computer will fail to execute it because CORS will block it. 

## Setup

```js
npm install cors
```

## Usage

```js
var express = require('express')
var cors = require('cors')
var app = express()

app.use(cors()) // WRONG: app.use(cors)

app.listen(80, function () {
  console.log('CORS-enabled web server listening on port 80')
})
```

From

* https://expressjs.com/en/resources/middleware/cors.html