<?php

$url = "http://www.boxhippo.com/whmcs/whmcs/includes/api.php";
$username = "matthew";
$password = "th4t0ldSong!";

$postfields = array();
$postfields["username"] = $username;
$postfields["password"] = md5($password);
$postfields["action"] = "get_clients";
$postfields["responsetype"] = "json";

$query_string = "";
foreach ($postfields AS $k=>$v) $query_string .= "$k=".urlencode($v)."&";

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_TIMEOUT, 30);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, $query_string);
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
$jsondata = curl_exec($ch);

if (curl_error($ch)) die("Connection Error: ".curl_errno($ch).' - '.curl_error($ch));
curl_close($ch);

$arr = json_decode($jsondata);

print_r($arr);

 echo "<textarea rows=50 cols=100>Request: ".print_r($postfields,true);
  echo "\nResponse: ".htmlentities($jsondata)."\n\nArray: ".print_r($arr,true);
   echo "</textarea>";

?>
