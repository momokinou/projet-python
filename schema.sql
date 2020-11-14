CREATE DATABASE IF NOT EXISTS StreamingSite CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
USE 'StreamingSite';

CREATE TABLE mangas      (
                        id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                        title LONGTEXT NOT NULL,
                        alt_title LONGTEXT,
                        category ENUM('Kodomo', 'Shonen', 'Shojo', 'Seinen', 'Josei', 'Seijin', 'Webcomic', 'Hentai', 'Unknown'),
                        description LONGTEXT,
                        release_date DATE NOT NULL,
                        ending_date DATE,
                        studio ENUM('Shueisha', 'D&C Media, Kakao') NOT NULL,
                        nbr_volume INT NOT NULL,
                        nbr_chap INT NOT NULL,
                        id_language INT NOT NULL,
                        FOREIGN KEY (id_language) REFERENCES language (id)
);

CREATE TABLE users      (
                        id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                        nickname LONGTEXT NOT NULL,
                        password LONGTEXT NOT NULL,
                        email LONGTEXT NOT NULL,
                        gender ENUM('male', 'female', 'unknown'),
                        id_language INT,
                        FOREIGN KEY (id_language) REFERENCES language (id)
);

CREATE TABLE language    (
                        id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                        name LONGTEXT NOT NULL
);

CREATE TABLE chapter   (
                        id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                        nbr_chapter INT NOT NULL,
                        title LONGTEXT NOT NULL,
                        id_manga INT NOT NULL,
                        id_language INT NOT NULL,
                        FOREIGN KEY (id_language) REFERENCES language (id),
                        FOREIGN KEY (id_manga) REFERENCES manga (id)
);

/*add to python*/
/*INSERT INTO language(name) 
VALUES ('Arabic'), ('Bengali'), ('Bulgarian'), ('Burmese'), ('Catalan'), ('Chinese(Simp)'), ('Chinese(Hong-Kong)'), ('Czech'), ('Danish'), ('Dutch'), ('English'), ('Filipino'), ('Finnish'), ('French'), ('German'), ('Greek'), ('Hebrew'), ('Hindi'), ('Hungarian'), ('Indonesian'), ('Italian'), ('Japanese'), ('Korean'), ('Lithuanian'), ('Malay'), ('Mongolian'), ('Norwegian'), ('Other'), ('Persian'), ('Polish'), ('Portuguese(BR)'), ('Portuguese(PT)'), ('Romanian'), ('Russian'), ('Serbo-Russian'), ('Spanish(ES)'), ('Spanish(LATAM)'), ('Swedish'), ('Thai'), ('Turkish'), ('Ukrainian'), ('Vietnamese');

INSERT INTO users(nickname, password, email, gender, id_language) 
VALUES ('vani', 'supervani', 'vani@gmail.fr', 'male', 14), ('hamtoé', 'jambon94', 'hamtoé@mail.com', 'male', 14), ('superuser', 'jesuissuperuser', 'user@user.fr', 'unknown', 28), ('moi', 'lui', 'elle@onnesaitplus.net', 'unknown', 5), ('Jacqueline', 'monchienestblanc', 'jacquelinevillard@hotmail.fr', 'female', 13);

INSERT INTO mangas(title, alt_title, category, description, release_date, ending_date, studio, nbr_volume, nbr_chap, id_language)
VALUES 
('ワンピース', 'One Piece', 'Shonen', 'Gloire, fortune et puissance, c\'est ce que possédait Gold Roger, le tout puissant roi des pirates, avant de mourir sur l\'échafaud. Mais ses dernières paroles ont éveillées bien des convoitises, et lança la fabuleuse "ère de la piraterie", chacun voulant trouver le fabuleux trésor qu\'il disait avoir laissé. A 17 ans, Luffy prend la mer dans une petite barque avec pour but de réunir un équipage de pirates, mais de pirates pas comme les autres, qui devront partager sa conception un peu étrange de la piraterie. L\'aventure est lancée.', '1997-12-24', '2020-04-03', 'Shueisha', 97, 974, 22),
('나 혼자만 레벨업', 'Solo Leveling, Only I level up, Na Honjaman Level Up', 'Shonen', 'Sung Jin Woo est considéré comme le plus faible des Chasseurs de rang E... Autrement dit le plus faible parmi les faibles. Il est tellement faible qu\'il est surnommé par ses confrères, le « Faible ». Avec une équipe de Chasseurs, il se rend dans un donjon de rang D. Malheureusement, l\'équipe se retrouve piégée dans une salle avec des monstres qui ne sont pas du tout du niveau du donjon... S\'en suit un massacre... Et Sung Jin Woo, aux portes de la mort arrive à acquérir une capacité pour le moins étrange...', '2019-09-26', '2020-08-27', 'D&C Media, Kakao', 3, 126, 23);
*/