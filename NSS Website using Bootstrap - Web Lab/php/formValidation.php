<?php
// define variables and set to empty values
$nameErr = $emailErrm= "";
$name = $email  = "";
$flag = 0;

function test_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  if (empty($_POST["textinput"])) {
    $nameErr = "Name is required";
    $flag = 1;
  } else {
    $name = test_input($_POST["textinput"]);
  }

  if (empty($_POST["mail"])) {
    $emailErr = "Email is required";
    $flag = 1;
  } else {
    $email = test_input($_POST["mail"]);
  }

  if (!preg_match("/^[a-zA-Z ]*$/",$name)) {
  $nameErr = "Only letters and white space allowed"; 
  $flag = 1;
  }

  if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
  $emailErr = "Invalid email format"; 
  $flag = 1;
  }

  if($flag == 0){
    echo "Your feedback is submitted";
  } else {
    echo "$nameErr";
    echo "$emailErr";
  }

}

extract($_POST);
$connect = mysql_connect("localhost", "root", "") or die("Connetion Failed");
mysql_select_db('nss') or die(mysql_error());
echo "Connected!";

$write = mysql_query("INSERT INTO feedback values ('$textinput', '$profession', '$organisation', '$mail', '$feedback')") or die(mysql_error());
$extract = mysql_query("SELECT * FROM feedback");
$group = mysql_query("SELECT * FROM feedback WHERE profession = 'student'");

while($row = mysql_fetch_assoc($extract)){
  $na = $row['name'];
  $fb = $row['comment'];
  echo "<br>$na 's feedback' : $fb";
}

echo "<br>----------------------------------------------------------------------------------------------------------------------------<br> <b>student feedbacks</b>";
while($row = mysql_fetch_assoc($group)){
  $na = $row['name'];
  $fb = $row['comment'];
  echo "<br>$na 's feedback' : $fb";
}


?>
