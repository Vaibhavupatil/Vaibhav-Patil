-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: project
-- ------------------------------------------------------
-- Server version	8.0.26

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
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) NOT NULL,
  `Address` varchar(255) NOT NULL,
  `Purchase_Items` varchar(255) DEFAULT NULL,
  `Quantity` int NOT NULL,
  `Phone_n` varchar(255) NOT NULL,
  `Product_amt` double NOT NULL,
  `Pay_amt` double NOT NULL,
  `Date` date DEFAULT NULL,
  `Remaining_amt` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'Sambha','Jalgaon',' 2burger and 5 breads',15,'0302464982',750,1500,'2011-01-20',-750),(2,'Gaurav','Nasik','1 burger and 10 breads',15,'0302464982',750,1200,'2010-02-25',-450),(3,'Tina','kalyan','9 burger and 10 breads',12,'0302464982',600,2000,'2000-02-25',-1400),(4,'Akash','Nanded','1 burger and 10 breads',9,'5602464982',450,100,'2012-02-25',350),(5,'Pratik','Mumbai','25 burger and 18 breads',10,'304446482',500,2000,'2000-02-25',-1500),(6,'Vicky','Thakur','1 burger and 10 breads',7,'1254458902',350,900,'2011-08-23',-550),(7,'ritik','Thane','22 burger and 20 breads',2,'1254458902',100,850,'2014-10-17',-750),(8,'roshan','Satara','25 burger and 20 breads',1,'1254458902',50,850,'2014-10-17',-800),(9,'Sagar','Sangli','25 burger and 20 breads',13,'2254458902',650,150,'2014-10-17',500),(10,'Kritika','Kolhapur','25 burger and 20 breads',18,'1254458902',900,180,'2019-10-17',720),(11,'Mitali','Thane','20 burger and 20 breads',23,'2254458902',1150,199,'2014-10-17',951),(12,'kiara','Latur','15 burger and 10 breads',16,'1254458902',800,112,'2017-10-17',688),(13,'Vaibhav','Sangmner','13 burger and 10 breads',19,'1254458902',950,58,'2017-10-17',892),(14,'Mital','Thane','20 burger and 20 breads',3,'2254458902',150,19,'2014-10-17',131),(15,'Vaishnav','Wagholi','113 burger and 110 breads',149,'1254458902',7450,18,'2012-10-17',7432);
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

mysql> desc customer;
+----------------+--------------+------+-----+---------+----------------+
| Field          | Type         | Null | Key | Default | Extra          |
+----------------+--------------+------+-----+---------+----------------+
| id             | int          | NO   | PRI | NULL    | auto_increment |
| Name           | varchar(255) | NO   |     | NULL    |                |
| Address        | varchar(255) | NO   |     | NULL    |                |
| Purchase_Items | varchar(255) | YES  |     | NULL    |                |
| Quantity       | int          | NO   |     | NULL    |                |
| Phone_n        | varchar(255) | NO   |     | NULL    |                |
| Product_amt    | double       | NO   |     | NULL    |                |
| Pay_amt        | double       | NO   |     | NULL    |                |
| Date           | date         | YES  |     | NULL    |                |
| Remaining_amt  | int          | YES  |     | NULL    |                |
+----------------+--------------+------+-----+---------+----------------+
10 rows in set (0.00 sec)

mysql> select * from customer;
+----+----------+----------+---------------------------+----------+------------+-------------+---------+------------+---------------+
| id | Name     | Address  | Purchase_Items            | Quantity | Phone_n    | Product_amt | Pay_amt | Date       | Remaining_amt |
+----+----------+----------+---------------------------+----------+------------+-------------+---------+------------+---------------+
|  1 | Sambha   | Jalgaon  |  2burger and 5 breads     |       15 | 0302464982 |         750 |    1500 | 2011-01-20 |          -750 |
|  2 | Gaurav   | Nasik    | 1 burger and 10 breads    |       15 | 0302464982 |         750 |    1200 | 2010-02-25 |          -450 |
|  3 | Tina     | kalyan   | 9 burger and 10 breads    |       12 | 0302464982 |         600 |    2000 | 2000-02-25 |         -1400 |
|  4 | Akash    | Nanded   | 1 burger and 10 breads    |        9 | 5602464982 |         450 |     100 | 2012-02-25 |           350 |
|  5 | Pratik   | Mumbai   | 25 burger and 18 breads   |       10 | 304446482  |         500 |    2000 | 2000-02-25 |         -1500 |
|  6 | Vicky    | Thakur   | 1 burger and 10 breads    |        7 | 1254458902 |         350 |     900 | 2011-08-23 |          -550 |
|  7 | ritik    | Thane    | 22 burger and 20 breads   |        2 | 1254458902 |         100 |     850 | 2014-10-17 |          -750 |
|  8 | roshan   | Satara   | 25 burger and 20 breads   |        1 | 1254458902 |          50 |     850 | 2014-10-17 |          -800 |
|  9 | Sagar    | Sangli   | 25 burger and 20 breads   |       13 | 2254458902 |         650 |     150 | 2014-10-17 |           500 |
| 10 | Kritika  | Kolhapur | 25 burger and 20 breads   |       18 | 1254458902 |         900 |     180 | 2019-10-17 |           720 |
| 11 | Mitali   | Thane    | 20 burger and 20 breads   |       23 | 2254458902 |        1150 |     199 | 2014-10-17 |           951 |
| 12 | kiara    | Latur    | 15 burger and 10 breads   |       16 | 1254458902 |         800 |     112 | 2017-10-17 |           688 |
| 13 | Vaibhav  | Sangmner | 13 burger and 10 breads   |       19 | 1254458902 |         950 |      58 | 2017-10-17 |           892 |
| 14 | Mital    | Thane    | 20 burger and 20 breads   |        3 | 2254458902 |         150 |      19 | 2014-10-17 |           131 |
| 15 | Vaishnav | Wagholi  | 113 burger and 110 breads |      149 | 1254458902 |        7450 |      18 | 2012-10-17 |          7432 |
+----+----------+----------+---------------------------+----------+------------+-------------+---------+------------+---------------+
15 rows in set (0.00 sec)





