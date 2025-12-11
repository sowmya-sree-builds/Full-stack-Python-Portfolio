// 1. Function Declaration
function greet() {
  console.log("Hello");
}
greet();

// 2. Function Expression
const greet2 = function() {
  console.log("Hello 2");
};
greet2();

// 3. Function With Parameters
function add(a, b) {
  console.log(a + b);
}
add(5, 3);

// 4. Function Without Parameters
function show() {
  console.log("Welcome");
}
show();

// 5. Anonymous Function
let hello = function(){
console.log('this is an anonymus function')
}
hello()

// 6. Function With Return
function multiply(a, b) {
  return a * b;
}
console.log(multiply(4, 2));

// 7. Function Without Return
function printName(name) {
  console.log(name);
}
printName("Sowmya");

// 8. Method Inside an Object
const obj = {
  greet() {
    console.log("Hello from object");
  }
};
obj.greet();

// 9. Higher-Order Function & Callback function
function one(hello){
    console.log('helloo');
    hello();
    console.log('students')}
function two(){
     console.log('good afternoon');
}
one(two)

// 11. Arrow Function
let data = (a,b)=>{
   console.log("hi this  ${a} harry ${b}")
}
data("is","Potter")

// 12. Recursive Function
function factorial(x){
    if(x==1){                       // base case / stopping func
        return 1;
    }
    else{
        return x*factorial(x-1)     // recursive call
    }
}

// 13. IIFE
(function(){
    console.log("Hii Guys")
})()
