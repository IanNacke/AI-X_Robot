<?php
session_start();
?>
<!DOCTYPE html>
<html>
	<head>
	</head>
	<body>
	<h1>Log in:</h1>
	<form action="ssh.php" method="post" enctype="multipart/form-data">
		<h2>Type </h2>
		<select name = "type" required>
		<option value = pi> pi</option>
		<option value = client> client</option>
		<input type="submit" value="submit" name="submit">
	</form>
	</body>
</html>