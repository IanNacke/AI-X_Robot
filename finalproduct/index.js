var app = require('express')();
var http = require('http').createServer(app);
var io = require('/home/student1920/.nvm/versions/node/v13.0.1/lib/node_modules/socket.io')(http);
var password = "rds123";

var piConnStatus = false;

var connections = 0;
var lastConnection;

app.get('/', function(req, res){
  res.sendFile(__dirname + "/");
});

io.on('connection', function(socket){
  console.log('user connected [' + connections + ']');
  socket.id = 10+connections;
  io.emit('server message', "user #" + connections + " connected [Pi connection status: " + piConnStatus + "] (btw, only the oldest client will be allowed to interact on the console)");
  socket.on('disconnect', function(){
    console.log('user disconnected');
    if(socket.id < 10)
	    connections--;
    io.emit('server message', "user disconnected");
    if(socket.id == 91){
      piConnStatus = false;
      io.emit('server message', "Pi disconnected");
    }
  });


  socket.on('controls message', function(msg)
  {
      console.log(msg);
      io.emit('controls message', msg);
  });


  socket.on('client message', function(msg){
    if(socket.id < 2)
    {
      console.log('client: '+msg);
      io.emit('client message', msg);
    }
  });
  socket.on('pi message', function(msg){
    console.log("pi: "+msg);
    piConnStatus = true;
    socket.id = 91;
    io.emit('pi message', msg);
  });
  socket.on('path message', function(msg){
    io.emit('path message', msg);
  });

  socket.on('image message', function(msg){
    console.log("imgdata send");
    io.emit('image message', msg);
  });

  socket.on('nano in', function(msg){
    console.log("nano in: " + msg);
    io.emit('nano in', msg);
  });

  socket.on('nano out', function(msg){
    console.log("nano out: " + msg);
    io.emit('nano out', msg);
  });

  socket.on('password', function(msg){
    if(msg == password){
      connections++;
      socket.id = connections;
    } else {
      socket.id = 10+connections;
      console.log(socket.id + " got the password wrong");
      socket.emit('password', "incorrect");
    }
  });
});


http.listen(6544, function(){
  console.log('listening on *:6544');
});
