CREATE TABLE `cars` (
  `id` INT(11) NOT NULL,
  `name` VARCHAR(50) NOT NULL,
  `available` BOOLEAN DEFAULT TRUE,
  `vin` VARCHAR(36) NOT NULL,
  `make` VARCHAR(50) NOT NULL,
  `madle` VARCHAR(50) NOT NULL,
  `year`INT NOT NULL ,
  `MOT` DATE NOT NULL,
  `price` INT NOT NULL,
  `colour` VARCHAR(50) NOT NULL,
  `other_details` TEXT,
  PRIMARY KEY (`id`),

) ENGINE=InnoDB DEFAULT CHARSET=utf8;