
// -------------------Document Object Model ------------------------
// dom represents hierarchy tree structure
// document: html file

// with the help of dom we can mnipulate the HTML Element like creating, adding, remove and modify.
// here browser allows js for interacting with the html elements. 
// script must be at the end of the body tag its a good practice

// console.log(document);   // it is nothing but the html file
// console.log(window)

// document.body.style.backgroundColor = "green"




// ---------------------DOM Selectors--------------------
// Which are used to access the paritcular html element
// 1. getElementsByTagName
// 2. getElementsByClassName
// 3. getElementById
// 4. querySelector
// 5. querySelectorAll

//tagname class names are in array format so to interact accessing 
// for queryselector class is . id is # for tag use direct tag name 

// in js consider text as space

// let p = document.getElementsByClassName('heroes1');
// p[0].style.backgroundColor = "red"     // it is in array format so to access it we gave p[0]
// console.log(p);

// let q = document.getElementsByTagName('ul');
// q[1].style.backgroundColor="blue"
// console.log(q)

// let z=document.getElementById('l2')
// z.style.color = "orange"

// let a = document.querySelector('ul')   // can take tag name id name and class name
// a.style.backgroundColor = "purple"
// console.log(a)

// let b = document.querySelectorAll('ul')
// b[1].style.backgroundColor = "red"


// html collection
// node list --  collection of html elements with including text
//  ParentNode
//  ChildNodes
//  FirstChild
//  LastChild
//  nextSibling

//html collection :  collection of html elements without including text
// ParentElement
// children
// FirstElementChild
// nextElementSibling

// text - text refers space


// let p = document.getElementById('Hero1');
// console.log(p.parentNode.parentNode.parentNode);
// console.log(p.childNodes)
// console.log(p.firstChild)
// console.log(p.Lastchild)
// console.log(p.nextsibling)

//console.log(p.parentElement)
// console.log(p.children)
// console.log(p.firstElementChild)
// console.log(p.lastElementChild)
// console.log(p.nextElementSibling)
