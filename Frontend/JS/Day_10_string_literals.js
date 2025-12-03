// we have to pass variable or expresions inside a string



let name ="sowmya";
let greet = "afternoon";
console.log(`hello ${name} good ${greet}`);

let x =20;
let y = 30;
console.log(`the sum of a and y is ${x+y}`)


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


let data ="         hello      i am in javascript class."
// console.log(data.length)
// console.log(data.indexOf('i'));
// console.log(data.lastIndexOf('i')); 
// console.log(data.indexOf('z'));   // -1
// console.log(data.startsWith('hello'))
// console.log(data.endsWith('s.'))
console.log(data.toUpperCase())
console.log(data.toLowerCase())
console.log(data.trim())