--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) NOT NULL,
  `Address` varchar(255) NOT NULL,
  `Designation` double NOT NULL,
  `Salary` double NOT NULL,
  `DOJ` date NOT NULL,
  `Absent` int NOT NULL,
  `Received_Salary` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1,'Saeed Khan','Novshera',2,24500,'1996-10-24',6,39200),(2,'uzar Khan','fatehkhana',3,10500,'2001-01-05',0,31500),(3,'Hammad khalid','Islamabad',5,15100,'2000-11-05',5,62916.666666666664),(4,'Ajay','Arora',7,20100,'1998-11-05',2,117250),(5,'Sandip','Jadhav',9,40100,'1996-11-25',5,300750),(6,'Rohit','Patil',19,40000,'2003-05-25',8,557333.3333333333),(7,'Geeta','lora',25,49000,'1992-06-21',10,816666.6666666667),(8,'Pawan','Oberio',22,42000,'1982-06-25',11,585200),(9,'Sanajan','Wankhede',12,52000,'2000-09-11',19,228800),(10,'Sheetal','Bonde',14,29000,'2000-03-18',2,378933.3333333334),(11,'kundan','Bonde',24,29200,'1996-03-18',8,513920),(12,'Aruna','Gujar',21,23200,'1997-03-18',6,389760),(13,'Sagar','Tadvi',8,20000,'2004-03-18',2,261333.33333333334),(14,'Mahima','Pinjari',18,20010,'2000-04-28',3,324162),(15,'Sahid','Kapoor',20,52200,'1982-03-18',6,835200);
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;


mysql> desc employee;
+-----------------+--------------+------+-----+---------+----------------+
| Field           | Type         | Null | Key | Default | Extra          |
+-----------------+--------------+------+-----+---------+----------------+
| id              | int          | NO   | PRI | NULL    | auto_increment |
| Name            | varchar(255) | NO   |     | NULL    |                |
| Address         | varchar(255) | NO   |     | NULL    |                |
| Designation     | double       | NO   |     | NULL    |                |
| Salary          | double       | NO   |     | NULL    |                |
| DOJ             | date         | NO   |     | NULL    |                |
| Absent          | int          | NO   |     | NULL    |                |
| Received_Salary | double       | NO   |     | NULL    |                |
+-----------------+--------------+------+-----+---------+----------------+
8 rows in set (0.00 sec)

mysql> select * from employee;
+----+---------------+------------+-------------+--------+------------+--------+--------------------+
| id | Name          | Address    | Designation | Salary | DOJ        | Absent | Received_Salary    |
+----+---------------+------------+-------------+--------+------------+--------+--------------------+
|  1 | Saeed Khan    | Novshera   |           2 |  24500 | 1996-10-24 |      6 |              39200 |
|  2 | uzar Khan     | fatehkhana |           3 |  10500 | 2001-01-05 |      0 |              31500 |
|  3 | Hammad khalid | Islamabad  |           5 |  15100 | 2000-11-05 |      5 | 62916.666666666664 |
|  4 | Ajay          | Arora      |           7 |  20100 | 1998-11-05 |      2 |             117250 |
|  5 | Sandip        | Jadhav     |           9 |  40100 | 1996-11-25 |      5 |             300750 |
|  6 | Rohit         | Patil      |          19 |  40000 | 2003-05-25 |      8 |  557333.3333333333 |
|  7 | Geeta         | lora       |          25 |  49000 | 1992-06-21 |     10 |  816666.6666666667 |
|  8 | Pawan         | Oberio     |          22 |  42000 | 1982-06-25 |     11 |             585200 |
|  9 | Sanajan       | Wankhede   |          12 |  52000 | 2000-09-11 |     19 |             228800 |
| 10 | Sheetal       | Bonde      |          14 |  29000 | 2000-03-18 |      2 |  378933.3333333334 |
| 11 | kundan        | Bonde      |          24 |  29200 | 1996-03-18 |      8 |             513920 |
| 12 | Aruna         | Gujar      |          21 |  23200 | 1997-03-18 |      6 |             389760 |
| 13 | Sagar         | Tadvi      |           8 |  20000 | 2004-03-18 |      2 | 261333.33333333334 |
| 14 | Mahima        | Pinjari    |          18 |  20010 | 2000-04-28 |      3 |             324162 |
| 15 | Sahid         | Kapoor     |          20 |  52200 | 1982-03-18 |      6 |             835200 |
+----+---------------+------------+-------------+--------+------------+--------+--------------------+
15 rows in set (0.00 sec)



