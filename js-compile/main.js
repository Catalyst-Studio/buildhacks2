var hop = require('@onehop/client')

const client = hop.hop.init( {projectId: "project_NDk2MTQxMTE0NTc3MTAxNDk"} )

client.on('CONNECTION_STATE_UPDATE', (state) => {
    console.log(state);
    if (state === "connected") {
        client.subscribeToChannel("test");
    }
});

client.on("MESSAGE", ({event, data}) => console.log);