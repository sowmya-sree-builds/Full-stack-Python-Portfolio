let d=document.getElementById("helllo")
d.className = one

// d.classList.add("one","two")
// d.classList.remove("two")
d.classList.replace("two","one")

let p = d.classList.contains("two");
console.log(p)

// toggle  -- add and remove

// d.classList.toggle("one")