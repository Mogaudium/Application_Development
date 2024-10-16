<?php

class Database {
    private $pdo;
    private $lastQuery;

    public function __construct($config) {
        try {
            $this->pdo = new PDO(
                "mysql:host={$config['host']};dbname={$config['database']}",
                $config['username'],
                $config['password']
            );
        } catch (PDOException $e) {
            die("Failed to connect to database: " . $e->getMessage());
        }
    }

    public function getAqiData($location, $from_date, $to_date) {
        $sql = "SELECT id, location, date, aqi, parameter FROM aqi_data WHERE location = :location AND date BETWEEN :from_date AND :to_date";
        $stmt = $this->pdo->prepare($sql);
        $stmt->bindParam(':location', $location);
        $stmt->bindParam(':from_date', $from_date);
        $stmt->bindParam(':to_date', $to_date);
        $stmt->execute();
        
        // Save the executed query
        $this->lastQuery = $stmt->queryString;

        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    public function getLocations() {
        $sql = "SELECT DISTINCT location FROM aqi_data ORDER BY location";
        $stmt = $this->pdo->query($sql);
    
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }
    

    // Add the getLastQuery() method
    public function getLastQuery() {
        return $this->lastQuery;
    }
}