--
-- Table structure for table `expenses`
--

DROP TABLE IF EXISTS `expenses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `expenses` (
  `Serial_no` int NOT NULL AUTO_INCREMENT,
  `Purchase_product` double DEFAULT NULL,
  `Renovation` double DEFAULT NULL,
  `Salaries` double DEFAULT NULL,
  `Sum_of_Expenses` double DEFAULT NULL,
  `Date` date DEFAULT NULL,
  PRIMARY KEY (`Serial_no`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `expenses`
--

LOCK TABLES `expenses` WRITE;
/*!40000 ALTER TABLE `expenses` DISABLE KEYS */;
INSERT INTO `expenses` VALUES (1,16611,800,5435225.333333334,5452636.333333334,'2008-11-15');
/*!40000 ALTER TABLE `expenses` ENABLE KEYS */;
UNLOCK TABLES;


mysql> desc expenses;
+------------------+--------+------+-----+---------+----------------+
| Field            | Type   | Null | Key | Default | Extra          |
+------------------+--------+------+-----+---------+----------------+
| Serial_no        | int    | NO   | PRI | NULL    | auto_increment |
| Purchase_product | double | YES  |     | NULL    |                |
| Renovation       | double | YES  |     | NULL    |                |
| Salaries         | double | YES  |     | NULL    |                |
| Sum_of_Expenses  | double | YES  |     | NULL    |                |
| Date             | date   | YES  |     | NULL    |                |
+------------------+--------+------+-----+---------+----------------+
6 rows in set (0.00 sec)

mysql> select * from expenses;
+-----------+------------------+------------+-------------------+-------------------+------------+
| Serial_no | Purchase_product | Renovation | Salaries          | Sum_of_Expenses   | Date       |
+-----------+------------------+------------+-------------------+-------------------+------------+
|         1 |            16611 |        800 | 5435225.333333334 | 5452636.333333334 | 2008-11-15 |
+-----------+------------------+------------+-------------------+-------------------+------------+
1 row in set (0.00 sec)



--
-- Table structure for table `menu`
--

DROP TABLE IF EXISTS `menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menu` (
  `Serial_no` int NOT NULL AUTO_INCREMENT,
  `SaleMan_list` varchar(255) DEFAULT NULL,
  `Employee_list` varchar(255) DEFAULT NULL,
  `Customer_list` varchar(255) DEFAULT NULL,
  `profit` double NOT NULL,
  `product` double NOT NULL,
  `Salaries` double NOT NULL,
  PRIMARY KEY (`Serial_no`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu`
--

LOCK TABLES `menu` WRITE;
/*!40000 ALTER TABLE `menu` DISABLE KEYS */;
INSERT INTO `menu` VALUES (1,'sale Man','Saeed Khan','Sambha',-5482755.333333334,119,31500),(2,'sale Man','uzar Khan','Gaurav',-5482755.333333334,66,31500),(3,'sale Man','Hammad khalid','Tina',-5482755.333333334,301,62916.666666666664),(4,'sale Man','Ajay','Akash',-5482755.333333334,387,117250),(5,'sale Man','Sandip','Pratik',-5482755.333333334,267,300750),(6,'sale Man','Rohit','Vicky',-5482755.333333334,897,557333.3333333333),(7,'sale Man','Geeta','ritik',-5482755.333333334,1028,816666.6666666667),(8,'sale Man','Pawan','roshan',-5482755.333333334,1272,585200),(9,'sale Man','Sanajan','Sagar',-5482755.333333334,1748,228800),(10,'sale Man','Sheetal','Kritika',-5482755.333333334,1913,378933.3333333334),(11,'sale Man','kundan','Mitali',-5482755.333333334,267,513920),(12,'sale Man','Aruna','kiara',-5482755.333333334,387,389760),(13,'sale Man','Sagar','Vaibhav',-5482755.333333334,521,261333.33333333334),(14,'sale Man','Mahima','Mital',-5482755.333333334,2544,324162),(15,'sale Man','Sahid','Vaishnav',-5482755.333333334,4894,835200);
/*!40000 ALTER TABLE `menu` ENABLE KEYS */;
UNLOCK TABLES;

mysql> desc Menu;
+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| Serial_no     | int          | NO   | PRI | NULL    | auto_increment |
| SaleMan_list  | varchar(255) | YES  |     | NULL    |                |
| Employee_list | varchar(255) | YES  |     | NULL    |                |
| Customer_list | varchar(255) | YES  |     | NULL    |                |
| profit        | double       | NO   |     | NULL    |                |
| product       | double       | NO   |     | NULL    |                |
| Salaries      | double       | NO   |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+
7 rows in set (0.00 sec)

