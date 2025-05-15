// let score = prompt("enter your score (0-100):");
// let grade;

// if(score >= 90 && score <= 100){
//     grade = "A";
// } else if(score >=70 && score <= 89){
//     grade = "B";
// } else if(score >= 60 && score <= 69){
//     grade = "C";
// } else if(score >=50 && score <= 59){
//     grade = "D";
// } else if(score >=0 && score <= 49){
//     grade = "F";
// }

// console.log("according to your scores, your grade is :" , grade)

// for(let i=1 ; i<=5 ; i++ ){
//     console.log("Apna Cologe");
// }

// console.log("loop has ended");   

//game 

let gameNum = 65;

let userNum = prompt("Guess the game number :");

while(userNum != gameNum){
    userNum = prompt("You entered the wrong number , guess the game number :");
}
console.log("congratulation, you entered the right value");