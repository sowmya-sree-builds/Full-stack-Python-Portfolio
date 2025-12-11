// we have to pass variable or expresions inside a string



// let name ="sowmya";
// let greet = "afternoon";
// console.log(`hello ${name} good ${greet}`);

// let x =20;
// let y = 30;
// console.log(`the sum of a and y is ${x+y}`)


// string methods:
// length: it returns the total length of a string
// indexOf: it returns the last index of a value of a character.
// lastIndexof: it returns the last index varlue of a charcater
// startswith: it checks whether the string is start with our given string or not.
// endswith: it checks whether the string is ends with our given string or not.
// toUpperCase: it converts the string in to uppercase.
// toLowerCase: it converts the string in to Lowercase.
// trim: it removes white spaces at strating and ending of a string.
// includes: it checks whether the char/word present or not.
// repeat: it is used to repeat a string
// replace: replace a old word with new word.
// slice: getting a substring from the original string.
// charAt: it returns the character based on teh index we give.


// let data ="         hello      i am in javascript class."
// // console.log(data.length)
// // console.log(data.indexOf('i'));
// // console.log(data.lastIndexOf('i')); 
// // console.log(data.indexOf('z'));   // -1
// // console.log(data.startsWith('hello'))
// // console.log(data.endsWith('s.'))
// console.log(data.toUpperCase())
// console.log(data.toLowerCase())
// console.log(data.trim())




// day_11
// it is es6
// it is used to write function in a shortway
// 
// single para
// multi para

// let data = (a)=>{
//    console.log("hi js ${a}")
// }
// data("es6").

// let data = a=>{
//    console.log("hi js ${a}")
// }
// data("es6").


// when we have single parameter the parenthesis is optional in arrow functions.

// let data = (a,b)=>{
//    console.log("hi js ${a} hello ${b}")
// }
// data("es6","ok").

// more than one parameter in function we must have parenthesis


// higher order functions -  a function which accepts another function as an argument

// callback function: a function which passes into another function as an argument 


// function one(hello){
//     console.log('helloo');
//     hello();
//     console.log('students')}
// function two(){
//      console.log('good afternoon');
// }
// here function one is higher order function and two is callback function.
// one(two)

// anonnymus function - a function without a name is called anonymus function


// let hello = function(){
// console.log('this is an anonymus function')
// }
// hello()


// recursive function: a function calling itself untill its meets base case
// base case: it is used for stopping the function it is mandatory to handle recursive

// function factorial(x){
//     if(x==1){                       // base case / stopping func
//         return 1;
//     }
//     else{
//         return x*factorial(x-1)     // recursive call
//     }
// }

// console.log(factorial(5))


// IIFE function:  Immediately invoke function expression
// function is wrapped in paranthesis
// calling the function instant


// (function(){
//     console.log("hello")
// })()