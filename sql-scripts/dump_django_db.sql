-- MySQL dump 10.16  Distrib 10.2.18-MariaDB, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: django_db
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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add post',7,'add_post'),(26,'Can change post',7,'change_post'),(27,'Can delete post',7,'delete_post'),(28,'Can view post',7,'view_post'),(29,'Can add profile',8,'add_profile'),(30,'Can change profile',8,'change_profile'),(31,'Can delete profile',8,'delete_profile'),(32,'Can view profile',8,'view_profile');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$100000$NVQ9qwrNKqsI$BKmjdTuzqO/GUnFFPSe88PhcfIIM5AKir5T6P0HGhug=','2018-11-07 12:17:02.056126',1,'admin','','','',1,1,'2018-09-16 11:43:24.269769'),(2,'pbkdf2_sha256$100000$gviahuMVIDrt$8AQuQmtH3gQE/Zj4+P2HedZYnXjDU4gOuu2mqMmYrtM=','2018-11-07 11:51:06.340280',0,'riceboy','루바','하','riceboysleeps@naver.com',1,1,'2018-09-16 11:46:57.000000'),(3,'pbkdf2_sha256$120000$nFRXFVr80sKz$MQLKJtwjYHOAjfrZv+ti5ZP/viJvjGXcJsRgysnzKzQ=','2018-09-19 12:56:50.600515',0,'testUser','Test','User','TU@test.com',0,1,'2018-09-16 12:54:33.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_post`
--

DROP TABLE IF EXISTS `blog_post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_post` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `content` longtext NOT NULL,
  `date_posted` datetime(6) NOT NULL,
  `author_id` int(11) NOT NULL,
  `memo` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `blog_post_author_id_dd7a8485_fk_auth_user_id` (`author_id`),
  CONSTRAINT `blog_post_author_id_dd7a8485_fk_auth_user_id` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=104 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_post`
--

LOCK TABLES `blog_post` WRITE;
/*!40000 ALTER TABLE `blog_post` DISABLE KEYS */;
INSERT INTO `blog_post` VALUES (31,'Hello World','\"Hello World\"','2018-08-10 00:16:03.000000',2,'blank..'),(32,'PROJECT - springApril','start_date : 2018/08/07\r\nJAVA8, ApacheTomcat8.5, Spring4\r\n','2018-08-10 00:22:50.000000',2,'blank..'),(33,'springApril 0807','database work :  create table / \'tab_member\' / \'tab_customer\'','2018-08-10 00:24:43.000000',2,'blank..'),(34,'springApril 0808','*form.jsp, *proc.jsp / pom.xml, web.xml settings','2018-08-10 00:26:07.000000',2,'blank..'),(35,'springApril 0809','problem : connecting between eclipse and tomcat','2018-08-10 00:28:10.000000',2,'blank..'),(36,'springApril 0810 : connect mysqsl','http://all-record.tistory.com/175','2018-08-10 00:51:14.000000',2,'blank..'),(37,'SQLAlchemy : order by desc','```\r\nfrom sqlalchemy import desc\r\nsomeselect.order_by(desc(table1.mycol))\r\n```\r\nhttps://stackoverflow.com/questions/4186062/sqlalchemy-order-by-descending','2018-08-10 01:01:12.000000',2,'blank..'),(38,'springApril 0810 : xml settings','root-context.xml : annotation-config, transaction, beans','2018-08-10 02:33:32.000000',2,'blank..'),(39,'springApril 0810','insertMember :\r\nservice, mapper','2018-08-10 04:47:11.000000',2,'blank..'),(40,'studyMVC 0810','JSON attach','2018-08-10 08:49:33.000000',2,'blank..'),(41,'springApril 0811',' memberInsert / memberUpdate / memberDelete','2018-08-11 04:39:28.000000',2,'blank..'),(42,'springApril 0811','session : login, logout','2018-08-11 07:25:27.000000',2,'blank..'),(43,'Fla 0811','update, delete /\r\nmodal','2018-08-11 14:27:47.000000',2,'blank..'),(44,'springApril 0813','start making customer service','2018-08-13 05:53:43.000000',2,'blank..'),(45,'springApril 0814','...ing\r\ncustomer select','2018-08-14 02:50:18.000000',2,'blank..'),(46,'springApril 0820','pagination with jQuery','2018-08-20 03:06:03.000000',2,'blank..'),(47,'springApril 0821','bootstraping','2018-08-21 04:55:16.000000',2,'blank..'),(48,'springApril 0822','0822\r\nbootstrapping\r\nchart start?\r\n우짜꼬?','2018-08-22 04:23:03.000000',2,'blank..'),(49,'순서A','data type\r\ncondition\r\nloop\r\nfunction\r\npackage\r\nmodule','2018-08-22 05:24:23.000000',2,'blank..'),(50,'순서W','pattern\r\ndatabase connection\r\nrequest\r\nsession\r\nCRUD\r\nboard\r\npagination\r\najax\r\ndistribute','2018-08-22 05:25:18.000000',2,'blank..'),(51,'springApril 0823','customer chart\r\nmdn? bootstrap chart','2018-08-23 04:11:53.000000',2,'blank..'),(52,'springApril 0823-2','chart using ajax','2018-08-23 23:59:53.000000',2,'blank..'),(53,'springApril 0824','정리정돈','2018-08-24 03:01:59.000000',2,'blank..'),(54,'0827','Start TEAM Project','2018-08-27 04:03:04.000000',2,'blank..'),(55,'aprilOne 0827 Day01','박 : 깃\r\n김 : 메뉴아이템\r\n차 : 워크플로우','2018-08-27 13:02:05.000000',2,'blank..'),(56,'aprilOne 0828 Day02A','박김차 : 데이터베이스 스키마','2018-08-28 03:58:28.000000',2,'blank..'),(57,'aprilOne 0828 Day02B','박 : 데이터베이스 스키마 \r\n차 : 데이터베이스 스키마, WBS\r\n김 : 데이터베이스 스키마 \r\n박차김 : 프로젝트 시작 세팅','2018-08-29 03:21:28.000000',2,'blank..'),(58,'aprilOne 0829 Day03','박김차: 초기세팅, 물리이름','2018-08-29 08:39:04.000000',2,'blank..'),(59,'aprilOne 0830 Day04','박 : 화면설계\r\n김 : ERD\r\n차 : WBS','2018-08-30 12:25:17.000000',2,'blank..'),(60,'aprilOne 0831 Day05','박 : 화면설계\r\n김차 : 킥오프 준비','2018-08-31 02:54:20.000000',2,'blank..'),(61,'aprilOne 0903 Day06','박 : \'세션\' 틀\r\n김 : 데이터베이스 스키마\r\n차 : \'게시판\'','2018-09-03 04:00:09.000000',2,'blank..'),(62,'aprilOne 0904 Day07','박 : Architecture\r\n김 : dev employee\r\n차 : dev noitce','2018-09-04 07:33:50.000000',2,'blank..'),(63,'aprilOne 0905 Day08','박 : 데이터베이스\r\n김 : 세션\r\n차 : 게시','2018-09-06 04:32:15.000000',2,'blank..'),(64,'aprilOne 0906 Day09','박 : 데이터베이\r\n김 : 환자목록\r\n차 : 게시판 상세보기','2018-09-07 08:38:21.000000',2,'blank..'),(65,'aprilOne 0907 Day10','박 : 데이터베이스 세션 직원\r\n김 : 환자 등록 수정\r\n차 : 게시판 등록 수정','2018-09-07 08:39:29.000000',2,'blank..'),(66,'aprilOne 0910 Day11','박 : \'진료\' 셀렉트\r\n김 : \'환자\' 페이지네이션','2018-09-10 08:33:11.000000',2,'blank..'),(67,'aprilOne 0911 Day12','박 : \'진료\'\r\n김 : \'처방\'\r\n차 : \'게시판\'','2018-09-11 04:11:24.000000',2,'blank..'),(68,'aprilOne 0912 Day13','박 : 공통 정리정돈\r\n김 : \'처방\' 리스트 등록\r\n차 : \'게시판\' 서치 페이지네이션','2018-09-12 10:03:51.000000',2,'blank..'),(69,'aprilOne 0913 Day14','박 : 서치/페이지/AJAX','2018-09-13 08:29:40.000000',2,'blank..'),(70,'aprilOne 0914 Day15','박 : 필터 적용을 해보자\r\n차 :','2018-09-17 08:35:52.000000',2,'blank..'),(71,'aprilOne 0917 Day16','박 : \'세션\' \'직원\' 디테일즈~\r\n김 : \'의약품\' 모달','2018-09-17 08:36:40.000000',2,'blank..'),(72,'aprilOne 0918 Day17','-','2018-09-19 08:39:14.000000',2,'blank..'),(73,'aprilOne 0919 Day18','박 : 진료리스트-조인, 상세보기, 페이지간 연결','2018-09-19 08:39:53.000000',2,'blank..'),(94,'aprilOne 0920 Day19','박 : 페이지간 연결고리\r\n김 : ‘처방’ 조인','2018-09-20 05:36:11.559713',2,'blank..'),(95,'aprilOne 0921 Day20','박 : \'직원\', \'게시판\'  정리정돈','2018-09-21 08:37:31.815824',2,'blank..'),(96,'aprilOne 0927 Day21','박 : 리팩토링','2018-09-27 13:27:15.500191',2,'blank..'),(97,'aprilOne 0928 Day22','박 : 인터럽터, 화면스타일 - 로그인, 직원등록','2018-09-29 01:55:41.078670',2,'blank..'),(98,'aprilOne 1001 Day23','박 : 메뉴 정리 정돈\r\n차 : 발표자료 만들기','2018-10-02 06:08:08.217955',2,'blank..'),(99,'Dev Django Korea 2018','[ 행사 개요 ]\r\n주최 : Dev Django Korea 2018\r\n일정 : 2018년 10월 07일 (일) 오전 09:30 - 오후 06:00\r\n장소 : 대한민국 서울특별시 마포구 공덕동 백범로31길 21 서울창업허브 10층 대강당\r\n\r\n\r\n**Snaker(Url Shortener) 원리 알아보기 _신호석\r\n-goo.gl (~2019)\r\n-트위터에서 활요을 많이 했지\r\n-github.com/erishfogG/snaker\r\n-request\r\n-분리 : Redirect / Operationg\r\n-pipenv : 패키지 관히와 가상환경을 같이 관리\r\n-pinject : DI를 통한 의종성 제거\r\n-pytest-django : TDD(?)\r\n-DB에서 WR에 병목이 생기는가 (일단, 인프라 증가시켜야)\r\n\r\n\r\n**Koreans-love-django : 한구의 django개발자와 회사들 _조재호\r\n-장고 토큐먼츠\r\n-안정성을 높이기 위해 test\r\n-추천도서 \'Two Scoops of Django\'\r\n-Form/CBV 이전에 먼저 FBV를 제대로 익히세요\r\n-trasifex : 웹기반 번역 플랫폼\r\n-장고팬사이트를 만들고 있습니다.\r\n\r\n\r\n**보안 스타트업에서 분석가가 Django로 웹서비스 만든 이야기 _김남준\r\n-특정ip가 일정 횟수 이상 요청하면 차단\r\n-문서/테스트 코드\r\n-inspectdb(?) (managed=FALSE #RO)\r\n-상태컬러는 커스텀 코드로 활용\r\n-분석, 분석, 분석\r\n-celery(+redis) : 비동기\r\n-caching의 활용\r\n-테스트 : 모델/클라이언트 테스트, 보안성테스트(sqlmap활용!)\r\n\r\n\r\n**Djnago를 배우다, Django로 배우다 _정경업\r\n-Formset(?)\r\n-데이터 마이그레이션\r\n-Aggragation\r\n-iamport : 결제\r\n-test, coverage\r\n-비개발자 <--parser--> 개발자\r\n-REST (between Back and Front)\r\n-proxyModel(?)\r\n-docker-compse\r\n-더 나은 test를 위해 \'Factory Boy\'\r\n-협업 or 분업\r\n-Pay it forward (베품)\r\n-문서만들기 / 리뷰하기 / 피드백\r\n-microservice : 격리성이필요할 때\r\n\r\n\r\n**Django의 배신(주니어 개발자의 Django 삽질기)\r\n-Count(Case(When()))\r\n-post = Posts.Objects.all()\r\n   for e in post:        # ->필요할때\r\n-debug-toolbar의 활용\r\n-select_related() / prepatch_related()\r\n-celery체크 : \'flower\' task\r\n-tx atomic commit시 \'celery\'사용 주의 -> on_commit의 활용\r\n-csrf는 쿠키에 저장\r\n-공부 : 네트워크 / https\r\n\r\n\r\n**DB와 ORM에 관한 7가지 고민\r\n-선 DB스키마 후django-ORM 순서로 간다(No using migration)\r\n-Null vs Invali value\r\n-JOIN in Django ORM :\r\n     INNER --promote_join--> LOUTER\r\n     INNER <--demote_join-- LOUTER\r\n-DB_ROUTER의 활용\r\n-DB분리 되어있을 때 : select_related대시 prefetch_related()를 사용','2018-10-07 00:45:15.281134',2,'blank..'),(100,'관리자가 알리는 글','이 글은\r\n관리자가\r\n테스트를\r\n하기 위한\r\n글입니다.','2018-10-22 17:23:46.000000',1,'blank..'),(101,'금일 오전 알림 사항(테스트)','곤리자 이외는 야-근 입니다.','2018-10-22 18:02:55.000000',1,'blank..'),(102,'10월23일 관리자의 테스트글','안녕하세요 관라자 입니다.\r\n아무 문제가 없는가요?','2018-10-23 13:59:35.297970',1,'blank..'),(103,'메모 필드를 추가하였습니다.','그래서 테스트를 합니다. 굳굳!','2018-11-07 12:18:15.000000',1,'이것이 포스트 메모 칸이올씨다.');
/*!40000 ALTER TABLE `blog_post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2018-09-16 11:46:57.450912','2','riceboy',1,'[{\"added\": {}}]',4,1),(2,'2018-09-16 11:48:54.270314','2','riceboy',2,'[{\"changed\": {\"fields\": [\"first_name\", \"last_name\", \"email\", \"is_staff\"]}}]',4,1),(3,'2018-09-16 12:52:25.735849','1','Blog 1 Updated',2,'[{\"changed\": {\"fields\": [\"title\", \"content\"]}}]',7,1),(4,'2018-09-16 12:54:34.050619','3','testUser',1,'[{\"added\": {}}]',4,1),(5,'2018-09-16 12:55:06.859488','3','testUser',2,'[{\"changed\": {\"fields\": [\"first_name\", \"last_name\"]}}]',4,1),(6,'2018-09-17 12:30:22.126320','1','riceboy Profile',1,'[{\"added\": {}}]',8,1),(7,'2018-09-17 12:31:12.432915','2','testUser Profile',1,'[{\"added\": {}}]',8,1),(8,'2018-09-17 12:43:21.824623','2','testUser Profile',3,'',8,1),(9,'2018-09-17 12:43:21.871212','1','riceboy Profile',3,'',8,1),(10,'2018-09-17 12:44:35.690808','3','riceboy Profile',1,'[{\"added\": {}}]',8,1),(11,'2018-09-17 12:44:45.783775','4','testUser Profile',1,'[{\"added\": {}}]',8,1),(12,'2018-10-22 15:48:16.695822','4','newUser',3,'',4,2),(13,'2018-10-22 15:48:16.729917','5','newUser2',3,'',4,2),(14,'2018-10-22 15:48:16.762961','6','newUser3',3,'',4,2),(15,'2018-10-22 15:48:16.830389','7','testtestid',3,'',4,2),(16,'2018-10-22 17:24:40.111501','100','관리자가 알리는 글',1,'[{\"added\": {}}]',7,1),(17,'2018-10-22 17:45:47.348352','100','관리자가 알리는 글',2,'[{\"changed\": {\"fields\": [\"content\"]}}]',7,1),(18,'2018-10-22 18:07:02.212504','101','금일 오전 알림 사항(테스트)',1,'[{\"added\": {}}]',7,1),(19,'2018-11-07 12:19:24.804495','103','메모 필드를 추가하였습니다.',1,'[{\"added\": {}}]',7,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(7,'blog','post'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(8,'users','profile');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-09-12 14:56:50.663390'),(2,'auth','0001_initial','2018-09-12 14:56:56.749012'),(3,'admin','0001_initial','2018-09-12 14:56:58.156320'),(4,'admin','0002_logentry_remove_auto_add','2018-09-12 14:56:58.213116'),(5,'admin','0003_logentry_add_action_flag_choices','2018-09-12 14:56:58.301899'),(6,'contenttypes','0002_remove_content_type_name','2018-09-12 14:56:59.011265'),(7,'auth','0002_alter_permission_name_max_length','2018-09-12 14:56:59.639304'),(8,'auth','0003_alter_user_email_max_length','2018-09-12 14:57:00.282494'),(9,'auth','0004_alter_user_username_opts','2018-09-12 14:57:00.339958'),(10,'auth','0005_alter_user_last_login_null','2018-09-12 14:57:00.704001'),(11,'auth','0006_require_contenttypes_0002','2018-09-12 14:57:00.760831'),(12,'auth','0007_alter_validators_add_error_messages','2018-09-12 14:57:00.818039'),(13,'auth','0008_alter_user_username_max_length','2018-09-12 14:57:01.446143'),(14,'auth','0009_alter_user_last_name_max_length','2018-09-12 14:57:02.058249'),(15,'sessions','0001_initial','2018-09-12 14:57:02.435371'),(16,'blog','0001_initial','2018-09-16 12:13:24.063882'),(17,'users','0001_initial','2018-09-17 12:24:30.321763'),(18,'blog','0002_post_memo','2018-11-07 12:03:50.514910');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('2zai9t84kf4kuhp19b7zglwssbln4p3d','M2IwOWQ3YjI3NzZlMTVmNzBhNTc2YjRhOTgxZjE4NWY4YzA0ZTU0OTp7fQ==','2018-11-05 15:44:50.196709'),('5c7vqthqd4qb6rrnpof99gtqxj6gcdwf','M2IwOWQ3YjI3NzZlMTVmNzBhNTc2YjRhOTgxZjE4NWY4YzA0ZTU0OTp7fQ==','2018-11-01 06:32:29.562828'),('87oq47b2jh5f1nifsass2n1uttisf3nk','M2IwOWQ3YjI3NzZlMTVmNzBhNTc2YjRhOTgxZjE4NWY4YzA0ZTU0OTp7fQ==','2018-11-05 15:50:48.628431'),('ccm7hjfuq8w0v6uq66yukbatsqyf5x1c','MGQzZGJlNjBkYzE2N2ZiODQyN2IwNzZmMDM1ZjZhMzg5OTIyYmNkNDp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjYjI5MmI5MjJlODkyYjI0OGNmOTdmNWI2MzVlYTU4NDNlZGUzNjYxIn0=','2018-10-04 05:34:28.936754'),('fou0nyjagl6l49e0s5uis4q8iknhgjfd','MGQzZGJlNjBkYzE2N2ZiODQyN2IwNzZmMDM1ZjZhMzg5OTIyYmNkNDp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjYjI5MmI5MjJlODkyYjI0OGNmOTdmNWI2MzVlYTU4NDNlZGUzNjYxIn0=','2018-10-16 06:06:43.880452'),('jceqhcix66vmc1s9coj0f0f9n118fpo5','M2IwOWQ3YjI3NzZlMTVmNzBhNTc2YjRhOTgxZjE4NWY4YzA0ZTU0OTp7fQ==','2018-10-15 07:00:21.994817'),('jq5d5ujla15hrcd75eoi2wmwkuttsyvd','MGQzZGJlNjBkYzE2N2ZiODQyN2IwNzZmMDM1ZjZhMzg5OTIyYmNkNDp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjYjI5MmI5MjJlODkyYjI0OGNmOTdmNWI2MzVlYTU4NDNlZGUzNjYxIn0=','2018-10-11 13:26:28.311511'),('jxgv7qrsll85frhayzf9n4o3d283eniu','M2IwOWQ3YjI3NzZlMTVmNzBhNTc2YjRhOTgxZjE4NWY4YzA0ZTU0OTp7fQ==','2018-11-01 06:33:01.502989'),('n3rts4fnqxp9zyim402g7ie5ko41i7la','MGQzZGJlNjBkYzE2N2ZiODQyN2IwNzZmMDM1ZjZhMzg5OTIyYmNkNDp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjYjI5MmI5MjJlODkyYjI0OGNmOTdmNWI2MzVlYTU4NDNlZGUzNjYxIn0=','2018-10-20 09:42:13.549826'),('q9pjajlut3jwjy9pgo2agq8gzb8o5n01','MGQzZGJlNjBkYzE2N2ZiODQyN2IwNzZmMDM1ZjZhMzg5OTIyYmNkNDp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjYjI5MmI5MjJlODkyYjI0OGNmOTdmNWI2MzVlYTU4NDNlZGUzNjYxIn0=','2018-10-20 09:27:37.119681'),('qawrcpisy1ms6bq1tlgxwle6itkdk4gs','MTM2NTU1MzY2NGJiNWY5MDYzMTcwMzM0OTY0NmZjNjBkNjEzNGUxYjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhMTBiNTEyY2E3Nzc5MDhjMDU1ZWI3NzFmZTI4OWZlMWRjZTA0ODY4In0=','2018-11-21 12:17:02.141879'),('rei9u3esfd6o1kjhf6guvnzeldqrm4nh','MGQzZGJlNjBkYzE2N2ZiODQyN2IwNzZmMDM1ZjZhMzg5OTIyYmNkNDp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjYjI5MmI5MjJlODkyYjI0OGNmOTdmNWI2MzVlYTU4NDNlZGUzNjYxIn0=','2018-10-11 13:34:01.547291'),('s7ru3ybcvxdj40ijs4exbxti6qraq6i0','M2IwOWQ3YjI3NzZlMTVmNzBhNTc2YjRhOTgxZjE4NWY4YzA0ZTU0OTp7fQ==','2018-11-01 06:34:10.618831'),('x01njc0c16xbi7ttsh5fmppl514lulqw','M2IwOWQ3YjI3NzZlMTVmNzBhNTc2YjRhOTgxZjE4NWY4YzA0ZTU0OTp7fQ==','2018-11-05 15:43:42.187399');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_profile`
--

DROP TABLE IF EXISTS `users_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_profile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `image` varchar(100) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `users_profile_user_id_2112e78d_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_profile`
--

LOCK TABLES `users_profile` WRITE;
/*!40000 ALTER TABLE `users_profile` DISABLE KEYS */;
INSERT INTO `users_profile` VALUES (1,'default.jpg',1),(3,'profile_pics/pic001.jpg',2),(4,'default.jpg',3);
/*!40000 ALTER TABLE `users_profile` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-28 15:36:13
