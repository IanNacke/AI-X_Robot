<<<<<<< HEAD
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
=======
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
>>>>>>> be7c485b6be8c9146a53b869a563d9c4ad579355
</html>