let data = [
    {
        image: "https://th.bing.com/th/id/OIP.YgMdB1OTpldRP7-LBqz-uAHaHa?w=192&h=187&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
        title: "laptop",
        desc: "this is a laptop",
        price: 30000
    },
    {
        image: "https://th.bing.com/th/id/OIP.YgMdB1OTpldRP7-LBqz-uAHaHa?w=192&h=187&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
        title: "mobile",
        desc: "this is a mobile",
        price: 15000
    },
    {
        image: "https://th.bing.com/th/id/OIP.YgMdB1OTpldRP7-LBqz-uAHaHa?w=192&h=187&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
        title: "tv",
        desc: "this is a tv",
        price: 18000
    },
    {
        image: "https://th.bing.com/th/id/OIP.YgMdB1OTpldRP7-LBqz-uAHaHa?w=192&h=187&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
        title: "laptop",
        desc: "this is a laptop",
        price: 30000
    },
    {
        image: "https://th.bing.com/th/id/OIP.YgMdB1OTpldRP7-LBqz-uAHaHa?w=192&h=187&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
        title: "mobile",
        desc: "this is a mobile",
        price: 15000
    },
    {
        image: "https://th.bing.com/th/id/OIP.YgMdB1OTpldRP7-LBqz-uAHaHa?w=192&h=187&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
        title: "tv",
        desc: "this is a tv",
        price: 18000
    }
];

let container = document.getElementById("container");

let output = data.map(item => {
    return `
        <div class="card">
            <img src="${item.image}">
            <h2>${item.title}</h2>
            <p>${item.desc}</p>
            <span class="price">${item.price}</span>
        </div>
    `;
});

container.innerHTML = output.join("");
