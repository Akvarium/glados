<html>
 <head>
<meta http-equiv="content-type" content="text/html; charset=utf-8"></meta>
  <title> YAY! </title>
   </head>
   <body>



<?php
$IP=$_SERVER['REMOTE_ADDR'];
$img="ipfire_tux_256x256.png";
$ADMPORT=5000;
$ADMIP="10.254.12.59";
$msg="";

$sock = socket_create(AF_INET, SOCK_DGRAM, SOL_UDP);
$v = file_get_contents("http://".$ADMIP."/active");

if ( substr_count($v, $IP) > 0) {
  $img="worldTux.png";
  $msg="You have internetz!";
}

// "når du trykker på knappen"
if(isset($_POST['user'])){

//$pass = base64_encode($_POST['pass']);
$pass = $_POST['pass'];
$user = $_POST['user'];
$cmd = "./auth.py ".$user." '".$pass."'";
exec($cmd, $out);
if ( substr_count($v, $user) > 0){
$msg="nah ah ah you can't login more than once $user";
$img="lol.png";

} elseif ( $out[0] == "True") {



$msg = 'add '.$user.' '.$IP;
if($img=="worldTux.png") {
$msg = 'del '.$user.' '.$IP;
}
$len = strlen($msg);

socket_sendto($sock, $msg, $len, 0, $ADMIP, $ADMPORT);
socket_close($sock);

header("Refresh:0");
} else {
$msg="nah ah ah you didn't say the magic word";
$img='lol.gif';


 
}


 }
?>

        <center>
        <br>
        <img src=<?php echo $img; ?> width="256" height="256">
        <br><b>Logg inn</b><br><br>
        <form method="POST">
        Brukernavn:<br>
        <input type="text" name="user"><br>
        Passord:<br>
        <input type="password" name="pass"><br><input value="internetz?" type="submit"></form>
        </center>
	<br>
	<br>
	<?php echo $msg; ?>
	<br>
	<?php echo $IP; ?>


   </body>
 </html>

