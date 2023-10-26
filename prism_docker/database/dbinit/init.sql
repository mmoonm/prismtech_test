# create  users
CREATE USER 'prism' @'%' IDENTIFIED WITH mysql_native_password BY 'prism';
CREATE USER 'prism' @'localhost' IDENTIFIED WITH mysql_native_password BY 'prism';

FLUSH PRIVILEGES;

# create databases
CREATE DATABASE IF NOT EXISTS `prism` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

# grant super user permission to paykit user
GRANT ALL PRIVILEGES ON *.* TO 'prism' @'%';
GRANT ALL PRIVILEGES ON *.* TO 'prism' @'localhost';

FLUSH PRIVILEGES;