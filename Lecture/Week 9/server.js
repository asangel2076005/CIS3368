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

// When user hits home page, then we show the hello.ejs
app.get("/", (request, response) => response.render("hello", {
    message: "Welcome to express and EJS"
}));

// Start the express application on port 8080 and print server start message
app.listen(port, () => console.log("Application started and listening on port 8080"));