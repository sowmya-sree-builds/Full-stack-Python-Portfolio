//perform addition, subtraction using function declaration

//perform multiplication, division using function expression

//print your family members names one by one using fd

//print "my name is abc my loc is hyd my age is 22"

//using method objects (keys name, loc, age, data)


function operation1(a, b) {
    console.log(`addition: ${a + b}`);
    console.log(`substraction: ${a - b}`);
}

operation1(5, 3);

const operation2=function(a,b){
    console.log(`multiplication: ${a * b}`);
    console.log(`division: ${a / b}`);
}

operation2(5,3);

function familyMembers() {
    console.log("Father: Nagesh");
    console.log("Mother: Rupa");
    console.log("Brother: Dhanu");
    console.log("Sister: Kavya");
    console.log("Me: Sowmya");
}

familyMembers();



let person = {
    name: "Sowmya",
    loc: "Hyderabad",
    age: 21,
    data: function () {
        console.log(`my name is ${this.name} my loc is ${this.loc} my age is ${this.age}`);
    }
};

person.data();