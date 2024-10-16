<?php
header('Content-Type: application/json');

require_once 'config.php';
require_once 'Database.php';

$location = $_GET['location'] ?? '';
$from_date = $_GET['from_date'] ?? '';
$to_date = $_GET['to_date'] ?? '';

$db = new Database($config);
$result = $db->getAqiData($location, $from_date, $to_date);
echo json_encode($result);
?>
