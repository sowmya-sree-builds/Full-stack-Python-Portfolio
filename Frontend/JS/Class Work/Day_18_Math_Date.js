// math objects

// here we are manipulate the numbers 
    // Math - keyword
// Pi
// ROUND
// FLOOR - nearest int
// MIN  - min val 
// MAX
// RANDOM - random number from ()
// POW


// let a = Math.PI;
// console.log(a);
// console.log(a.toFixed(4));


// let b =Math.min(1,2,3,4,5);
// console.log(b)

// let c = Math.pow(2,3)  // 2**3 = 8  just like exponential
// console.log(c)

// let d = Math.round(5.4)  // 5
// let e = Math.row(5.7) // 6


// nearest int
// let f = Math.floor(5.7);
// console.log(e)   // 5


// let g = Math.random()
// console.log(g)  // random number from (0,1)
// console.log(g.toFixed(1))  // 0.3
// console.log(g.toFixed(1)*10)  // 1,10
// console.log(g.toFixed(1)*100)  // 1,100 - 10,20,30,40,50,60,70,80,90


// 4 numbers to generate and number should refresh everytime i click on otp  (2345)

// get element by id otp
// rnadom num


// number and whethers its even or odd in a circle



// date objects:
// which are used to work on dates and times


// Date()  -  to print current date and time


// new - new keyword will helps to create an object constructor function


// let a = new Date();
// console.log(a)

// let a = new Date("2025 , 11, 15");
// console.log(a)          // string method


// let a = new Date(2025,11,15,10,32,40);   // year,month,date,hour,min,sec   // month follows index in normal format index starting from (0,11)
// console.log(a)

// let a = new Date(0);   // time limit
// console.log(a)    // it gives when the js function started 

// let a = new Date(126584269852684);   // ms
// let a = new Date();
// console.log(a)    // it gives when the js function started 
// console.log(a.getFullYear());
// console.log(a.getMonth());
// console.log(a.getDay());

//getMethods

// getFullYear
// getMonth
// getDay
// getHours
// getMinutes
// getmilliseconds 
// getTime  // ms format 

//date formatting methods
// console.log(a.toDateString());  // only then we get name or else we get index
// console.log(a.toTimeString());
// console.log(a.toLocaleDateString());
// console.log(a.toLocaleTimeString());
// console.log(a.toLocaleString);



// setMethods  - same as get methods 
let d = new Date();
d.setFullYear(2027);
console.log(d)


// task should get hours mins seconds side by side with colon   // give 3 variable and use interpolation




