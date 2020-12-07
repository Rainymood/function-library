# How to setup a basic express app

Import `express`, `bodyParser`, and create a new express application by initialising it.

```js
const express = require('express');
const bodyParser = require('body-parser');
const app = express();
```

Then set the port with `app.set()`.

```js
app.set('port', 5000)
```

Then we add some body parsers. Sometimes this is not needed but you can put it in regardless. Can't hurt really.

```js
// Support parsing of application/x-www-form-urlencoded post data
app.use(bodyParser.urlencoded({
    extended: false
}));

// Support parsing of application/json
app.use(bodyParser.json());
```

And spin up the server

```js
// Spin up the server
app.listen(app.get('port'), function () {
    console.log(`running on port ${app.get('port')}`);
})
```

## Complete code

```js
const express = require('express');
const bodyParser = require('body-parser');
const app = express();

app.set('port', 5000)

// Process application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({
    extended: false
}));

// Process application/json
app.use(bodyParser.json());

// Spin up the server
app.listen(app.get('port'), function () {
    console.log(`running on port ${app.get('port')}`);
})
```

# Flashcards/questions

* How to initialize express app? 
* Why do we need a body parser?
* How to set port?
* How to spin up and listen to port?