var sys = require('sys');
var exec = require('child_process').exec;
var socket = require('socket.io-client')('http://1920.lakeside-cs.org:6543/');

socket.emit('pi message', "pi is connected!");

socket.on('client message', function(msg){
	console.log("CLIENT: "+msg);
	child = exec(msg, function (error, stdout, stderr) {
		socket.emit('pi message', stdout + stderr);
	});
});

socket.on('server message', function(msg){
	console.log("SERVER: "+msg);
});