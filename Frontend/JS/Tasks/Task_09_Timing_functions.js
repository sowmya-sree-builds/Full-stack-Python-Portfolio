function updateTime() {
    const now = new Date();

    let hours = now.getHours();
    let minutes = now.getMinutes();
    let seconds = now.getSeconds();

    hours = hours < 10 ? "0" + hours : hours;   // condition ? value_if_true : value_if_false
    minutes = minutes < 10 ? "0" + minutes : minutes;
    seconds = seconds < 10 ? "0" + seconds : seconds;

    document.getElementById("time").innerText =
        `${hours}:${minutes}:${seconds}`;                 // HH:MM:SS
}

setInterval(updateTime, 1000);
updateTime();