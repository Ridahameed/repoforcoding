
 // displaying the numbers into screen

function appendNumber(number) {
    var screen = document.getElementById("screen");
    if (screen.innerHTML === "0" || screen.innerHTML === "") {
        screen.innerHTML = "";
    }
    screen.innerHTML += number; 
}

// displaying the operators into screen

function appendOperator(operator) {
    let screen = document.getElementById("screen").innerText;
    
    if (screen === "" || screen === "0") {
        return; 
    }

    if ('+-*/.'.includes(screen.slice(-1))) {
        screen = screen.slice(0, -1); 
    }  
    
    document.getElementById("screen").innerHTML = screen + operator;
}

// clearing the screen

function clean() {
    document.getElementById("screen").innerHTML = "0";
}

// deleting the last character

function del() {
    let screen = document.getElementById("screen").innerText;
    document.getElementById("screen").innerHTML = screen.slice(0, -1);
}

// calculating the result

function calculate() {
    let screen = document.getElementById("screen").innerText;
    document.getElementById("screen").innerHTML = eval(screen); 
}


