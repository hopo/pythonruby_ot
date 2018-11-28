-- MySQL dump 10.16  Distrib 10.2.18-MariaDB, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: flask_db
-- ------------------------------------------------------
-- Server version	10.2.14-MariaDB-10.2.14+maria~jessie

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `post`
--

DROP TABLE IF EXISTS `post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `post` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `date_posted` datetime NOT NULL,
  `content` text NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `post_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post`
--

LOCK TABLES `post` WRITE;
/*!40000 ALTER TABLE `post` DISABLE KEYS */;
INSERT INTO `post` VALUES (5,'Hello World','2018-08-10 00:16:03','\"Hello World\"',2),(6,'PROJECT - springApril','2018-08-10 00:22:50','start_date : 2018/08/07\r\nJAVA8, ApacheTomcat8.5, Spring4\r\n',2),(7,'springApril 0807','2018-08-10 00:24:43','database work :  create table / \'tab_member\' / \'tab_customer\'',2),(8,'springApril 0808','2018-08-10 00:26:07','*form.jsp, *proc.jsp / pom.xml, web.xml settings',2),(9,'springApril 0809','2018-08-10 00:28:10','problem : connecting between eclipse and tomcat',2),(10,'springApril 0810 : connect mysqsl','2018-08-10 00:51:14','http://all-record.tistory.com/175',2),(11,'SQLAlchemy : order by desc','2018-08-10 01:01:12','```\r\nfrom sqlalchemy import desc\r\nsomeselect.order_by(desc(table1.mycol))\r\n```\r\nhttps://stackoverflow.com/questions/4186062/sqlalchemy-order-by-descending',2),(12,'springApril 0810 : xml settings','2018-08-10 02:33:32','root-context.xml : annotation-config, transaction, beans',2),(13,'springApril 0810','2018-08-10 04:47:11','insertMember :\r\nservice, mapper',2),(14,'studyMVC 0810','2018-08-10 08:49:33','JSON attach',2),(15,'springApril 0811','2018-08-11 04:39:28',' memberInsert / memberUpdate / memberDelete',2),(16,'springApril 0811','2018-08-11 07:25:27','session : login, logout',2),(18,'Fla 0811','2018-08-11 14:27:47','update, delete /\r\nmodal',2),(19,'springApril 0813','2018-08-13 05:53:43','start making customer service',2),(20,'springApril 0814','2018-08-14 02:50:18','...ing\r\ncustomer select',2),(21,'springApril 0820','2018-08-20 03:06:03','pagination with jQuery',2),(22,'springApril 0821','2018-08-21 04:55:16','bootstraping',2),(23,'springApril 0822','2018-08-22 04:23:03','0822\r\nbootstrapping\r\nchart start?\r\n우짜꼬?',2),(24,'순서A','2018-08-22 05:24:23','data type\r\ncondition\r\nloop\r\nfunction\r\npackage\r\nmodule',2),(25,'순서W','2018-08-22 05:25:18','pattern\r\ndatabase connection\r\nrequest\r\nsession\r\nCRUD\r\nboard\r\npagination\r\najax\r\ndistribute',2),(26,'springApril 0823','2018-08-23 04:11:53','customer chart\r\nmdn? bootstrap chart',2),(27,'springApril 0823-2','2018-08-23 23:59:53','chart using ajax',2),(28,'springApril 0824','2018-08-24 03:01:59','정리정돈',2),(29,'0827','2018-08-27 04:03:04','Start TEAM Project',2),(30,'aprilOne 0827 Day01','2018-08-27 13:02:05','박 : 깃\r\n김 : 메뉴아이템\r\n차 : 워크플로우',2),(31,'aprilOne 0828 Day02A','2018-08-28 03:58:28','박김차 : 데이터베이스 스키마',2),(32,'aprilOne 0828 Day02B','2018-08-29 03:21:28','박 : 데이터베이스 스키마 \r\n차 : 데이터베이스 스키마, WBS\r\n김 : 데이터베이스 스키마 \r\n박차김 : 프로젝트 시작 세팅',2),(33,'aprilOne 0829 Day03','2018-08-29 08:39:04','박김차: 초기세팅, 물리이름',2),(34,'aprilOne 0830 Day04','2018-08-30 12:25:17','박 : 화면설계\r\n김 : ERD\r\n차 : WBS',2),(35,'aprilOne 0831 Day05','2018-08-31 02:54:20','박 : 화면설계\r\n김차 : 킥오프 준비',2),(36,'aprilOne 0903 Day06','2018-09-03 04:00:09','박 : \'세션\' 틀\r\n김 : 데이터베이스 스키마\r\n차 : \'게시판\'',2),(37,'aprilOne 0904 Day07','2018-09-04 07:33:50','박 : Architecture\r\n김 : dev employee\r\n차 : dev noitce',2),(38,'aprilOne 0905 Day08','2018-09-06 04:32:15','박 : 데이터베이스\r\n김 : 세션\r\n차 : 게시',2),(39,'aprilOne 0906 Day09','2018-09-07 08:38:21','박 : 데이터베이\r\n김 : 환자목록\r\n차 : 게시판 상세보기',2),(40,'aprilOne 0907 Day10','2018-09-07 08:39:29','박 : 데이터베이스 세션 직원\r\n김 : 환자 등록 수정\r\n차 : 게시판 등록 수정',2),(43,'aprilOne 0910 Day11','2018-09-10 08:33:11','박 : \'진료\' 셀렉트\r\n김 : \'환자\' 페이지네이션',2),(44,'aprilOne 0911 Day12','2018-09-11 04:11:24','박 : \'진료\'\r\n김 : \'처방\'\r\n차 : \'게시판\'',2),(45,'aprilOne 0912 Day13','2018-09-12 10:03:51','박 : 공통 정리정돈\r\n김 : \'처방\' 리스트 등록\r\n차 : \'게시판\' 서치 페이지네이션',2),(46,'aprilOne 0913 Day14','2018-09-13 08:29:40','박 : 서치/페이지/AJAX',2),(47,'aprilOne 0914 Day15','2018-09-17 08:35:52','박 : 필터 적용을 해보자\r\n차 :',2),(48,'aprilOne 0917 Day16','2018-09-17 08:36:40','박 : \'세션\' \'직원\' 디테일즈~\r\n김 : \'의약품\' 모달',2),(49,'aprilOne 0918 Day17','2018-09-19 08:39:14','-',2),(50,'aprilOne 0919 Day18','2018-09-19 08:39:53','박 : 진료리스트-조인, 상세보기, 페이지간 연결',2);
/*!40000 ALTER TABLE `post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `email` varchar(120) NOT NULL,
  `image_file` varchar(20) NOT NULL,
  `password` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'admin','admin@email.com','default.jpg','$2b$12$xCPeywKTwTZEL8L.p7/x9OgT6I6LDQhpNl95Cp5s0E2v53/Mn5oTi'),(2,'RiceboySleeps','riceboysleeps@naver.com','riceboypic.jpg','$2b$12$iGrUtlk3UQMN/NpXtaIId.46ENw9iXnPopo3BirYddusHFS9mDvuy'),(8,'amber','amber@email.com','default.jpg','$2b$12$70tUmoNK0pDYmEeShqhAU.7z2KHA/6dJeWKB1c0Z3Ng9t9/QMc1ym'),(9,'testUser','testuser@test.com','default.jpg','$2b$12$FbGQqGh1v7C7udUAbR83nO1aBJbOCPHeeQ/PQvIxD8dwArBcZw2Hm');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-28 15:36:54
