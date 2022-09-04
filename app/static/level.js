const base_url = window.location.host;
const path = window.location.pathname;
console.log(base_url);
const levelname = document.getElementById("levelname").className
const levelnum = document.getElementById("levelnum").className
const username = document.getElementById("username").className;
var ws_url = 'wss://' + base_url + '/level/' + levelname + '/' + levelnum;
console.log(ws_url);
var ws = new WebSocket(ws_url);
var editor = ace.edit("editor");
const guessCode = async () => {
    const code = editor.getValue()
    ws.send(code)
    ws.onmessage = function (event) {
        const data = JSON.parse(event.data);
        const type = data.type;
        let message = data.message;
        console.log(message)
        if (type === "good") {
            const doc = document.getElementById("message");
            doc.className = "ms-label ms-action2";
            doc.innerText = message;
            ws.close()
        }
        else if (type === "bad") {
            const doc = document.getElementById("message");
            doc.className = "ms-label ms-primary";
            doc.innerText = message;
        }
    }
}
ws_url = 'wss://' + base_url + '/api/chat/' + username;
var wschat = new WebSocket(ws_url);
function sendMessage() {
    const message = document.getElementById("message_send");
    let data = {
        "username": username,
        "message": message.value
    };
    message.value = ""
    wschat.send(JSON.stringify(data));
}

wschat.onmessage = function (event) {
    const data = JSON.parse(event.data);
    const user = data.username;
    const message = data.message;
    const div = document.getElementById("scroll-bar-hidden");
    const code = '<p><b>' + user + '</b>: ' + message;
    div.innerHTML += code;
    div.scrollTop = div.scrollHeight;
};