
//  Today task: 
// 1.Create an array for 5 emails and print 3 emails and  exit the loop if index is greater than 2.

let emails = [
  "bahubali@gmail.com",
  "mirai@yahoo.com",
  "sita@reddit.com",
  "ram@example.com",
  "mina@example.com"
];

for (let i = 0; i < emails.length; i++) {
  if (i > 2) {
    break; // exit loop if index > 2
  }
  console.log(emails[i]);
}


// 2.Create an array for 5 emails and print all the emails using while loop/For Loop.
let emails2 = [
  "dhanu@example.com",
  "sowmyasree@example.com",
  "sita@example.com",
  "ram@example.com",
  "mina@example.com"
];

let i = 0;
while (i < emails2.length) {
  console.log(emails2[i]);
  i++;
}

for (let j = 0; j < emails2.length; j++) {
  console.log(emails2[j]);
}

// 3.Write a JavaScript program using a for loop to print the multiplication table of 2.
for (let i = 1; i <= 10; i++) {
  console.log("2 x " + i + " = " + (2 * i));
}

// 4.using functions Write a program that prints the numbers from 1 to 100. For multiples of
// three, print "Fizz" instead of the number. For multiples of five, print "Buzz"
// instead of the number. For numbers that are multiples of both three and
// five, print "FizzBuzz".

function fizzBuzz() {
  for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log("FizzBuzz");
    } else if (i % 3 === 0) {
      console.log("Fizz");
    } else if (i % 5 === 0) {
      console.log("Buzz");
    } else {
      console.log(i);
    }
  }
}

fizzBuzz();
