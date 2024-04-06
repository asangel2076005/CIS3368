// load the things we need
var express = require('express');
var app = express();
const bodyParser  = require('body-parser');

// required module to make calls to a REST API
const axios = require('axios');

app.use(bodyParser.urlencoded());

// set the view engine to ejs
app.set('view engine', 'ejs');



//index page
app.get('/', function(req,res){
    let persons = 
    [
        {
            "id": 1,
            "first_name": "John",
            "last_name": "Doe"
        },
        {
            "id": 2,
            "first_name": "Jane",
            "last_name": "Smith"
        },
        {
            "id": 3,
            "first_name": "Michael",
            "last_name": "Johnson"
        },
        {
            "id": 4,
            "first_name": "Emily",
            "last_name": "Davis"
        } 
    ];
    //res.render("pages/index.ejs", {});
    res.render("pages/alias.ejs", {people: persons})
})

app.post('/process_login', function(req, res){
    var user = req.body.username;
    var password = req.body.password;
    
    axios.get()
    if(user === 'admin' && password === 'password')
    {
        res.render('pages/welcome.ejs' ,{
            user: user,
            auth: true
        });
    }
    else
    {
        res.render('pages/welcome.ejs' ,{
            user: "UNAUTHORIZED",
            auth: false
        });
    }

})

app.post('/process_form', function(req, res){
    const selectedPersonId = req.body.selectedPerson;
    console.log("SELECTED PERSON's ID IS: " + selectedPersonId);

    var hero = req.body.hero;
    var url = "https://www.superheroapi.com/api.php/10221405381743383/search/" + hero;
    axios.get(url)
    .then((response) =>{
        let myHeroArray = response.data.results;
        let hero = myHeroArray[0];
        let aliases = hero.biography.aliases;

        res.render('pages/thanks.ejs', {
            aliases: aliases
        })
    })
})






app.listen(8081);
console.log('8081 is the magic port');
