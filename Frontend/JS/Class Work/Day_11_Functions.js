// functions in JS:
// a block of code is designed to perform some repetative tasks
// a function does not executed it  self, it is executed when we call or invoke the function 
// when we call or invoke the function
// code reusability purpose
// heart of javascript


// function syntax:
// function =>  keyword
// function function_name
// ()
// {
    // statement / code block
// }
// function call/invoke

// parameters: the values which are passed in the function declaration
// in js parameters are called as "inbuilt variables"
// arguments: the values which are passed in the function call

// Types of Functions
// 1. function declaration
// 2. function expression
// 3. function with parameter
// 4. function without parameter
// 5. function with return
// 6. function without return
// 7. Method objects
// 8. Arrow functions(Es6 concept)
// 9. Higher order function
// 10. callback function
// 11. anonymus function
// 12. recursive function
// 13. life function
// 14. timing functions




// console.log("this is sai");
// console.log('this is ram');
// console.log("this is siva");

// console.log("this is sai");
// console.log('this is ram');
// console.log("this is siva");


// 1. function declaration
function fun1(){
    console.log("this is sai");
    console.log('this is ram');
    console.log("this is siva");
}
fun1()
fun1()


// 2. function Expresion - Here we have to assign a function to a variable
// a function with out a name is anonymus function like fun exp
let fun2 = function(){
    console.log('this is a function exp')
}
fun2()

// 3. function with parameters
let fun3 = function(a,b){
    console.log(a+b)
    console.log(a-b)
    console.log(a*b)
    console.log(a/b)
}
fun3(3,5)
// fun3() -- //error undefined

// 4. function without parameter
function fun4(){
    console.log("Hi!! sagar what a sudden supai!")
}
fun4()

// 5. function with return
// return - it is a keyword which returns some data back, if we write any statements after they return will not be executed
//          it will stop the function execution
//          you can store the data into one variable
function fun5(a,b){
    console.log("addition brother")
    return a+b;
    console.log("hello") // statements after return will not be executed it stops at the return keyword itself
}
let res = fun5(10,30);
console.log(res)


// 6. function without return
function fun6(a,b){
    console.log(a+b);
}fun6(6,10)  //uncaught reference error will come if we ignore giving parameters in functin def

// 7. Method objects
// a function which is passed in to an object is called method object

let hero = {
    name:"sam",
    age:22,
    loc:"hyd",
    data1:function(){
        console.log(`hii this is ${this.name}`)
    }
}
console.log(hero.data1())
// bydefault functions are undefined


// perform addition substraction using function declaration perform mul,div using function expression
// print your family mem names one by one using fd
// print "my name is abc my loc is hyd age is 22"
// using method objects(keys = name,loc,age,data)

// 8. Arrow functions(Es6 concept)
// 9. Higher order function
// 10. callback function
// 11. anonymus function
// 12. recursive function
// 13. life function
// 14. timing functions