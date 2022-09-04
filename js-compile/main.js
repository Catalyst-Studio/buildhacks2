var hop = require('@onehop/client')

const client = hop.hop.init( {projectId: "project_NDk2MTQxMTE0NTc3MTAxNDk"} )

client.on('CONNECTION_STATE_UPDATE', (state) => {
    console.log(state);
    if (state === "connected") {
        client.subscribeToChannel("test");
    }
});
const channelId = "test";
client.on("MESSAGE", ({event, data}) => console.log(data));

client.channels.on('stateUpdate', (channelId, state) => {
    console.log(state)
});
