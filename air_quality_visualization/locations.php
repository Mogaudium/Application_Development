<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');

require_once 'config.php';
require_once 'Database.php';

$db = new Database($config);
$result = $db->getLocations();
echo json_encode($result);
?>
