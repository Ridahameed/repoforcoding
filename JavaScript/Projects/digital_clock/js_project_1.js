const hoursE1 = document.getElementById("hour")
const miutesE1 = document.getElementById("min")
const secondE1 = document.getElementById("sec")
const newLocal = document.getElementById("amp")
const ampmE1 = document.getElementById("am_pm")

function updateClock(){
    let h = new Date().getHours()
    let m = new Date().getMinutes()
    let s = new Date().getSeconds()
    let am_pm = "AM"

    if (h > 12){
        h = h- 12
        am_pm = "PM"
    }

    h = h < 10 ? "0" + h : h;
    m = m < 10 ? "0" + m : m;
    s = s < 10 ? "0" + s : s;

    hoursE1.innerText= h;
    miutesE1.innerText= m;
    secondE1.innerText= s;
    ampmE1,(innerText= am_pm);
    setTimeout(()=>{
        updateClock()

    }, 1000)
}
updateClock()