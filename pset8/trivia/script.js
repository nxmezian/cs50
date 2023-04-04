document.addEventListener("DOMContentLoaded", function() {

    let correct = document.querySelector(".correct");
    correct.addEventListener("click", function() {
        correct.style.backgroundColor = "green";
        document.querySelector("#feedback1").innerHTML = "Correct!";
    });

    let incorrect = document.querySelectorAll(".incorrect");
    for (let i = 0; i < incorrect.length; i++) {
        incorrect[i].addEventListener("click", function() {
            incorrect[i].style.backgroundColor = "red";
            document.querySelector("#feedback1").innerHTML = "Incorrect!";
        });

        // Check free response submission
        document.querySelector(".open").addEventListener("click", function() {
            let input = document.querySelector("input");
            if (input.value == 2) {
                input.style.backgroundColor = "green";
                document.querySelector("feedback2").innerHTML = "Correct!";
            } else {
                input.style.backgroundColor = "red";
                document.querySelector("feedback2").innerHTML = "Incorrect!";
            }
        });

    }});