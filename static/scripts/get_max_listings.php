<?php

$url = "http://www.boxhippo.com/whmcs/includes/api.php";
$username = "matthew";
$password = "th4t0ldSong!";
$email = $argv[1];


$postfields = array();
$postfields["username"] = $username;
$postfields["password"] = md5($password);
$postfields["action"] = "getclientsproducts";
$postfields["email"] = $email;
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

$arr = json_decode($jsondata, true);


$just_products = $arr['products']['product'];


$max_listings = 0;
for($x = 0; $x < count($just_products); $x++) {
  if($just_products[$x]['pid'] == '1') {
    $max_listings = $max_listings + 1;
  }
  if($just_products[$x]['pid'] == '2') {
    $max_listings = $max_listings + 3;
  }
  if($just_products[$x]['pid'] == '3') {
    $max_listings = -1;
    break;
  }
}

echo "$max_listings";
