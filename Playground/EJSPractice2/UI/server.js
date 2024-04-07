// load the things we need
const express = require('express');
const app = express();
const bodyParser  = require('body-parser');
const path = require("path");

// required module to make calls to a REST API
const axios = require('axios');
app.use(bodyParser.urlencoded());

// set the view engine to ejs
app.set('view engine', 'ejs');
app.set("views", path.resolve(__dirname, "views")); 

// Allow script and css to be used by the pages
app.use(express.static(path.join(__dirname, "misc")));


// Begin Code here
app.get("/", function(req, res) {

    const welcome = "Welcome"

    res.render("pages/index", {
        welcome
    });
});
app.post("/process_login", function(req, res) {

    const username = req.body.username;
    const password = req.body.password;

    if (username === "admin" && password === "12345") {
        // "Absolute" link instead of saying relative "pages/home"
        res.redirect("/home")
    } else {
        res.render("pages/error", {
            authorization: "Error"
        });
    }
});

app.get("/home", function(req, res) {
    
    axios.get(`http://127.0.0.1:5000/api/student`)
    .then((response)=>{
        
        let student = response.data;
        console.log(student);
         // use res.render to load up an ejs view file
        res.render('pages/home', {
            student
        });
    });
});

// Start the express application on port 8080 and print server start message
const port = 8080;
app.listen(port, () => console.log("Application started and listening on port 8080"));