var app = require('express')();
var http = require('http').createServer(app);
var io = require('/home/student1920/.nvm/versions/node/v13.0.1/lib/node_modules/socket.io')(http);

app.get('/', function(req, res){
  res.sendFile(__dirname + "/");
});

io.on('connection', function(socket){
  console.log('a user connected');
  io.emit('server message', "user connected");
  socket.on('disconnect', function(){
    console.log('user disconnected');
  });
  socket.on('client message', function(msg){
    console.log('client: '+msg);
    io.emit('client message', msg);
  });
  socket.on('pi message', function(msg){
    console.log("pi: "+msg);
    io.emit('pi message', msg);
  });

  socket.on('pi image data', function(msg){
    console.log("pi: "+msg);
    io.emit('pi message', msg);
  });
});

http.listen(6543, function(){
  console.log('listening on *:6543');
});
