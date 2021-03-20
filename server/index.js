var server = require('wss').Server;
var s = new server({port: 8000});
var cli_count = 0;
const TIMEOUT = 5 //seconds

function noop() {}

function heartbeat() {
  this.isAlive = true;
  // console.log('pong kittito')
}

s.on('connection', function(ws, req) {
	cli_count += 1;
	const ip = req.socket.remoteAddress; //optional

	console.log("Client " + cli_count + " connected. IP address: "+ip);

	ws.isAlive = true;
	ws.on('pong', heartbeat);
	// ws.on('open', function(ws) {
		
	// });
	// ws.send('ping', function(ws) {
	// 	console.log("Sent ping");
	// })
	ws.on('close', function() {
		console.log("Client " + cli_count + " disconnected");
		cli_count -= 1;
		clearInterval(interval);
	});
});

const interval = setInterval(function ping() {
  s.clients.forEach(function each(ws) {
    if (ws.isAlive === false) return ws.terminate();

    ws.isAlive = false;
    ws.ping(noop);
  });
}, TIMEOUT*1000);
