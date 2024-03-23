const facility = [
    {
        "FACILITY_ID": 1,
        "FACILITY_NAME": "Math"
    },
    {
        "FACILITY_ID": 2,
        "FACILITY_NAME": "Science"
    },
    {
        "FACILITY_ID": 3,
        "FACILITY_NAME": "Art"
    },
    {
        "FACILITY_ID": 4,
        "FACILITY_NAME": "Language"
    },
    {
        "FACILITY_ID": 5,
        "FACILITY_NAME": "Area 51-Annex"
    }
]

const teacher = [
    {
        "CLASS_ID": 1,
        "TEACHER_FNAME": "John",
        "TEACHER_ID": 1,
        "TEACHER_LNAME": "Smith"
    },
    {
        "CLASS_ID": 2,
        "TEACHER_FNAME": "Alice",
        "TEACHER_ID": 2,
        "TEACHER_LNAME": "Johnson"
    },
    {
        "CLASS_ID": 3,
        "TEACHER_FNAME": "Michael",
        "TEACHER_ID": 3,
        "TEACHER_LNAME": "Williams"
    },
    {
        "CLASS_ID": 4,
        "TEACHER_FNAME": "Emily",
        "TEACHER_ID": 4,
        "TEACHER_LNAME": "Brown"
    },
    {
        "CLASS_ID": 5,
        "TEACHER_FNAME": "Daniel",
        "TEACHER_ID": 5,
        "TEACHER_LNAME": "Jones"
    },
    {
        "CLASS_ID": 6,
        "TEACHER_FNAME": "Sarah",
        "TEACHER_ID": 6,
        "TEACHER_LNAME": "Davis"
    },
    {
        "CLASS_ID": 7,
        "TEACHER_FNAME": "David",
        "TEACHER_ID": 7,
        "TEACHER_LNAME": "Miller"
    },
    {
        "CLASS_ID": 8,
        "TEACHER_FNAME": "Jessica",
        "TEACHER_ID": 8,
        "TEACHER_LNAME": "Wilson"
    },
    {
        "CLASS_ID": 9,
        "TEACHER_FNAME": "Matthew",
        "TEACHER_ID": 9,
        "TEACHER_LNAME": "Taylor"
    },
    {
        "CLASS_ID": 10,
        "TEACHER_FNAME": "Emma",
        "TEACHER_ID": 10,
        "TEACHER_LNAME": "Martinez"
    },
    {
        "CLASS_ID": 11,
        "TEACHER_FNAME": "Christopher",
        "TEACHER_ID": 11,
        "TEACHER_LNAME": "Anderson"
    },
    {
        "CLASS_ID": 12,
        "TEACHER_FNAME": "Olivia",
        "TEACHER_ID": 12,
        "TEACHER_LNAME": "Hernandez"
    },
    {
        "CLASS_ID": 13,
        "TEACHER_FNAME": "Andrew",
        "TEACHER_ID": 13,
        "TEACHER_LNAME": "Garcia"
    },
    {
        "CLASS_ID": 14,
        "TEACHER_FNAME": "Elizabeth",
        "TEACHER_ID": 14,
        "TEACHER_LNAME": "Lopez"
    },
    {
        "CLASS_ID": 15,
        "TEACHER_FNAME": "Ryan",
        "TEACHER_ID": 15,
        "TEACHER_LNAME": "Young"
    },
    {
        "CLASS_ID": 16,
        "TEACHER_FNAME": "Grace",
        "TEACHER_ID": 16,
        "TEACHER_LNAME": "Scott"
    },
    {
        "CLASS_ID": 17,
        "TEACHER_FNAME": "Joshua",
        "TEACHER_ID": 17,
        "TEACHER_LNAME": "Green"
    },
    {
        "CLASS_ID": 18,
        "TEACHER_FNAME": "Ava",
        "TEACHER_ID": 18,
        "TEACHER_LNAME": "Adams"
    },
    {
        "CLASS_ID": 19,
        "TEACHER_FNAME": "Kevin",
        "TEACHER_ID": 19,
        "TEACHER_LNAME": "King"
    },
    {
        "CLASS_ID": 20,
        "TEACHER_FNAME": "Sophia",
        "TEACHER_ID": 20,
        "TEACHER_LNAME": "Hill"
    },
    {
        "CLASS_ID": 21,
        "TEACHER_FNAME": "Eddie",
        "TEACHER_ID": 22,
        "TEACHER_LNAME": "Brock"
    },
    {
        "CLASS_ID": 21,
        "TEACHER_FNAME": "Peter",
        "TEACHER_ID": 23,
        "TEACHER_LNAME": "Parker"
    }
]

const select = document.querySelector("select");

for (const entity of facility) {
    const option = document.createElement('option');
    option.value = entity['FACILITY_ID'];
    option.textContent = entity["FACILITY_NAME"];
    select.appendChild(option);
}

const datalist = document.querySelector("datalist");

for (const entity of teacher) {
    const option = document.createElement('option');
    option.textContent = `${entity["TEACHER_LNAME"]} ${entity["TEACHER_FNAME"]}`;
    datalist.appendChild(option); 
}