mysql> select * from Menu;
+-----------+--------------+---------------+---------------+--------------------+---------+--------------------+
| Serial_no | SaleMan_list | Employee_list | Customer_list | profit             | product | Salaries           |
+-----------+--------------+---------------+---------------+--------------------+---------+--------------------+
|         1 | sale Man     | Saeed Khan    | Sambha        | -5482755.333333334 |     119 |              31500 |
|         2 | sale Man     | uzar Khan     | Gaurav        | -5482755.333333334 |      66 |              31500 |
|         3 | sale Man     | Hammad khalid | Tina          | -5482755.333333334 |     301 | 62916.666666666664 |
|         4 | sale Man     | Ajay          | Akash         | -5482755.333333334 |     387 |             117250 |
|         5 | sale Man     | Sandip        | Pratik        | -5482755.333333334 |     267 |             300750 |
|         6 | sale Man     | Rohit         | Vicky         | -5482755.333333334 |     897 |  557333.3333333333 |
|         7 | sale Man     | Geeta         | ritik         | -5482755.333333334 |    1028 |  816666.6666666667 |
|         8 | sale Man     | Pawan         | roshan        | -5482755.333333334 |    1272 |             585200 |
|         9 | sale Man     | Sanajan       | Sagar         | -5482755.333333334 |    1748 |             228800 |
|        10 | sale Man     | Sheetal       | Kritika       | -5482755.333333334 |    1913 |  378933.3333333334 |
|        11 | sale Man     | kundan        | Mitali        | -5482755.333333334 |     267 |             513920 |
|        12 | sale Man     | Aruna         | kiara         | -5482755.333333334 |     387 |             389760 |
|        13 | sale Man     | Sagar         | Vaibhav       | -5482755.333333334 |     521 | 261333.33333333334 |
|        14 | sale Man     | Mahima        | Mital         | -5482755.333333334 |    2544 |             324162 |
|        15 | sale Man     | Sahid         | Vaishnav      | -5482755.333333334 |    4894 |             835200 |
+-----------+--------------+---------------+---------------+--------------------+---------+--------------------+
15 rows in set (0.00 sec)



--
-- Table structure for table `profit`
--

DROP TABLE IF EXISTS `profit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `profit` (
  `Day` int NOT NULL AUTO_INCREMENT,
  `expenses` double DEFAULT NULL,
  `purchase` double DEFAULT NULL,
  `salary` double DEFAULT NULL,
  `Daily_profit` double DEFAULT NULL,
  PRIMARY KEY (`Day`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profit`
--

LOCK TABLES `profit` WRITE;
/*!40000 ALTER TABLE `profit` DISABLE KEYS */;
INSERT INTO `profit` VALUES (1,5452636.333333334,119,31500,-5482755.333333334),(2,5452636.333333334,66,31500,-5482502.333333334),(3,5452636.333333334,301,62916.666666666664,-5514904.000000001),(4,5452636.333333334,387,117250,-5568973.333333334),(5,5452636.333333334,267,300750,-5748803.333333334),(6,5452636.333333334,897,557333.3333333333,-6007666.666666667),(7,5452636.333333334,1028,816666.6666666667,-6225381.000000001),(8,5452636.333333334,1272,585200,-5991708.333333334),(9,5452636.333333334,1748,228800,-5659184.333333334),(10,5452636.333333334,1913,378933.3333333334,-5375732.666666667),(11,5452636.333333334,267,513920,-5431323.333333334),(12,5452636.333333334,387,389760,-5392633.333333334),(13,5452636.333333334,521,261333.33333333334,-5667840.666666667),(14,5452636.333333334,2544,324162,-5775742.333333334),(15,5452636.333333334,4894,835200,-6236830.333333334);
/*!40000 ALTER TABLE `profit` ENABLE KEYS */;
UNLOCK TABLES;


mysql> desc profit;
+--------------+--------+------+-----+---------+----------------+
| Field        | Type   | Null | Key | Default | Extra          |
+--------------+--------+------+-----+---------+----------------+
| Day          | int    | NO   | PRI | NULL    | auto_increment |
| expenses     | double | YES  |     | NULL    |                |
| purchase     | double | YES  |     | NULL    |                |
| salary       | double | YES  |     | NULL    |                |
| Daily_profit | double | YES  |     | NULL    |                |
+--------------+--------+------+-----+---------+----------------+
5 rows in set (0.00 sec)

