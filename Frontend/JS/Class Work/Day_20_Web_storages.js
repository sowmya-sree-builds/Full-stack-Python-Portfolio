// webstorage:
// data will be stored locally
// browser it self


// localStorage - here data will be stored until unless user clears the data(5MB)
// sessionStorage - here data will be cleared after some period of time(5MB)
// cookies - it stores small part of data(4kb)


// methods:
// setItem() - for adding
// getItem() - for retriving
// removeItem() - for removing a particular data
// clear() - entire data will be clear

// localStorage
// sessionStorage

// localStorage.setItem('age','22');
// sessionStorage.setItem('age','21');
localStorage.setItem('name','sam');

// let a =localStorage.getItem('name');
// console.log(a)

localStorage.removeItem('name')
localStorage.clear()


localStorage.setItem('frnd','hey man')
localStorage.setItem('enemy','bye')
localStorage.setItem('frnd','hii')     // here already exsisitng reference will get updated


let days =["sun","mon","tue","wed","thur"];  // this is considered as raw data not like an array
localStorage.setItem("week",JSON.stringify(days))

let b = JSON.parse(localStorage.getItem('week'))
console.log(b[1])

// JSON - javascript object notation
// JSON.stringify  -  rawdata(js array)  will convert in to json string ; written within parenthesis
// // JSON.parse   -  json string convert into js array ; written outside

let student = {
    name:"surpanaka",
    age:32
}

localStorage.setItem("details",JSON.stringify(student))

let c = JSON.parse(localStorage.getItem("details"));
console.log(c['name'])  // console.log(c.name)


localStorage.clear()
// signup form with name password (n,p in local storage) and submit(go to login page (name,password)-->{same as n,p in local storage} submit) button 
// home page
// setn,p in local storage to login using get  
// if incorrrect must get entered details are incorrect


// window.location.href = (page path like) "homepage.html"
// one js has set items another has get items 


// second task:
// input box add button like to do list 