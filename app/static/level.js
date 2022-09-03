const base_url = window.location.host;
const path = window.location.pathname;
console.log(base_url);
var ws_url = 'ws://' + base_url + '/level';
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