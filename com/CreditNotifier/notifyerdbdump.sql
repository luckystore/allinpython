-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.11 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             9.5.0.5196
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for mysql
CREATE DATABASE IF NOT EXISTS `mysql` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */;
USE `mysql`;

-- Dumping structure for table mysql.credit_feeds
CREATE TABLE IF NOT EXISTS `credit_feeds` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `FI` varchar(50) DEFAULT NULL,
  `ACCOUNT_TYPE` varchar(50) DEFAULT NULL,
  `CUSTOMER_ID` int(11) DEFAULT NULL,
  `ACCOUNT_NO` varchar(50) DEFAULT NULL,
  `ACCOUNT_HOLDER` varchar(50) DEFAULT NULL,
  `AMOUNT_DUE_IN_DOLLERS` varchar(50) DEFAULT NULL,
  `DUE_DATE` varchar(50) DEFAULT NULL,
  `DUE_REMAINDER_DATE` varchar(50) DEFAULT NULL,
  `DUE_CLEARANCE_MODE` varchar(50) DEFAULT NULL,
  `NOTIFICATION_STATUS` varchar(50) DEFAULT 'UNSENT',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=163 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table mysql.credit_feeds: ~2 rows (approximately)
/*!40000 ALTER TABLE `credit_feeds` DISABLE KEYS */;
INSERT IGNORE INTO `credit_feeds` (`ID`, `FI`, `ACCOUNT_TYPE`, `CUSTOMER_ID`, `ACCOUNT_NO`, `ACCOUNT_HOLDER`, `AMOUNT_DUE_IN_DOLLERS`, `DUE_DATE`, `DUE_REMAINDER_DATE`, `DUE_CLEARANCE_MODE`, `NOTIFICATION_STATUS`) VALUES
	(161, 'WellsForgo', 'Savings', 1, '3323232324', 'John', '$750', '1532490000000', '1532320000000', 'ECS', 'UNSENT'),
	(162, 'WellsForgo', 'Savings', 2, '3589787654', 'David Miller', '$850', '1532490000000', '1532320000000', 'ECS', 'UNSENT');
/*!40000 ALTER TABLE `credit_feeds` ENABLE KEYS */;

-- Dumping structure for table mysql.customer_details
CREATE TABLE IF NOT EXISTS `customer_details` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `CUSTOMER_NAME` varchar(50) NOT NULL DEFAULT '0',
  `CUSTOMER_EMAIL` varchar(50) NOT NULL DEFAULT '0',
  `CUSTOMER_MOBILE` varchar(50) NOT NULL DEFAULT '0',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table mysql.customer_details: ~2 rows (approximately)
/*!40000 ALTER TABLE `customer_details` DISABLE KEYS */;
INSERT IGNORE INTO `customer_details` (`ID`, `CUSTOMER_NAME`, `CUSTOMER_EMAIL`, `CUSTOMER_MOBILE`) VALUES
	(1, 'Kiran', 'kiranmekanuri@gmail.com', '11111111111'),
	(2, 'Suneel', 'reddysuneelkumar@gmail.com', '2222222222');
/*!40000 ALTER TABLE `customer_details` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
