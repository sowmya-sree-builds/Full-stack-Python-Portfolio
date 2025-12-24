// 1.print 1 to 5 numbers using for loop,while and dowhile
// 2.perform break and continue with three loops
// 3.take array of objects atleast 5 obj perform break&
// continue on array of objects data using for and while
// 4.take input from user variable name is dicevalue if your
// value is 1 then print "u r dice value is 1 " same like up to six numbers
// using switch
// 5.even or odd using if else
// 6.take an obj with atleast 6 key value pairs access only values
// using for in loop
// 7.perform for of loop on arrays and strings


// Task-1
// for(let i = 1;i<=5;i++){
//     console.log(i)
// }
// let j=1;
// while(j<=5){
//     console.log(j);
//     j++;
// }

// let k = 1;
// do{
//     console.log(k);
//     k++;
// }while(k<=5);

// Task-2
// for(let i =1;i<=10;i++){
//     if (i==5){
//         continue;
//     }
//     console.log(i);
// }

// for(let j=0;j<=9;j++){
//     if (j==4){
//         break
//     }
//     console.log(j);
// }

// let k = 1;
// while (k <= 10) {
//     if (k === 5) {
//         k++;        // increment before continue
//         continue;
//     }
//     console.log(k);
//     k++;
// }

// let k = 1;
// do {
//     if (k === 5) {
//         k++;        // increment before continue
//         break;
//     }
//     console.log(k);
//     k++;
// }while (k <= 10)


// Task-3
// let students = [
//     { id: 1, name: "Asha", marks: 85 },
//     { id: 2, name: "Ravi", marks: 40 },
//     { id: 3, name: "Meena", marks: 72 },
//     { id: 4, name: "Kiran", marks: 30 },
//     { id: 5, name: "Anil", marks: 90 }
// ];

// for (let i = 0; i < 5; i++) {
//     if (students[i].id === 4) {
//         continue;
//     }
//     console.log(students[i].name, students[i].marks);
// }



// 4.take input from user variable name is dicevalue if your
// value is 1 then print "u r dice value is 1 " same like up to six numbers
// using switch

// let diceValue = Number(prompt("Enter dice value (1 to 6):"));

// switch (diceValue) {
//     case 1:
//         console.log("Your dice value is 1");
//         break;
//     case 2:
//         console.log("Your dice value is 2");
//         break;
//     case 3:
//         console.log("Your dice value is 3");
//         break;
//     case 4:
//         console.log("Your dice value is 4");
//         break;
//     case 5:
//         console.log("Your dice value is 5");
//         break;
//     case 6:
//         console.log("Your dice value is 6");
//         break;
//     default:
//         console.log("Invalid dice value. Please enter a number between 1 and 6.");
// }


// 5.even or odd using if else
// let n = 2
// if (n%2 == 0){
//     console.log("Even")
// }
// else{
//     console.log("odd")
// }


// 6.take an obj with atleast 6 key value pairs access only values
// using for in loop
let city = {
    c1: "Vizag",
    c2: "Hyderabad",
    c3: "Chennai",
    c4: "Bangalore",
    c5: "Mumbai",
    c6: "Vijayawada"
};

for (let key in city){
    console.log(city[key]);
}



// 7.perform for of loop on arrays and strings
let numbers = [10, 20, 30, 40, 50];

for (let num of numbers) {
    console.log(num);
}

let fruits = ["Apple", "Banana", "Mango"];

for (let fruit of fruits) {
    console.log(fruit);
}

let name = "Sowmya";

for (let char of name) {
    console.log(char);
}