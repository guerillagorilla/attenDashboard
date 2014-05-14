var http = require('http')
var net = require('net');
//var readline = require('readline');
var client = net.connect(3001, '172.30.0.100');

client.on('data', function(data) {

	http.createServer(function (request, response) {
    	response.writeHead(200, {'Content-Type': 'text/plain'});
    	response.write(data.toString());
    	console.log(data);
    	response.end();

    	client.write('RAA\n');
		client.write('DIS\n');

		}).listen(8081, '205.243.57.130');
		console.log('Server running at http://205.243.57.1300:8080/');

});

client.on('error', function(err) {
    console.log('error:', err.message);
});
