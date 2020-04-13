var app = require('express')();
var http = require('http').createServer(app);
var io = require('/home/student1920/.nvm/versions/node/v13.0.1/lib/node_modules/socket.io')(http);
var cleintTimestamp = 0;
var piTimestamp = 0;

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
    cleintTimestamp = msg.substring(0,msg.indexOf("|"));
    console.log('client: '+msg);
    io.emit('client message', msg);
  });
  socket.on('pi message', function(msg){
    console.log("pi: "+msg);
    piTimestamp = msg.substring(0,msg.indexOf("|"));
    io.emit('server message', "Delay of "+(piTimestamp-cleintTimestamp) + " milliseconds");
    io.emit('pi message', msg);
  });
});

http.listen(6543, function(){
  console.log('listening on *:6543');
});
