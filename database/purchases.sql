CREATE TABLE purchases (
    `purchase_id` INT(11) PRIMARY KEY,
    `user_id` VARCHAR(36),
    `car_id` INT(11),
    `purchase_date` DATE,
    `total_price` DECIMAL(10, 2),
    `details` TEXT,
    PRIMARY KEY (`purchase_id`),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`id`),
    FOREIGN KEY (`car_id`) REFERENCES `cars`(`id`)
);