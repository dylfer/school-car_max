CREATE TABLE `cars` (
  `id` VARCHAR(36) NOT NULL,
  `vin` VARCHAR(36) NOT NULL,
  `make` VARCHAR(50) NOT NULL,
  `madle` VARCHAR(50) NOT NULL,
  `year`INT NOT NULL ,
  `price` INT NOT NULL,
  `colour` VARCHAR(50) NOT NULL,
  `other_details` TEXT,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`id`) REFERENCES ``(`car_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;