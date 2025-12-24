// loops:are used to repeatdely execute a block of statement 
// loop in js perform repertative tasks in less time

// types of loops
// for loop, while loop, do while loop


// for loop: is used when we know the number of iterations.
// syntax:
// for - keyword.
// (initializer, condition, finalvalue)
// {
        // block of statements
// } -- code block
// es6 concepts:
// foreach
// for in
// for of


// foreach:
// es6 concept
// it is an array iteration method

// syntax:
// variablename.forEach((paramters)=>{
//   
//})
// paramters - value,index,array

// forloop

// for(let i=1;i<=10;i++){
//     console.log(i)
// }

// for(let i=10;i<=1;i--){
//     console.log(i)
// }


// let data=[
//     {name:'sam',age:21},
//     {name:'sri',age:24},
//     {name:'kruel',age:32}
// ]

// for(let i=2;i<=0,i--){
//     console.log(data.names)
// }



// data.forEach((value,index,array)=>{
//     // console.log(value)
//     // console.log(index)
//     // console.log(array)
//     console.log(value,index,array)
// })



// for in loop:
// it is also one of the es6 concept
// it is used to iterate the properties of an object
// arrays and objects



// let hero = {
//     name:'narayana',
//     age:1234567,
//     role:'supreme God'
// }


// for(let i in hero){
//     // console.log(i)
//     console.log(hero[i])
// }



// for of loop:
// it is used on itrable objects like arrays and strings
// works only on str, arrays


// let data = [1,2,3,4,5]
// for (let i of data){
//     console.log(i)
// }



// for loop lo array patters anta 


// ------------------------------------------------------------Day-8----------------------------------------------------------------
// While Loop: it is used when we dont know the no of iterations
// it is execute the block of statements until the cond is true
// in for inititalization condition and increment are written in same line but in while its different
// while - excecutes only when condition is true; if condition is false then there is no output.
// syntax:
// initialisation
// while(cond){
        // block of statements
        // final value
// }


// let i = 1;
// while(i <= 10){                  
//     console.log(i);
//     i++;
// }


// do while - it will exceute the block of statements atleast once even if cond the is false.

// let i = 1;
// do{                  
//     console.log(i);
//     i++;
// }while(i <= 10);

// 1 to 5 f,w,d if cond f,w,d if continue, break at 4


// control flow statements 


// break - it is used to exit/terminate from the loop

// continue - it skips the current iteration



// for(let i =0;i<=5;i++){
//     if(i==3){
//         continue;
//     }
//     console.log(i);
//     i++;
// }



// let i = 1;
// while (i<=5){
//     if(i == 3){
//         break;
//     }
//     console.log(i)
// }


// let i = 1;
// while (i<=5){
//     i++;
//     if(i == 3){
//         continue;
//     }
//     console.log(i)
// }
// dummy json


let i = 2;
do{
    i++;
    if(i == 3){
        continue;
    }
    console.log(i)
}while (i<=5)

