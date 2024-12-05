CREATE TABLE `bookings` (
  `id` INT(11) NOT NULL,
    `user_id` VARCHAR(36) NOT NULL,
    `type` ENUM('inspection', 'test_drive', 'collection') NOT NULL,
    `status` ENUM('pending', 'confirmed', 'completed', 'cancelled') NOT NULL,
    `vehicle_id` INT(11) NOT NULL,
    `scheduled_at` DATETIME NOT NULL,
    `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES `users`(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;