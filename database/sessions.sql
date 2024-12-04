CREATE TABLE `clients` (
  `session_id` VARCHAR(36) NOT NULL,
  `previous_session_id` VARCHAR(36) DEFAULT NULL,
  `user_id` INT(11),
  `login_status` BOOLEAN DEFAULT FALSE,
  `token` VARCHAR(255) DEFAULT NULL,
  `last_request` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- / last updated 
  `save_data` TEXT,
  `ip_address` VARCHAR(45) NOT NULL,
  `user_agent` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`session_id`),
  FOREIGN KEY (`user_id`) REFERENCES `users`(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;