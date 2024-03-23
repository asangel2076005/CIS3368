const button = document.querySelector("button");
const output = document.querySelector(".output");

button.addEventListener("click", function() {
    const input = document.querySelector("#user-input").value.trim();
    output.textContent = "";

    player = [
        {
            "jersey_number": 1,
            "rating": 3
        },
        {
            "jersey_number": 2,
            "rating": 5
        }
    ];

    // If there is no value given to the input
    if (input) {
          console.log(input);
    } else {
        output.textContent = "No input received";
    } 

    switch (input) {

        case "a":
            // Creates 2 input elements
            let jerseyNumber = document.createElement("input");
            jerseyNumber.setAttribute("type", "text")
            jerseyNumber.setAttribute("id", "jersey-number");

            let rating = document.createElement("input");
            rating.setAttribute("type", "text");
            rating.setAttribute("id", "rating");

            // Creates 2 label elements
            const jerseyNumberLabel = document.createElement("label");
            jerseyNumberLabel.setAttribute("for", "jersey-number");
            jerseyNumberLabel.textContent = "Enter jersey number: ";

            const ratingLabel = document.createElement("label");
            ratingLabel.setAttribute("for", "rating");
            ratingLabel.textContent = "Enter rating from 1- 10: ";

            // Creates a button element
            const addButton = document.createElement("button"); 
            addButton.setAttribute("id", "addButton");
            addButton.textContent = "Enter";

            // Appends all created elements to .output element
            output.appendChild(document.createElement("br"));
            output.appendChild(jerseyNumberLabel);
            output.appendChild(jerseyNumber);
            output.appendChild(document.createElement("br"));
            output.appendChild(ratingLabel);
            output.appendChild(rating);
            output.appendChild(document.createElement("br"));
            output.appendChild(addButton);

            // Create another output paragraph element that takes place after the button element
            // The temporary input texts still remain
            const output2 = document.createElement("p");
            output2.setAttribute("class", "output");
            output.appendChild(output2);
        
            addButton.addEventListener("click", function() {
                // Ensures that output 2 everytime the addButton is clicked
                output2.innerHTML = "";

                if (isNaN(jerseyNumber.value) || isNaN(rating.value)) {
                    const errorParagraph = document.createElement("p");
                    errorParagraph.textContent = "All inputs must be numbers only"
                    output2.appendChild(errorParagraph);
                } else {
                    const paragraph = document.createElement("p");
                    
                    
                    for (const entity of player) {
                        // If both inputs are out of range 
                        if ((entity["jersey_number"] === Number(jerseyNumber.value)) || (Number(rating.value) < 0) || (Number(rating.value) > 10)) {
                            
                            if ((entity["jersey_number"] ===  Number(jerseyNumber.value))) {
                                const errorParagraph = document.createElement("p");
                                errorParagraph.textContent = "player already exists";
                                output2.appendChild(errorParagraph);
                            }

                            if ((Number(rating.value) < 0) || (Number(rating.value) > 10)) {
                                const errorParagraph = document.createElement("p");
                                errorParagraph.textContent = "rating must not be less than 0 or greater than 10";
                                output2.appendChild(errorParagraph);
                            }
                        }
                    }
                }
            });             
            break;

        case "d":
            break;

        case "u":
            break;

        case "r":
            break;

        case "o":

            if (player.length === 0) {
                output.textContent = "Empty data entry";
                
            } else {

                // NOT DONE: List each players in a format
                for (const entity of player) {
                    const paragraph = document.createElement("p");
                    paragraph.textContent = entity["jersey_number"];
                    output.appendChild(paragraph);
                }
            }

            break;
    }
});