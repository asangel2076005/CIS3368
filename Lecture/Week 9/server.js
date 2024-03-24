// Load express module
const express = require("express");
const path = require("path");

// Put new express application on app variable
const app = express();

// Set views property and views engine
// This is the only thing that needs to be changed when doing other projects
app.set("views", path.resolve(__dirname, "views")); // Look for a directory called "views"
app.set("view engine", "ejs"); // Renders responses to you

const port = 8080;

// index page 
app.get('/', function(request, response) {
    // 127.0.0.1:8080/?name=Nana
    const name = request.query.name || "Guest";
    
    response.render('hello', {
        mascots: [
            { name: 'Sammy', organization: "DigitalOcean", birth_year: 2012},
            { name: 'Tuxedo', organization: "Linux", birth_year: 1996},
            { name: 'Moby Dick', organization: "Docker", birth_year: 2013}
        ],
        tagline: "No programming concept is complete without a cute animal mascot.",
        kinda: ["Something", "Really"],
        message: `${name} You're bruising up my heart`,
        mix: "Hello"
    });
});

// Start the express application on port 8080 and print server start message
app.listen(port, () => console.log("Application started and listening on port 8080"));