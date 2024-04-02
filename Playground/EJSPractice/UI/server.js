// load the things we need
var express = require('express');
var app = express();
const bodyParser  = require('body-parser');

// required module to make calls to a REST API
const axios = require('axios');
app.use(bodyParser.urlencoded());

// set the view engine to ejs
app.set('view engine', 'ejs');




// Start here
app.get('/', function(req, res) {

    //itunes API call
    axios.get('https://itunes.apple.com/search?term=radiohead')
    .then((response)=>{
        let musicData = response.data;
        console.log(musicData);
        res.render('pages/index', {
            music: musicData
        });
    });

});

// About
app.get("/about", function(req, res) {
    //local API call to my Python REST API that delivers cars
    axios.get(`http://127.0.0.1:5000/api/student`)
    .then((response)=>{
        
        var student = response.data;
        var tagline = "Here is the data coming from my own API";
        console.log(student);
         // use res.render to load up an ejs view file
        res.render('pages/about', {
            student: student,
            tagline: tagline
        });
    });
});


// Contact
app.get("/contact", function(req, res) {

    const lol = "char"

    res.render("pages/contact", {
        char: lol
    })
});

// Rendering a form
app.post("/login", function(req, res) {
    const username = req.body.username;
    const password = req.body.password;

    console.log(`${username} ${password}`);

    res.render("pages/thanks", {
        username: username,
        password: password
    });
});


// Start the express application on port 8080 and print server start message
const port = 8080;
app.listen(port, () => console.log("Application started and listening on port 8080"));