mysql> select * from profit;
+-----+-------------------+----------+--------------------+--------------------+
| Day | expenses          | purchase | salary             | Daily_profit       |
+-----+-------------------+----------+--------------------+--------------------+
|   1 | 5452636.333333334 |      119 |              31500 | -5482755.333333334 |
|   2 | 5452636.333333334 |       66 |              31500 | -5482502.333333334 |
|   3 | 5452636.333333334 |      301 | 62916.666666666664 | -5514904.000000001 |
|   4 | 5452636.333333334 |      387 |             117250 | -5568973.333333334 |
|   5 | 5452636.333333334 |      267 |             300750 | -5748803.333333334 |
|   6 | 5452636.333333334 |      897 |  557333.3333333333 | -6007666.666666667 |
|   7 | 5452636.333333334 |     1028 |  816666.6666666667 | -6225381.000000001 |
|   8 | 5452636.333333334 |     1272 |             585200 | -5991708.333333334 |
|   9 | 5452636.333333334 |     1748 |             228800 | -5659184.333333334 |
|  10 | 5452636.333333334 |     1913 |  378933.3333333334 | -5375732.666666667 |
|  11 | 5452636.333333334 |      267 |             513920 | -5431323.333333334 |
|  12 | 5452636.333333334 |      387 |             389760 | -5392633.333333334 |
|  13 | 5452636.333333334 |      521 | 261333.33333333334 | -5667840.666666667 |
|  14 | 5452636.333333334 |     2544 |             324162 | -5775742.333333334 |
|  15 | 5452636.333333334 |     4894 |             835200 | -6236830.333333334 |
+-----+-------------------+----------+--------------------+--------------------+
15 rows in set (0.00 sec)




--
-- Table structure for table `purchase`
--

