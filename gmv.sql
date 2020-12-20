-- MySQL dump 10.13  Distrib 8.0.21, for Linux (x86_64)
--
-- Host: localhost    Database: gmv
-- ------------------------------------------------------
-- Server version	8.0.21-0ubuntu0.20.04.4

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Dealers`
--

DROP TABLE IF EXISTS `Dealers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Dealers` (
  `Fname` varchar(20) NOT NULL,
  `Mname` varchar(20) DEFAULT NULL,
  `Lname` varchar(20) NOT NULL,
  `Commission` decimal(4,2) DEFAULT NULL,
  `PhoneNo` varchar(10) NOT NULL,
  `HouseNo` int NOT NULL,
  `Area` varchar(20) NOT NULL,
  `City` varchar(20) NOT NULL,
  PRIMARY KEY (`PhoneNo`),
  CONSTRAINT `Dealers_chk_1` CHECK ((`Commission` > 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Dealers`
--

LOCK TABLES `Dealers` WRITE;
/*!40000 ALTER TABLE `Dealers` DISABLE KEYS */;
INSERT INTO `Dealers` VALUES ('john','danger','hammoc',3.90,'1234567809',1,'kombi','chennai'),('mohammed',NULL,'inshan',4.20,'1234567890',1,'kukatpally','hyd'),('tanya',NULL,'isabel',6.90,'1234567980',1,'padra','vadora');
/*!40000 ALTER TABLE `Dealers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Departments`
--

DROP TABLE IF EXISTS `Departments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Departments` (
  `ID` int NOT NULL,
  `Dname` varchar(30) NOT NULL,
  `Employee_count` int DEFAULT NULL,
  `Manager_ID` bigint DEFAULT NULL,
  PRIMARY KEY (`ID`),
  CONSTRAINT `Departments_chk_1` CHECK ((`Employee_count` > 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Departments`
--

LOCK TABLES `Departments` WRITE;
/*!40000 ALTER TABLE `Departments` DISABLE KEYS */;
INSERT INTO `Departments` VALUES (1,'woodstuff',3,12),(2,'cushionstuff',5,13);
/*!40000 ALTER TABLE `Departments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Employee`
--

DROP TABLE IF EXISTS `Employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Employee` (
  `PhoneNo` varchar(10) NOT NULL,
  `Fname` varchar(20) NOT NULL,
  `Mname` varchar(20) DEFAULT NULL,
  `Lname` varchar(20) NOT NULL,
  `Employee_ID` bigint NOT NULL,
  `Dno` int NOT NULL DEFAULT '0',
  `DOB` date NOT NULL,
  `HouseNo` int NOT NULL,
  `Area` varchar(20) NOT NULL,
  `City` varchar(20) NOT NULL,
  PRIMARY KEY (`Employee_ID`,`Dno`),
  KEY `Dno` (`Dno`),
  CONSTRAINT `Employee_ibfk_1` FOREIGN KEY (`Dno`) REFERENCES `Departments` (`ID`) ON DELETE SET DEFAULT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Employee`
--

LOCK TABLES `Employee` WRITE;
/*!40000 ALTER TABLE `Employee` DISABLE KEYS */;
INSERT INTO `Employee` VALUES ('2345678903','james','007','bond',1,1,'1981-09-09',1,'continental','new york'),('2345678904','tom',NULL,'cruise',2,1,'1982-09-09',91,'continental','new york'),('2345678905','naruto','awesome','uzumaki',3,2,'1990-09-09',420,'leaf village','ching chong'),('2345678906','boruto','shitty','uzumaki',4,2,'2002-09-09',56,'leaf','village'),('2345678907','nezuko','demon','tanjiro',5,2,'2010-09-09',78,'demon','world'),('2345678908','jai','dumass','ganesh',6,2,'1980-09-09',69,'dumb','town'),('2345678901','john','baba ya ga','wick',12,1,'1980-09-09',69,'continental','new york'),('2345678902','shin',NULL,'chan',13,2,'2001-09-11',42,'utaba','tokyo');
/*!40000 ALTER TABLE `Employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Full_time_Emp`
--

DROP TABLE IF EXISTS `Full_time_Emp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Full_time_Emp` (
  `Emp_ID` bigint NOT NULL,
  `salary` decimal(8,2) NOT NULL,
  `Dno` int NOT NULL,
  PRIMARY KEY (`Emp_ID`,`Dno`),
  KEY `Dno` (`Dno`),
  CONSTRAINT `Full_time_Emp_ibfk_1` FOREIGN KEY (`Emp_ID`) REFERENCES `Employee` (`Employee_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Full_time_Emp_ibfk_2` FOREIGN KEY (`Dno`) REFERENCES `Employee` (`Dno`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Full_time_Emp`
--

LOCK TABLES `Full_time_Emp` WRITE;
/*!40000 ALTER TABLE `Full_time_Emp` DISABLE KEYS */;
INSERT INTO `Full_time_Emp` VALUES (5,800000.00,2),(12,100000.00,1),(13,100069.00,2);
/*!40000 ALTER TABLE `Full_time_Emp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Make_Products`
--

DROP TABLE IF EXISTS `Make_Products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Make_Products` (
  `Name` varchar(30) NOT NULL,
  `Emp_ID` bigint NOT NULL,
  `Dept_ID` int NOT NULL,
  PRIMARY KEY (`Emp_ID`,`Dept_ID`,`Name`),
  KEY `Dept_ID` (`Dept_ID`,`Name`),
  CONSTRAINT `Make_Products_ibfk_1` FOREIGN KEY (`Dept_ID`, `Name`) REFERENCES `Products` (`Dept_ID`, `Name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Make_Products_ibfk_2` FOREIGN KEY (`Emp_ID`) REFERENCES `Employee` (`Employee_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Make_Products_ibfk_3` FOREIGN KEY (`Dept_ID`) REFERENCES `Departments` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Make_Products`
--

LOCK TABLES `Make_Products` WRITE;
/*!40000 ALTER TABLE `Make_Products` DISABLE KEYS */;
INSERT INTO `Make_Products` VALUES ('bed frame',1,1),('coaxial bed frame',2,1),('bed',4,2),('bed cover',6,2),('cushions',5,2),('memory foam',3,2);
/*!40000 ALTER TABLE `Make_Products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Mat_supply`
--

DROP TABLE IF EXISTS `Mat_supply`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Mat_supply` (
  `Phoneno` varchar(10) NOT NULL,
  `Materials_supplied` varchar(50) NOT NULL,
  PRIMARY KEY (`Phoneno`,`Materials_supplied`),
  CONSTRAINT `Mat_supply_ibfk_1` FOREIGN KEY (`Phoneno`) REFERENCES `suppliers` (`Phoneno`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Mat_supply`
--

LOCK TABLES `Mat_supply` WRITE;
/*!40000 ALTER TABLE `Mat_supply` DISABLE KEYS */;
INSERT INTO `Mat_supply` VALUES ('1234567809','fabric'),('1234567809','glue'),('1234567809','nails'),('1234567809','varnish'),('1234567809','wood'),('1234567890','glue'),('1234567890','varnish'),('1234567890','wood'),('1234567980','foam'),('1234567980','plastics'),('1234567980','raw memory foam');
/*!40000 ALTER TABLE `Mat_supply` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Part_time_Emp`
--

DROP TABLE IF EXISTS `Part_time_Emp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Part_time_Emp` (
  `Emp_ID` bigint NOT NULL,
  `hourly_wage` decimal(7,2) NOT NULL,
  `Contract_duration` varchar(4) NOT NULL,
  `Dno` int NOT NULL,
  PRIMARY KEY (`Emp_ID`,`Dno`),
  KEY `Dno` (`Dno`),
  CONSTRAINT `Part_time_Emp_ibfk_1` FOREIGN KEY (`Emp_ID`) REFERENCES `Employee` (`Employee_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Part_time_Emp_ibfk_2` FOREIGN KEY (`Dno`) REFERENCES `Employee` (`Dno`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Part_time_Emp`
--

LOCK TABLES `Part_time_Emp` WRITE;
/*!40000 ALTER TABLE `Part_time_Emp` DISABLE KEYS */;
INSERT INTO `Part_time_Emp` VALUES (1,10.50,'1221',1),(2,21.00,'1221',1),(3,15.00,'1221',2),(4,5.00,'1221',2),(6,0.01,'1299',2);
/*!40000 ALTER TABLE `Part_time_Emp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Prod_Supply`
--

DROP TABLE IF EXISTS `Prod_Supply`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Prod_Supply` (
  `phone_number` varchar(10) NOT NULL,
  `products_supplied` varchar(30) NOT NULL,
  PRIMARY KEY (`phone_number`,`products_supplied`),
  CONSTRAINT `Prod_Supply_ibfk_1` FOREIGN KEY (`phone_number`) REFERENCES `Dealers` (`PhoneNo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Prod_Supply`
--

LOCK TABLES `Prod_Supply` WRITE;
/*!40000 ALTER TABLE `Prod_Supply` DISABLE KEYS */;
INSERT INTO `Prod_Supply` VALUES ('1234567809','bed frame'),('1234567809','memory foam'),('1234567890','bed'),('1234567890','bed frame'),('1234567890','memory foam'),('1234567980','bed frame'),('1234567980','coaxial bed frame'),('1234567980','memory foam');
/*!40000 ALTER TABLE `Prod_Supply` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Products`
--

DROP TABLE IF EXISTS `Products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Products` (
  `Quantities` int NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Dept_ID` int NOT NULL,
  `price` int NOT NULL,
  PRIMARY KEY (`Dept_ID`,`Name`),
  CONSTRAINT `Products_ibfk_1` FOREIGN KEY (`Dept_ID`) REFERENCES `Departments` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Products_chk_1` CHECK (((`price` > 0) and (`Quantities` > 0)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Products`
--

LOCK TABLES `Products` WRITE;
/*!40000 ALTER TABLE `Products` DISABLE KEYS */;
INSERT INTO `Products` VALUES (100,'bed frame',1,10000),(20,'coaxial bed frame',1,20000),(100,'bed',2,3000),(420,'bed cover',2,420),(1000,'cushions',2,300),(100,'memory foam',2,6969);
/*!40000 ALTER TABLE `Products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Raw_materials_supply`
--

DROP TABLE IF EXISTS `Raw_materials_supply`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Raw_materials_supply` (
  `Sup_PhNo` varchar(10) NOT NULL,
  `Dep_ID` int NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Quantities` int DEFAULT NULL,
  PRIMARY KEY (`Dep_ID`,`Sup_PhNo`,`Name`),
  KEY `Sup_PhNo` (`Sup_PhNo`),
  CONSTRAINT `Raw_materials_supply_ibfk_1` FOREIGN KEY (`Sup_PhNo`) REFERENCES `suppliers` (`Phoneno`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Raw_materials_supply_ibfk_2` FOREIGN KEY (`Dep_ID`) REFERENCES `Departments` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Raw_materials_supply_chk_1` CHECK ((`Quantities` > 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Raw_materials_supply`
--

LOCK TABLES `Raw_materials_supply` WRITE;
/*!40000 ALTER TABLE `Raw_materials_supply` DISABLE KEYS */;
INSERT INTO `Raw_materials_supply` VALUES ('1234567809',1,'fabric',1000),('1234567809',1,'glue',200),('1234567809',1,'nails',1000),('1234567890',1,'varnish',150),('1234567890',1,'wood',150),('1234567980',2,'foam',100),('1234567980',2,'plastics',122),('1234567980',2,'raw memory foam',297);
/*!40000 ALTER TABLE `Raw_materials_supply` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Sell_Products`
--

DROP TABLE IF EXISTS `Sell_Products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Sell_Products` (
  `Name` varchar(30) NOT NULL,
  `Dealer_PhNo` varchar(10) NOT NULL,
  `Dept_ID` int NOT NULL,
  PRIMARY KEY (`Dealer_PhNo`,`Dept_ID`,`Name`),
  KEY `Dept_ID` (`Dept_ID`,`Name`),
  CONSTRAINT `Sell_Products_ibfk_1` FOREIGN KEY (`Dept_ID`, `Name`) REFERENCES `Products` (`Dept_ID`, `Name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Sell_Products_ibfk_2` FOREIGN KEY (`Dealer_PhNo`) REFERENCES `Dealers` (`PhoneNo`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Sell_Products_ibfk_3` FOREIGN KEY (`Dept_ID`) REFERENCES `Departments` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Sell_Products`
--

LOCK TABLES `Sell_Products` WRITE;
/*!40000 ALTER TABLE `Sell_Products` DISABLE KEYS */;
INSERT INTO `Sell_Products` VALUES ('bed frame','1234567809',1),('bed frame','1234567890',1),('bed frame','1234567980',1),('coaxial bed frame','1234567980',1),('bed','1234567890',2),('memory foam','1234567809',2),('memory foam','1234567890',2),('memory foam','1234567980',2);
/*!40000 ALTER TABLE `Sell_Products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suppliers`
--

DROP TABLE IF EXISTS `suppliers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suppliers` (
  `Phoneno` varchar(10) NOT NULL,
  `Houseno` int NOT NULL,
  `area` varchar(20) NOT NULL,
  `city` varchar(20) NOT NULL,
  `Supply_frequency` int NOT NULL,
  `Fname` varchar(20) NOT NULL,
  `Mname` varchar(20) DEFAULT NULL,
  `Lname` varchar(20) NOT NULL,
  PRIMARY KEY (`Phoneno`),
  CONSTRAINT `suppliers_chk_1` CHECK ((`Supply_frequency` > 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suppliers`
--

LOCK TABLES `suppliers` WRITE;
/*!40000 ALTER TABLE `suppliers` DISABLE KEYS */;
INSERT INTO `suppliers` VALUES ('1234567809',69,'chhya','porbandar',9,'rocky',NULL,'babloa'),('1234567890',32,'bachupally','hyd',7,'damian',NULL,'wayne'),('1234567980',420,'chembur','mumbai',4,'bruce',NULL,'wayne');
/*!40000 ALTER TABLE `suppliers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-06 16:03:12
