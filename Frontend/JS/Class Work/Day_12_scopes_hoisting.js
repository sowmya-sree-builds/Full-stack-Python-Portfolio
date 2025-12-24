// Scopes"
// where a variable is declared and where it can be access

// in var data is leaked out only in functions data cannot be accessed outside
// types of scopes:
// global scope - where a variable is declared lgobally it can be accessed both locally and globally
// functional scope - (var)both block and local
// block scope - let , const
// local scope

// let a =10;
// console.log(a)
// {
//     let a = 20;
//     console.log(a)
// }

// if(true){
//     let a = 30;
//     console.log(a)
// }
// for(let i=1;i<=5;i++){
//     let a = 30;
//     console.log(a)
//     console.log(i)
// }


// let a = 30;
// console.log(a);

// {
//     console.log(a)
// }

// var a = 30;
// console.log(a);

// {
//     console.log(a)
// }

// const a = 30;
// console.log(a);

// {
//     console.log(a)
// }


// {
//     let a = 10;
//     console.log(a)
// }
// console.log(a)  //--> for let cant be accessed out side if its var it can be accessed outside as well


// function name{
//     var a = 10;
//     console.log(a)
// }
// name()
// console.log(a)  // var is functional scope


// {} represents block of scope

// {
//     const a = 10;
//     console.log(a)
// }
// console.log(a)




// var - 
















// Hoisting: we can move the declaration part at the top of the scope

// var - it supports hoisting let const -- both doesnt support hoisting

// 

// var data;
// console.log(data)              // undefined

// var a =10;
// console.log(a);
// var a = 10;



// TDZ  -  temporal dead zone   -- the time between compliation phase and execution phase

// compilation execution
// var a ; memory access a = undefined (initialized)
// let a; memory access a = uninitialized
// const a; memory access a = uninitialized


//    hoisiting supports function declaration
// greet()
// function greet(){
//     console.log("hello")
// }



greet()
function greet(){
    console.log("hello")
}