DROP TABLE IF EXISTS `purchase`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `purchase` (
  `Serial_no` int NOT NULL AUTO_INCREMENT,
  `Maida` double DEFAULT NULL,
  `Sugar` double NOT NULL,
  `Salt` double NOT NULL,
  `till` double NOT NULL,
  `LPG` double NOT NULL,
  `Oil` double NOT NULL,
  `Yeast` double NOT NULL,
  `EKa` double DEFAULT NULL,
  `Gluten` double DEFAULT NULL,
  `Packing` double DEFAULT NULL,
  `cartoon` double DEFAULT NULL,
  `packing_shopper` double DEFAULT NULL,
  `burger_shopper` double DEFAULT NULL,
  `baraf` double DEFAULT NULL,
  `sum` double DEFAULT NULL,
  PRIMARY KEY (`Serial_no`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchase`
--

LOCK TABLES `purchase` WRITE;
/*!40000 ALTER TABLE `purchase` DISABLE KEYS */;
INSERT INTO `purchase` VALUES (1,12,15,26,27,18,2,3,2,4,2,2,2,2,2,119),(2,2,5,26,7,8,2,2,2,2,2,2,2,2,2,66),(3,2,15,26,67,48,90,4,2,1,2,2,2,28,12,301),(4,2,15,26,67,48,90,4,102,7,2,2,2,8,12,387),(5,22,15,26,67,8,80,4,12,7,2,2,2,8,12,267),(6,22,15,26,617,78,80,4,12,7,12,2,2,8,12,897),(7,32,15,216,67,418,10,54,102,47,12,12,23,18,2,1028),(8,22,15,26,617,78,80,4,12,7,162,25,42,80,102,1272),(9,32,15,216,607,418,190,54,102,47,12,12,23,18,2,1748),(10,322,1245,16,57,18,90,4,12,43,2,82,2,1,19,1913),(11,22,15,26,67,8,80,4,12,7,2,2,2,8,12,267),(12,2,15,26,67,48,90,4,102,7,2,2,2,8,12,387),(13,44,115,26,67,8,80,90,12,10,9,8,22,18,12,521),(14,1022,915,26,67,80,80,64,12,87,12,24,66,77,12,2544),(15,102,1915,216,167,80,80,64,12,817,152,244,866,77,102,4894);
/*!40000 ALTER TABLE `purchase` ENABLE KEYS */;
UNLOCK TABLES;



mysql> desc purchase;
+-----------------+--------+------+-----+---------+----------------+
| Field           | Type   | Null | Key | Default | Extra          |
+-----------------+--------+------+-----+---------+----------------+
| Serial_no       | int    | NO   | PRI | NULL    | auto_increment |
| Maida           | double | YES  |     | NULL    |                |
| Sugar           | double | NO   |     | NULL    |                |
| Salt            | double | NO   |     | NULL    |                |
| till            | double | NO   |     | NULL    |                |
| LPG             | double | NO   |     | NULL    |                |
| Oil             | double | NO   |     | NULL    |                |
| Yeast           | double | NO   |     | NULL    |                |
| EKa             | double | YES  |     | NULL    |                |
| Gluten          | double | YES  |     | NULL    |                |
| Packing         | double | YES  |     | NULL    |                |
| cartoon         | double | YES  |     | NULL    |                |
| packing_shopper | double | YES  |     | NULL    |                |
| burger_shopper  | double | YES  |     | NULL    |                |
| baraf           | double | YES  |     | NULL    |                |
| sum             | double | YES  |     | NULL    |                |
+-----------------+--------+------+-----+---------+----------------+
16 rows in set (0.00 sec)

mysql> select * from purchase;
+-----------+-------+-------+------+------+-----+-----+-------+------+--------+---------+---------+-----------------+----------------+-------+------+
| Serial_no | Maida | Sugar | Salt | till | LPG | Oil | Yeast | EKa  | Gluten | Packing | cartoon | packing_shopper | burger_shopper | baraf | sum  |
+-----------+-------+-------+------+------+-----+-----+-------+------+--------+---------+---------+-----------------+----------------+-------+------+
|         1 |    12 |    15 |   26 |   27 |  18 |   2 |     3 |    2 |      4 |       2 |       2 |               2 |              2 |     2 |  119 |
|         2 |     2 |     5 |   26 |    7 |   8 |   2 |     2 |    2 |      2 |       2 |       2 |               2 |              2 |     2 |   66 |
|         3 |     2 |    15 |   26 |   67 |  48 |  90 |     4 |    2 |      1 |       2 |       2 |               2 |             28 |    12 |  301 |
|         4 |     2 |    15 |   26 |   67 |  48 |  90 |     4 |  102 |      7 |       2 |       2 |               2 |              8 |    12 |  387 |
|         5 |    22 |    15 |   26 |   67 |   8 |  80 |     4 |   12 |      7 |       2 |       2 |               2 |              8 |    12 |  267 |
|         6 |    22 |    15 |   26 |  617 |  78 |  80 |     4 |   12 |      7 |      12 |       2 |               2 |              8 |    12 |  897 |
|         7 |    32 |    15 |  216 |   67 | 418 |  10 |    54 |  102 |     47 |      12 |      12 |              23 |             18 |     2 | 1028 |
|         8 |    22 |    15 |   26 |  617 |  78 |  80 |     4 |   12 |      7 |     162 |      25 |              42 |             80 |   102 | 1272 |
|         9 |    32 |    15 |  216 |  607 | 418 | 190 |    54 |  102 |     47 |      12 |      12 |              23 |             18 |     2 | 1748 |
|        10 |   322 |  1245 |   16 |   57 |  18 |  90 |     4 |   12 |     43 |       2 |      82 |               2 |              1 |    19 | 1913 |
|        11 |    22 |    15 |   26 |   67 |   8 |  80 |     4 |   12 |      7 |       2 |       2 |               2 |              8 |    12 |  267 |
|        12 |     2 |    15 |   26 |   67 |  48 |  90 |     4 |  102 |      7 |       2 |       2 |               2 |              8 |    12 |  387 |
|        13 |    44 |   115 |   26 |   67 |   8 |  80 |    90 |   12 |     10 |       9 |       8 |              22 |             18 |    12 |  521 |
|        14 |  1022 |   915 |   26 |   67 |  80 |  80 |    64 |   12 |     87 |      12 |      24 |              66 |             77 |    12 | 2544 |
|        15 |   102 |  1915 |  216 |  167 |  80 |  80 |    64 |   12 |    817 |     152 |     244 |             866 |             77 |   102 | 4894 |
+-----------+-------+-------+------+------+-----+-----+-------+------+--------+---------+---------+-----------------+----------------+-------+------+
15 rows in set (0.00 sec)



--
-- Table structure for table `salaries`
--

DROP TABLE IF EXISTS `salaries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `salaries` (
  `Serial_no` int NOT NULL AUTO_INCREMENT,
  `Employee_id` int DEFAULT NULL,
  `Employee_name` varchar(255) DEFAULT NULL,
  `Employee_Salary` double DEFAULT NULL,
  PRIMARY KEY (`Serial_no`),
  KEY `Employee_id` (`Employee_id`),
  CONSTRAINT `salaries_ibfk_1` FOREIGN KEY (`Employee_id`) REFERENCES `employee` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salaries`
--

LOCK TABLES `salaries` WRITE;
/*!40000 ALTER TABLE `salaries` DISABLE KEYS */;
INSERT INTO `salaries` VALUES (1,1,'Saeed Khan',31500),(2,2,'uzar Khan',31500),(3,3,'Hammad khalid',62916.666666666664),(4,4,'Ajay',117250),(5,5,'Sandip',300750),(6,6,'Rohit',557333.3333333333),(7,7,'Geeta',816666.6666666667),(8,8,'Pawan',585200),(9,9,'Sanajan',228800),(10,10,'Sheetal',378933.3333333334),(11,11,'kundan',513920),(12,12,'Aruna',389760),(13,13,'Sagar',261333.33333333334),(14,14,'Mahima',324162),(15,15,'Sahid',835200);
/*!40000 ALTER TABLE `salaries` ENABLE KEYS */;
UNLOCK TABLES;

mysql> desc salaries;
+-----------------+--------------+------+-----+---------+----------------+
| Field           | Type         | Null | Key | Default | Extra          |
+-----------------+--------------+------+-----+---------+----------------+
| Serial_no       | int          | NO   | PRI | NULL    | auto_increment |
| Employee_id     | int          | YES  | MUL | NULL    |                |
| Employee_name   | varchar(255) | YES  |     | NULL    |                |
| Employee_Salary | double       | YES  |     | NULL    |                |
+-----------------+--------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)

mysql> select * from salaries;
+-----------+-------------+---------------+--------------------+
| Serial_no | Employee_id | Employee_name | Employee_Salary    |
+-----------+-------------+---------------+--------------------+
|         1 |           1 | Saeed Khan    |              31500 |
|         2 |           2 | uzar Khan     |              31500 |
|         3 |           3 | Hammad khalid | 62916.666666666664 |
|         4 |           4 | Ajay          |             117250 |
|         5 |           5 | Sandip        |             300750 |
|         6 |           6 | Rohit         |  557333.3333333333 |
|         7 |           7 | Geeta         |  816666.6666666667 |
|         8 |           8 | Pawan         |             585200 |
|         9 |           9 | Sanajan       |             228800 |
|        10 |          10 | Sheetal       |  378933.3333333334 |
|        11 |          11 | kundan        |             513920 |
|        12 |          12 | Aruna         |             389760 |
|        13 |          13 | Sagar         | 261333.33333333334 |
|        14 |          14 | Mahima        |             324162 |
|        15 |          15 | Sahid         |             835200 |
+-----------+-------------+---------------+--------------------+
15 rows in set (0.00 sec)




--
-- Table structure for table `sale_man`
--

DROP TABLE IF EXISTS `sale_man`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sale_man` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) NOT NULL,
  `Address` varchar(255) NOT NULL,
  `Purchase_Items` varchar(255) DEFAULT NULL,
  `Quantity` int NOT NULL,
  `Phone_n` varchar(255) NOT NULL,
  `sum` double NOT NULL,
  `Pay_amt` double NOT NULL,
  `Date` date DEFAULT NULL,
  `Remaining_amt` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sale_man`
--

LOCK TABLES `sale_man` WRITE;
/*!40000 ALTER TABLE `sale_man` DISABLE KEYS */;
INSERT INTO `sale_man` VALUES (1,'sale Man','Sale MAn 1 Address','5 burgers and 10 breads',15,'03025---',750,500,'2008-11-25',250),(2,'sale Man','Sale man 2 Address','55 burgers and 101 breads',19,'05625---',950,450,'2010-01-12',500),(3,'sale Man','Sale MAn 3 Address','515 burgers and 141 breads',7,'2265625---',350,1150,'2008-11-15',-800),(4,'sale Man','Sale man 4 Address','555 burgers and 111 breads',17,'05625---',850,333,'2010-08-29',517),(5,'sale Man','Sale man 5 Address','4915 burgers and 1631 breads',87,'16785625---',4350,66,'2012-02-15',4284),(6,'sale Man','Sale man 6 Address','735 burgers and 991 breads',57,'103625---',2850,323,'2009-08-29',2527),(7,'sale Man','Sale man 7 Address','589 burgers and 251 breads',897,'05625---',44850,31,'2010-09-21',44819),(8,'sale Man','Sale MAn 8 Address','849 burgers and 911 breads',947,'47925---',47350,9631,'2010-10-23',37719),(9,'sale Man','Sale MAn 9 Address','1049 burgers and 711 breads',467,'47925---',23350,79631,'2000-10-03',-56281),(10,'sale Man','Sale MAn 10 Address','4909 burgers and 9441 breads',9137,'47925---',456850,91331,'2005-01-03',365519),(11,'sale Man','Sale man 11  Address','4909 burgers and 9454breads',10687,'47925---',534350,791331,'2007-03-03',-256981),(12,'sale Man','Sale man 12  Address','4909 burgers and 4894 breads',8987,'47925---',449350,791331,'2009-10-31',-341981),(13,'sale Man','Sale MAn 13 Address','9009 burgers and 94894 breads',914,'47925---',45700,791331,'2014-12-31',-745631),(14,'sale Man','Sale MAn 14 Address','9229 burgers and 91114 breads',69,'40015---',3450,1113331,'2016-09-15',-1109881),(15,'sale Man','Sale MAn 15 Address','8910 burgers and 9114 breads',969,'41895---',48450,1243591,'2013-04-15',-1195141);
/*!40000 ALTER TABLE `sale_man` ENABLE KEYS */;
UNLOCK TABLES;




mysql> desc sale_man;
+----------------+--------------+------+-----+---------+----------------+
| Field          | Type         | Null | Key | Default | Extra          |
+----------------+--------------+------+-----+---------+----------------+
| id             | int          | NO   | PRI | NULL    | auto_increment |
| Name           | varchar(255) | NO   |     | NULL    |                |
| Address        | varchar(255) | NO   |     | NULL    |                |
| Purchase_Items | varchar(255) | YES  |     | NULL    |                |
| Quantity       | int          | NO   |     | NULL    |                |
| Phone_n        | varchar(255) | NO   |     | NULL    |                |
| sum            | double       | NO   |     | NULL    |                |
| Pay_amt        | double       | NO   |     | NULL    |                |
| Date           | date         | YES  |     | NULL    |                |
| Remaining_amt  | int          | YES  |     | NULL    |                |
+----------------+--------------+------+-----+---------+----------------+
10 rows in set (0.00 sec)

mysql> select *  from sale_man;
+----+----------+----------------------+-------------------------------+----------+-------------+--------+---------+------------+---------------+
| id | Name     | Address              | Purchase_Items                | Quantity | Phone_n     | sum    | Pay_amt | Date       | Remaining_amt |
+----+----------+----------------------+-------------------------------+----------+-------------+--------+---------+------------+---------------+
|  1 | sale Man | Sale MAn 1 Address   | 5 burgers and 10 breads       |       15 | 03025---    |    750 |     500 | 2008-11-25 |           250 |
|  2 | sale Man | Sale man 2 Address   | 55 burgers and 101 breads     |       19 | 05625---    |    950 |     450 | 2010-01-12 |           500 |
|  3 | sale Man | Sale MAn 3 Address   | 515 burgers and 141 breads    |        7 | 2265625---  |    350 |    1150 | 2008-11-15 |          -800 |
|  4 | sale Man | Sale man 4 Address   | 555 burgers and 111 breads    |       17 | 05625---    |    850 |     333 | 2010-08-29 |           517 |
|  5 | sale Man | Sale man 5 Address   | 4915 burgers and 1631 breads  |       87 | 16785625--- |   4350 |      66 | 2012-02-15 |          4284 |
|  6 | sale Man | Sale man 6 Address   | 735 burgers and 991 breads    |       57 | 103625---   |   2850 |     323 | 2009-08-29 |          2527 |
|  7 | sale Man | Sale man 7 Address   | 589 burgers and 251 breads    |      897 | 05625---    |  44850 |      31 | 2010-09-21 |         44819 |
|  8 | sale Man | Sale MAn 8 Address   | 849 burgers and 911 breads    |      947 | 47925---    |  47350 |    9631 | 2010-10-23 |         37719 |
|  9 | sale Man | Sale MAn 9 Address   | 1049 burgers and 711 breads   |      467 | 47925---    |  23350 |   79631 | 2000-10-03 |        -56281 |
| 10 | sale Man | Sale MAn 10 Address  | 4909 burgers and 9441 breads  |     9137 | 47925---    | 456850 |   91331 | 2005-01-03 |        365519 |
| 11 | sale Man | Sale man 11  Address | 4909 burgers and 9454breads   |    10687 | 47925---    | 534350 |  791331 | 2007-03-03 |       -256981 |
| 12 | sale Man | Sale man 12  Address | 4909 burgers and 4894 breads  |     8987 | 47925---    | 449350 |  791331 | 2009-10-31 |       -341981 |
| 13 | sale Man | Sale MAn 13 Address  | 9009 burgers and 94894 breads |      914 | 47925---    |  45700 |  791331 | 2014-12-31 |       -745631 |
| 14 | sale Man | Sale MAn 14 Address  | 9229 burgers and 91114 breads |       69 | 40015---    |   3450 | 1113331 | 2016-09-15 |      -1109881 |
| 15 | sale Man | Sale MAn 15 Address  | 8910 burgers and 9114 breads  |      969 | 41895---    |  48450 | 1243591 | 2013-04-15 |      -1195141 |
+----+----------+----------------------+-------------------------------+----------+-------------+--------+---------+------------+---------------+
15 rows in set (0.00 sec)
--
-- Table structure for table `sales`
--

DROP TABLE IF EXISTS `sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sales` (
  `Serial_no` int NOT NULL AUTO_INCREMENT,
  `sale_man_sales` double DEFAULT NULL,
  `customer_sales` double DEFAULT NULL,
  PRIMARY KEY (`Serial_no`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sales`
--

LOCK TABLES `sales` WRITE;
/*!40000 ALTER TABLE `sales` DISABLE KEYS */;
INSERT INTO `sales` VALUES (1,750,750),(2,950,750),(3,350,600),(4,850,450),(5,4350,500),(6,2850,350),(7,44850,100),(8,47350,50),(9,23350,650),(10,456850,900),(11,534350,1150),(12,449350,800),(13,45700,950),(14,3450,150),(15,48450,7450);
/*!40000 ALTER TABLE `sales` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;



mysql> desc sales;
+----------------+--------+------+-----+---------+----------------+
| Field          | Type   | Null | Key | Default | Extra          |
+----------------+--------+------+-----+---------+----------------+
| Serial_no      | int    | NO   | PRI | NULL    | auto_increment |
| sale_man_sales | double | YES  |     | NULL    |                |
| customer_sales | double | YES  |     | NULL    |                |
+----------------+--------+------+-----+---------+----------------+
3 rows in set (0.00 sec)

mysql> select * from sales;
+-----------+----------------+----------------+
| Serial_no | sale_man_sales | customer_sales |
+-----------+----------------+----------------+
|         1 |            750 |            750 |
|         2 |            950 |            750 |
|         3 |            350 |            600 |
|         4 |            850 |            450 |
|         5 |           4350 |            500 |
|         6 |           2850 |            350 |
|         7 |          44850 |            100 |
|         8 |          47350 |             50 |
|         9 |          23350 |            650 |
|        10 |         456850 |            900 |
|        11 |         534350 |           1150 |
|        12 |         449350 |            800 |
|        13 |          45700 |            950 |
|        14 |           3450 |            150 |
|        15 |          48450 |           7450 |
+-----------+----------------+----------------+
15 rows in set (0.00 sec)
-- Dump completed on 2021-12-24 15:17:20
