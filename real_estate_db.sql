-- MySQL dump 10.13  Distrib 8.0.46, for Win64 (x86_64)
--
-- Host: localhost    Database: real_estate_db
-- ------------------------------------------------------
-- Server version	8.0.46

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `properties`
--

DROP TABLE IF EXISTS `properties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `properties` (
  `propertyId` varchar(50) NOT NULL,
  `title` varchar(150) NOT NULL,
  `propertyType` varchar(50) DEFAULT NULL,
  `locality` varchar(100) DEFAULT NULL,
  `bedrooms` int DEFAULT NULL,
  `price` decimal(15,2) DEFAULT NULL,
  `areaSqFt` int DEFAULT NULL,
  `amenities` text,
  `description` text NOT NULL,
  `listingStatus` varchar(30) DEFAULT 'Available',
  PRIMARY KEY (`propertyId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `properties`
--

LOCK TABLES `properties` WRITE;
/*!40000 ALTER TABLE `properties` DISABLE KEYS */;
INSERT INTO `properties` VALUES ('P001','2 BHK Flat','Apartment','Ahmedabad',2,4500000.00,1100,'Lift, Parking','Beautiful 2 BHK flat with lift and parking','Available'),('P002','3 BHK Luxury Flat','Apartment','Gandhinagar',3,7500000.00,1600,'Gym, Garden','Spacious 3 BHK flat with gym and garden','Available'),('P003','1 BHK Affordable Flat','Apartment','Ahmedabad',1,2500000.00,650,'Parking','Affordable flat for a small family','Available'),('P004','Residential Plot','Plot','Gandhinagar',0,3500000.00,1500,'Road, Water','Residential plot with road and water facility','Available'),('P005','4 BHK Villa','Villa','Ahmedabad',4,12000000.00,2500,'Pool, Garden','Luxury villa with swimming pool and garden','Available');
/*!40000 ALTER TABLE `properties` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-11-01 19:30:07
