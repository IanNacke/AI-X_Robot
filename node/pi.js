var sys = require("sys");
var exec = require("child_process").exec;
var socket = require("socket.io-client")("http://1920.lakeside-cs.org:6544/");
var path = "~";

socket.emit("pi message", "pi is connected!");
socket.emit("path message", "path");

socket.on("client message", function(msg){
	console.log("CLIENT: "+msg);

	if(msg.includes("rm ")){
		socket.emit("pi message", "Removing files is not allowed for security reasons");
	}
	else if(msg.includes("&&")){
		socket.emit("pi message", "Chaining commands is not supported yet, sorry!");
	}
	else{
		var hasCd = false;
		var hasNano = false;
		if(msg.includes("cd ")){
			msg += " && pwd";
			hasCd = true;
		}
		else if(!msg.replace("/\s/g", " ").length){
			msg = "pwd";
		}
		else if(msg.includes("nano ")){
			msg = "cat" + msg.substring(msg.indexOf("o")+1);
			hasNano = true;
		}
		console.log("cd " + path + " && " + msg);
		child = exec("cd " + path + " && " + msg, function (error, stdout, stderr) {
			if(hasCd){
				path = stdout.replace("..." == null)
				socket.emit("nano out", msg.substring(4).replace("/\s/g", " ") + "|" + stdout);
			}
		});
	}
});

socket.on("server message", function(msg){
	console.log("SERVER: "+msg);
});

socket.on("nano in", function(msg){
	var filename = msg.substring(0,msg.indexOf("|")).replace("/\s/g", " ");
	var contents = msg.substring(msg.indexOf("|")+1);
	exec("cd " + path + " && mv " + filename +  " " + filename + ".backup", function(error, stdout, stderr){
		if(error == null){
			exec("cd " + path + " && echo " + contents + " > " + filename, function(error, stdout, stderr){
				if(error == null){
					exec("cd " + path + " && cat " + filename, function(error, stdout, stderr){
						socket.emit("pi message", stdout + stderr);
					});
				} else {
					socket.emit("pi message", stderr);
				}
			});
		} else {
			socket.emit("pi message", "mv " + filename + " " + filename + ".backup: " + stderr);
		}
	});
});

socket.on("disconnect", function(){
	console.log("Disconnected from server");
});

