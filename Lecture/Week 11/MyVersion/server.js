// load the things we need
var express = require('express');
var app = express();
const bodyParser  = require('body-parser');
const path = require("path");

// required module to make calls to a REST API
const axios = require('axios');
app.use(bodyParser.urlencoded());

// set the view engine to ejs
app.set('view engine', 'ejs');
app.set("views", path.resolve(__dirname, "views")); 

// use res.render to load up an ejs view file

app.get("/", function(req, res) {

    // Pretend this is retrieved from database using axios
    let person = [
        {
            id: 1,
            firstName: "John",
            lastName: "Doe"
        },
        {
            id: 2,
            firstName: "Jane",
            lastName: "Smith"
        },
        {
            id: 3,
            firstName: "Michael",
            lastName: "Johnson"
        },
        {
            id: 4,
            firstName: "Emily",
            lastName: "Davis"
        }
    ];

    res.render("index.ejs", {
        person: person
    });

    res.render("index.ejs", {
        person: person
    });
});

app.post("/process_login", function(req, res) {
    const user = req.body.username;
    const password = req.body.password;

    if (user === "admin" && password === "password")  {
        res.render("thanks.ejs", {
            user: user,
            auth: true
        });
    } else {
        res.render("thanks.ejs", {
            user: "UNAUTHORIZED",
            auth: false
        });
    }
});

app.post("/process_form", function(req, res) {
    const selectedPerson = req.body.selectedPerson;
    const hero = req.body.hero;
    const url = "https://www.superheroapi.com/api.php/10221405381743383/search/" + hero;
    
    axios.get(url)
    .then((response) => {
        let myHeroArray = response.data.results;
        let hero = myHeroArray[0];
        let aliases = hero.biography.aliases;

        res.render("thanks.ejs", {
            selectedPerson: selectedPerson,
            aliases: aliases
        });
    });
    
});

const port = 8080;
// Start the express application on port 8080 and print server start message
app.listen(port, () => console.log("Application started and listening on port 8080"));