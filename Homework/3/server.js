// load the things we need
var express = require('express');
var app = express();
var path = require("path");
const bodyParser  = require('body-parser');

// required module to make calls to a REST API
const axios = require('axios');
app.use(bodyParser.urlencoded());

// Allow script and index to be used by index.ejs
app.use(express.static(path.join(__dirname, "misc")));

// set the view engine to ejs
app.set('view engine', 'ejs');

// Main Code
app.get("/", function(req, res) {
    // Retrieve comment data
    axios.get('https://dummyjson.com/comments')
    .then((response) => {

        let commentData = response.data;
        let comment = commentData["comments"]
        console.log(comment);

        res.render('index', {
            comment: comment
        });
    });
});


// Start the express application on port 8080 and print server start message
const port = 8080;
app.listen(port, () => console.log("Application started and listening on port 8080"));