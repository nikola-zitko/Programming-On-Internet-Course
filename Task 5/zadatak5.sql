-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 14, 2020 at 06:46 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `zadatak5`
--

-- --------------------------------------------------------

--
-- Table structure for table `collections`
--

CREATE TABLE `collections` (
  `collection_id` int(11) NOT NULL,
  `collection` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `collections`
--

INSERT INTO `collections` (`collection_id`, `collection`) VALUES
(1, 'cards'),
(2, 'pictures'),
(3, 'car');

-- --------------------------------------------------------

--
-- Table structure for table `image`
--

CREATE TABLE `image` (
  `id` int(11) NOT NULL,
  `path` varchar(255) NOT NULL,
  `counter` int(11) NOT NULL,
  `created` timestamp NULL DEFAULT NULL,
  `last` timestamp NULL DEFAULT NULL,
  `collection_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `image`
--

INSERT INTO `image` (`id`, `path`, `counter`, `created`, `last`, `collection_id`) VALUES
(1, 'slika1.jpg', 9, '2020-01-11 23:00:00', '2020-01-14 17:45:31', 1),
(12, 'priroda.jpg', 1, '2020-01-14 16:15:30', '2020-01-14 16:46:31', 2),
(14, 'cars.jpg', 0, '2020-01-14 16:16:24', '2020-01-14 16:16:24', 3),
(15, 'slika2.jpg', 5, '2020-01-14 16:55:26', '2020-01-14 17:30:39', 1),
(16, 'priroda.png', 0, '2020-01-14 17:06:10', '2020-01-14 17:06:10', 2);

-- --------------------------------------------------------

--
-- Table structure for table `sessions`
--

CREATE TABLE `sessions` (
  `session_id` int(11) NOT NULL,
  `data` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sessions`
--

INSERT INTO `sessions` (`session_id`, `data`) VALUES
(18, '{\"user_id\": 10, \"collection_id\": 1}'),
(20, '{\"user_id\": 10, \"collection_id\": 1}'),
(21, '{\"user_id\": 10, \"collection_id\": 1}'),
(22, '{\"user_id\": 10, \"collection_id\": 1}'),
(24, '{\"user_id\": 10, \"collection_id\": 1}'),
(25, '{\"user_id\": 10, \"collection_id\": 1}'),
(26, '{\"user_id\": 10, \"collection_id\": 1}'),
(27, '{\"user_id\": 10, \"collection_id\": 1}'),
(29, '{\"user_id\": 10, \"collection_id\": 1}'),
(34, '{\"user_id\": 6, \"collection_id\": 1}'),
(35, '{\"user_id\": 6, \"collection_id\": 1, \"username\": \"niko\"}'),
(36, '{}'),
(37, '{}'),
(38, '{}'),
(39, '{}'),
(40, '{\"user_id\": 6, \"collection_id\": 1, \"username\": \"niko\"}'),
(41, '{\"user_id\": 6, \"collection_id\": 1, \"username\": \"niko\"}'),
(42, '{\"user_id\": 6, \"collection_id\": 1, \"username\": \"niko\"}'),
(43, '{\"user_id\": 6, \"collection_id\": 1, \"username\": \"niko\"}'),
(46, '{\"user_id\": 11, \"collection_id\": 1, \"username\": \"ante\"}');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `role` enum('admin','user') NOT NULL DEFAULT 'user'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `username`, `password`, `email`, `role`) VALUES
(6, 'niko', '$2b$12$ClC73mJA2DSIkKAme2wtSuQ.6ds9zT.9WlLoA/djHnGPdlw2VYlNW', '', 'user'),
(7, 'mateo', '$2b$12$fmQnRTtajWJVgEKmw3/YreWRjq7SAh6wLOm3yLP9X0IdfNr7MV4qa', '', 'admin'),
(10, 'mate', '$2b$12$Mon2FjNUP4eMoTCOnFQ5au0Pw/nKwiWTPk8mkMEox2bZ6lKbeecY6', 'mate@mate.hr', 'admin'),
(11, 'ante', '$2b$12$DeOKjTB9X8zPDjrKNoFB8..fNkThj.KwT3P6F1Sit2CZCF.wRJMA2', 'ante@ante.com', 'user');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `collections`
--
ALTER TABLE `collections`
  ADD PRIMARY KEY (`collection_id`);

--
-- Indexes for table `image`
--
ALTER TABLE `image`
  ADD PRIMARY KEY (`id`),
  ADD KEY `collection_id` (`collection_id`);

--
-- Indexes for table `sessions`
--
ALTER TABLE `sessions`
  ADD PRIMARY KEY (`session_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `collections`
--
ALTER TABLE `collections`
  MODIFY `collection_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `image`
--
ALTER TABLE `image`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `sessions`
--
ALTER TABLE `sessions`
  MODIFY `session_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
