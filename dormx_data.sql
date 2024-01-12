-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: dormx
-- ------------------------------------------------------
-- Server version	8.0.35

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
-- Table structure for table `bets`
--

DROP TABLE IF EXISTS `bets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bets` (
  `bet_id` int NOT NULL AUTO_INCREMENT,
  `bet_user_id` int NOT NULL,
  `bet_product_id` int NOT NULL,
  `bet_amount` float NOT NULL,
  `bet_date` date NOT NULL,
  `bet_time` time NOT NULL,
  PRIMARY KEY (`bet_id`),
  UNIQUE KEY `bet_id_UNIQUE` (`bet_id`),
  KEY `bet_user_id_idx` (`bet_user_id`),
  KEY `bet_product_id_idx` (`bet_product_id`),
  CONSTRAINT `bet_product_id` FOREIGN KEY (`bet_product_id`) REFERENCES `products` (`product_id`) ON DELETE CASCADE,
  CONSTRAINT `bet_user_id` FOREIGN KEY (`bet_user_id`) REFERENCES `user_cred` (`user_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bets`
--

LOCK TABLES `bets` WRITE;
/*!40000 ALTER TABLE `bets` DISABLE KEYS */;
INSERT INTO `bets` VALUES (1,1,9,1899.99,'2024-01-05','21:10:17'),(2,1,9,1900,'2024-01-05','21:44:42'),(3,3,10,13,'2024-01-05','21:54:57'),(4,1,8,1500,'2024-01-08','17:52:54'),(5,1,8,1900,'2024-01-08','17:53:24'),(6,1,8,1950,'2024-01-08','17:55:22'),(7,4,7,13,'2024-01-09','19:48:25'),(8,4,10,12,'2024-01-09','19:48:57'),(9,1,13,15,'2024-01-10','23:26:33'),(10,3,11,1,'2024-01-10','23:28:08'),(11,1,21,30,'2024-01-11','01:50:10'),(13,1,7,16,'2024-01-11','04:00:20'),(14,6,21,20,'2024-01-11','04:21:20'),(15,6,20,10,'2024-01-11','04:22:13'),(16,6,14,75,'2024-01-11','04:23:04'),(17,3,22,30,'2024-01-11','04:32:34'),(18,1,22,25,'2024-01-11','04:32:56'),(22,1,17,8,'2024-01-11','19:28:44'),(23,4,22,25,'2024-01-12','02:37:36'),(24,4,19,15,'2024-01-12','02:37:52'),(25,4,16,1200,'2024-01-12','02:38:17'),(26,4,21,35,'2024-01-12','02:43:58'),(27,7,22,31,'2024-01-12','15:18:27'),(28,7,21,42,'2024-01-12','15:19:04'),(30,3,24,150,'2024-01-12','15:27:26');
/*!40000 ALTER TABLE `bets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_status`
--

DROP TABLE IF EXISTS `product_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_status` (
  `product_id` int NOT NULL,
  `condition` varchar(10) NOT NULL DEFAULT 'Pending',
  `entry_date` date NOT NULL,
  `entry_time` time NOT NULL,
  `last_update_date` date NOT NULL,
  `last_update_time` time NOT NULL,
  PRIMARY KEY (`product_id`),
  CONSTRAINT `product_id` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_status`
--

LOCK TABLES `product_status` WRITE;
/*!40000 ALTER TABLE `product_status` DISABLE KEYS */;
INSERT INTO `product_status` VALUES (1,'Pending','2024-01-04','17:49:16','2024-01-10','22:51:47'),(6,'Pending','2024-01-04','20:16:27','2024-01-04','20:16:27'),(7,'Pending','2024-01-04','20:21:29','2024-01-04','20:21:29'),(8,'Pending','2024-01-05','12:49:11','2024-01-05','12:49:11'),(9,'Completed','2024-01-05','17:47:09','2024-01-10','00:39:24'),(10,'Pending','2024-01-05','21:52:59','2024-01-11','01:46:22'),(11,'Pending','2024-01-10','11:54:35','2024-01-11','00:24:38'),(13,'Pending','2024-01-10','23:25:56','2024-01-10','23:27:09'),(14,'Completed','2024-01-10','23:30:57','2024-01-10','23:38:40'),(15,'Pending','2024-01-10','23:35:59','2024-01-10','23:35:59'),(16,'Pending','2024-01-10','23:40:45','2024-01-10','23:41:36'),(17,'Pending','2024-01-10','23:45:01','2024-01-10','23:45:25'),(18,'Pending','2024-01-10','23:51:45','2024-01-10','23:53:29'),(19,'Pending','2024-01-10','23:56:13','2024-01-10','23:56:13'),(20,'Pending','2024-01-10','23:57:28','2024-01-10','23:57:28'),(21,'Completed','2024-01-11','01:46:58','2024-01-12','15:20:58'),(22,'Pending','2024-01-11','04:30:22','2024-01-11','04:32:13'),(24,'Pending','2024-01-12','15:25:30','2024-01-12','15:25:30');
/*!40000 ALTER TABLE `product_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `product_id` int NOT NULL AUTO_INCREMENT,
  `product_user_id` int NOT NULL,
  `product_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `product_type` varchar(4) NOT NULL,
  `product_desc` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `product_pic` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'product_default.png',
  `price_range` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'None',
  PRIMARY KEY (`product_id`),
  UNIQUE KEY `product_id_UNIQUE` (`product_id`),
  KEY `product_user_id_idx` (`product_user_id`),
  CONSTRAINT `product_user_id` FOREIGN KEY (`product_user_id`) REFERENCES `user_cred` (`user_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,3,'Test Update','Buy','Testing description\r\nDesc Line two\r\nNew tesst Line','d0a0448e54ed6991fb64.png','800-1000'),(6,3,'Chinese Salad','Buy','I want to buy this, if anyone know any shop in this range contact me.','6e6ff46d7a6d9fb343b4.JPG','10-15 RMB'),(7,3,'Malatang Soup','Sell','I know a good shop with this price range','5976468ff71b49824b21.JPG','12-18 RMB'),(8,3,'This is a product with very very long name,can it fit the title?','Buy','This is the description','product_default.png','1000-2000 RMB'),(9,3,'Used Electric Bike','Sell','Rechargeable electric bike.\r\nMax Speed: 30 KM/H\r\nCharge time: 2-3 Hours\r\nDuration: 5-6 Hours','6dd3e0d8e5e0ee4a8a55.JPG','2000-2300 RMB'),(10,1,'Salad with Heated Chicken & Rice','Buy','?️ In canteen 3rd floor.\r\n✅ Vegetables\r\n✅ Rice\r\n✅ Chicken\r\n✅ Salad and Teriyaki Sauce','551937af55c327e50598.JPG','12-20 RMB'),(11,1,'Herbs Rice & Eggs','Sell','Rice cooked with many herbs ?, dry grapes ?, with boiled eggs ?','32ee21bf4c5a1db3c511.jpg','10-15'),(13,3,'Home made Pizza','Sell','Seafood Pizza with medium size. ?️?\r\nFree tomato sauce.\r\nFree sticker for kids.\r\n中等大小的海鲜披萨。\r\n免费番茄酱。\r\n儿童免费贴纸。\r\n.\r\nVery delicious ? 很好吃?','d5a7e0d16b8111359fbf.jpg','10-25 RMB'),(14,3,'New Robot Edition','Buy','Good robot for competition ?\r\n适合竞争?的好机器人','7f38198d889c6cdee3d6.jpg','50-2500'),(15,3,'Running Suits','Buy','Running suits including: \r\n1. Shirt size M\r\n2. Pants size L \r\n3. Running shoes size 42\'\r\n\r\n:: I used only one time for sport competition.\r\n.\r\n跑步服包括：\r\n1. 衬衫尺码 M\r\n2.裤子尺码 L\r\n3. 跑鞋尺码 42\'\r\n\r\n：： 我只用过一次体育比赛。','a8d38c65a0fa543b18cf.jpg','20-50'),(16,3,'Lenovo Laptop','Sell','For more information, you can contact me privately by leaving your phone-number.\r\n欲了解更多信息，您可以通过留下您的电话号码私下与我联系。','0d8ce62dc8e4cc35fe71.jpg','1250-2500'),(17,3,'Library Seat','Buy','I need to work on Library 8th floor (803) on 13th Jan.\r\nRequire seat in the middle, near the windows and far from toilet.\r\n\r\n我需要在 1 月 13 日在图书馆 8 楼 （803） 工作。\r\n需要坐在中间，靠近窗户，远离厕所。','19ec362af0b99b8dbe0b.jpg','5-10'),(18,3,'Sunflower Sprouts','Sell','Sunflower Sprouts 500g','a6ceef7c8b0753bf6554.JPG','20-35'),(19,1,'Seashell Souvenir','Buy','Looking for buying seashell made small souvenir int the price range.','471698810a4e3d60cb7e.JPG','10-20 RMB'),(20,3,'DIY Spicy Noodle with Veggie','Sell','DIY Spicy Noodle with Veggie includes:\r\n- Hot Spicy Cheese Dry Noodle\r\n- One Egg\r\n- 3 Seaweed for Korean style\r\n- 30g of Sunflower Sprouts\r\nVery satisfies to eat ?\r\n.\r\nDIY蔬菜辣面包括：\r\n- 热辣芝士干面\r\n- 一个鸡蛋\r\n- 3 韩式海藻\r\n- 30克向日葵芽\r\n吃?得很满意','product_default.png','20-30'),(21,3,'Lao Seafood Salad','Sell','Full of shrimp and rice noodle Lao salad style with organic veggies.','8ef8f000de4de58854f4.JPEG','25-45'),(22,6,'Best Laotian pizza','Sell','     Bill\'s pizza\r\nwe serve a better pizza than louis \'cafe and  restaurant.\r\nfresh, clean and yummy have to go to Bill\'s pizza.\r\nCutie small   25\r\nMega pizza 35\r\n\r\n','c6b8f7aed15fcd46587c.jpg','25-35 rmb'),(24,7,'水果','Sell','please ignore me','db73914b9d0fbeed1aae.jpg','100-120');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_cred`
--

DROP TABLE IF EXISTS `user_cred`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_cred` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` varchar(100) NOT NULL,
  `role` varchar(20) NOT NULL DEFAULT 'user',
  PRIMARY KEY (`user_id`,`username`),
  UNIQUE KEY `user_id_UNIQUE` (`user_id`),
  UNIQUE KEY `username_UNIQUE` (`username`),
  KEY `username_idx` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_cred`
--

LOCK TABLES `user_cred` WRITE;
/*!40000 ALTER TABLE `user_cred` DISABLE KEYS */;
INSERT INTO `user_cred` VALUES (1,'Emon','123456','user'),(3,'Puna','223344','user'),(4,'Xavier','123456','user'),(6,'BIllone1','12345678','user'),(7,'qq','123456','user');
/*!40000 ALTER TABLE `user_cred` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_logs`
--

DROP TABLE IF EXISTS `user_logs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_logs` (
  `log_user_id` int NOT NULL,
  `last_login_date` date DEFAULT NULL,
  `last_login_time` time DEFAULT NULL,
  `last_profile_update_date` date DEFAULT NULL,
  `last_profile_update_time` time DEFAULT NULL,
  `reg_date` date NOT NULL,
  `reg_time` time NOT NULL,
  PRIMARY KEY (`log_user_id`),
  UNIQUE KEY `log_user_id_UNIQUE` (`log_user_id`),
  CONSTRAINT `log_user_id` FOREIGN KEY (`log_user_id`) REFERENCES `user_cred` (`user_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_logs`
--

LOCK TABLES `user_logs` WRITE;
/*!40000 ALTER TABLE `user_logs` DISABLE KEYS */;
INSERT INTO `user_logs` VALUES (1,'2024-01-12','02:49:49','2024-01-12','02:50:35','2024-01-03','03:33:02'),(3,'2024-01-12','02:50:58','2024-01-09','22:43:31','2024-01-03','03:52:33'),(4,'2024-01-12','02:43:47','2024-01-11','04:08:48','2024-01-09','08:12:11'),(6,'2024-01-11','04:20:09',NULL,NULL,'2024-01-11','04:19:55'),(7,'2024-01-12','15:17:32','2024-01-12','15:26:58','2024-01-12','15:17:24');
/*!40000 ALTER TABLE `user_logs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int NOT NULL,
  `fullname` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `gender` varchar(10) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `address` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `profile_pic` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `user_id_UNIQUE` (`user_id`),
  CONSTRAINT `user_id` FOREIGN KEY (`user_id`) REFERENCES `user_cred` (`user_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Emon','Male','19398192331','GA19，山东科技大学','ec681e663141108c.jpg'),(3,'Pluna ?','Female','19353208980','GA21-209','bb80c03e3ccdd4e1.JPG'),(4,'Charlex Xavier','Male','19026807250','山东科技大学','f691e28230416e8d.JPG'),(6,'sithikone pathamavong','Male','+86 19027 72 73','','male_default.png'),(7,'qqli','Female','13156276237','J13-322','female_default.png');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-12 16:08:29
