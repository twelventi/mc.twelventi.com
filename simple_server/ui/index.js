
let webhook_url = "/api/submission";
const urlParams = new URLSearchParams(window.location.search);
let identityt = undefined;
if (urlParams.has('it')) {
    identityt = urlParams.get("it");
    history.pushState({}, null, location.protocol + '//' + location.host + location.pathname);
}
window.onload = (e) => {
    let username_element = document.querySelector('#minecraft-name');
    function processForm(e) {
        if (e.preventDefault) e.preventDefault();

        if (identityt) {
            fetch(
                webhook_url,
                {
                    method: "post",
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    //make sure to serialize your JSON body
                    body: JSON.stringify({
                        name: username_element.value,
                        code: identityt
                    })
                }
            ).then(resp => {
                if (resp.success) {
                    localStorage.identityt = identityt;
                    localStorage.username = username_element.value;
                }
            })
        }
        username_element.value = ""
        // You must return false to prevent the default form behavior
        return false;
    }

    let form = document.getElementById('submit-form');
    if (form.attachEvent) {
        form.attachEvent("submit", processForm);
    } else {
        form.addEventListener("submit", processForm);
    }


    //Stolen from https://www.w3schools.com/howto/howto_js_countdown.asp
    // Set the date we're counting down to
    var countDownDate = new Date("Dec 14, 2021 19:00:00").getTime();

    // Update the count down every 1 second
    var x = setInterval(function () {

        // Get today's date and time
        var now = new Date().getTime();

        // Find the distance between now and the count down date
        var distance = countDownDate - now;

        // Time calculations for days, hours, minutes and seconds
        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Display the result in the element with id="demo"
        document.getElementById("countdown-timer").innerHTML = days + "d | " + hours + "h | "
            + minutes + "m | " + seconds + "s ";

        // If the count down is finished, write some text
        if (distance < 0) {
            clearInterval(x);
            document.getElementById("countdown-timer").innerHTML = "LAUNCHING SOON! CONNECT TO mc.twelventi.com in your Minecraft Client!";
        }
    }, 1000);
}