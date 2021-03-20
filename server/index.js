var server = require('wss').Server;
var s = new server({port: 8000});
var cli_count = 0;

s.on('connection', function(ws, req) {
	cli_count += 1;
	const ip = req.socket.remoteAddress; //optional

	console.log("Client " + cli_count + " connected. IP address: "+ip);

	// ws.on('message', function(ws) {
		
	// });
	
	ws.on('close', function() {
		console.log("Client " + cli_count + " disconnected");
		cli_count -= 1;
	});
});

