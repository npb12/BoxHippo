<?php

$url = "http://www.boxhippo.com/whmcs/includes/api.php";
$username = "matthew";
$password = "th4t0ldSong!";

$email = $argv[1];
$pass2 = $argv[2];

$postfields = array();
$postfields["username"] = $username;
$postfields["password"] = md5($password);
$postfields["action"] = "addclient";
$postfields["email"] = $email;
$postfields["country"] = "US";
$postfields["password2"] = $pass2;
$postfields["responsetype"] = "json";

echo $email;
echo "\n";
echo $pass2;
echo "\n";

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

$arr = json_decode($jsondata, true);

print_r($arr);

?>
