var sys = require("sys");
var exec = require("child_process").exec;
var socket = require("socket.io-client")("http://1920.lakeside-cs.org:6544/");
var path = "~";
const fs = require('fs');

socket.on("controls message", function(msg){
	fs.writeFile("controls", msg, function(err) {
	    if(err) {
	        return console.log(err);
	    }
	});
});
