
// array iteration methods

// iterate the arrays

// manipulate the arrays

// methods:
// foreach
// Map
// filter
// reduce 
// find 
// some 
// every



// difference between foreach and map

// document.body.innerHTML += "<h1>hello"\

// let data =[1,2,3,4,5];

// simple for loop
// for(let i =0;i<=4;i++){
//     console.log(data[i])
// }


//foreach:
// it is one of the array iteration method and it does not have any condition
// data.forEach((value)=>{
//     console.log(value)
// })


// let b = data.map((value)=>{
//     return value;
// })


// console.log(b)


// for each does not return an array map will return an array


// map:
// map will return an array

// dummy JSON
let data = [
    {title:"laptop",desc:"this is a laptop",price:30000},
    {title:"mobile",desc:"this is a mobile",price:15000},
    {title:"tv",desc:"this is a tv",price:18000}
]



// data.forEach((value,index,array)=>{
//     console.log(value.title) 
//     document.body.innerHTML += value.title
// })


let container = document.getElementById("container")
// data.forEach((value)=>{
//     container.innerHTML += `"<div id ="card">
//             <h1${value.title}></h1>
//             <p>${value.desc}</p>
//             <mark>${value.price}</mark>
//         </div>`
// })

let b = data.map((value)=>{ 
            return `<div id ="card">
            <h1${value.title}></h1>
            <p>${value.desc}</p>
            <mark>${value.price}</mark>
        </div>`
})

container.innerHTML += b.join('')


// foreach map inner reduce examples...