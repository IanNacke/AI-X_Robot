<?php
session_start();
?>
<!DOCTYPE html>
<html>
	<head>
	</head>
	<body>
	<?php
	$_SESSION['type']= "";
		if($_SERVER["REQUEST_METHOD"] == "POST"	){
			if($_POST['type'] = 'pi'){
				$_SESSION['type'] = 'pi'
			}
			else{
				$_SESSION['type'] = 'client'
			}
		}
	?>
	</body>
</html>