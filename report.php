<?php

$date_1 = $_POST['date_1'];
$user = getallheaders()['User'];

//echo $date_1  . "<br>";
echo $date_1 . " Bedtime Set <br>";
if(!empty($_POST['date_1'])){
$data = $_POST['date_1'];
$fname = strtoupper($user) . ".txt";//generates random name
$file = fopen("/scripts/bedTime/userFiles/" .$fname, 'w');//creates new file
fwrite($file, $data);
fclose($file);
}
?>

