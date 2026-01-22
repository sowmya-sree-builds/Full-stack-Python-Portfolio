// Asynchronous javasdcript

// it was not in format or order

// promises - api - it is one of the way to handle the asy operation.
//          asynchronous - synchronous
//          with the help of resolve and reject
//          with the help of new keyword we can create a promise
//          promise has 3 states  - pending, fullfilled, rejected

// API - application programming interface. - get the data from one application to our or another application.

// fetch is a method it will give the promise
// it will return the data when promise is resolved

// request the data to the server through url

// https://dummyjson.com/products


// async - await
// callback


// // console.log("task1");
// settimeout(()=>{
//     console.log("task2");
// },3000);
// console.log("task3")



// example add to payment only after product added to cart tasks depends on each other line lo jargali tasks
// let p = new Promise((resolve,reject)=>{
//     console.log("add to cart");
//     setTimeout(()=>{
//         console.log("proceed to pay");
//         resolve();
//     },3000)
// })
// .then(()=>{                     // to know the promise is success or not 
//     console.log("payment successful")
// })
// console.log(p)



let container = document.getElementById('container')
let products = fetch("https://dummyjson.com/products")
.then((response)=>{
    return response.json()
})
.then((data)=>{
    // console.log(data.products)
    let b = data.products.map((item)=>{
        return `<div id="card">
            <img src="${item.thumbnail}" alt="">
            <h1>${item.thumbnail}</h1>
            <p>${item.thumbnail}</p>
        </div>`
    })
    container.innerHTML+=b.json("")
})
