CREATE TABLE if not exists inventory(
	id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    brand VARCHAR(30) NOT NULL,
    model VARCHAR(30) NOT NULL,
    load_rating INTEGER,
    speed_rating VARCHAR(5),
    inv_type VARCHAR(20),
    stock INTEGER
);

SELECT * FROM inventory;

INSERT INTO inventory(brand, model, load_rating, speed_rating, inv_type, stock)
VALUES ('Michelin', 'Pilot Sport 4S', 98, 'Y', 'Summer', 50);

INSERT INTO inventory(brand, model, load_rating, speed_rating, inv_type, stock)
VALUES ('Bridgestone', 'Potenza RE980AS', 94, 'W', 'All-Season', 30);

INSERT INTO inventory(brand, model, load_rating, speed_rating, inv_type, stock)
VALUES ('Goodyear', 'Eagle F1 Asymmetric 5', 96, 'Y', 'Summer', 60);

INSERT INTO inventory(brand, model, load_rating, speed_rating, inv_type, stock)
VALUES ('Pirelli', 'P Zero Nero GT', 95, 'Y', 'Summer', 40);

INSERT INTO inventory(brand, model, load_rating, speed_rating, inv_type, stock)
VALUES ('Continental', 'ExtremeContact DWS06', 98, 'W', 'All-Season', 55);

INSERT INTO inventory(brand, model, load_rating, speed_rating, inv_type, stock)
VALUES ('Hankook', 'Ventus V12 Evo2', 96, 'Y', 'Summer', 25);

INSERT INTO inventory(brand, model, load_rating, speed_rating, inv_type, stock)
VALUES ('Yokohama', 'Advan Sport A/S+', 97, 'W', 'All-Season', 35);

INSERT INTO inventory(brand, model, load_rating, speed_rating, inv_type, stock)
VALUES ('Dunlop', 'Direzza ZIII', 94, 'W', 'Summer', 20);

INSERT INTO inventory(brand, model, load_rating, speed_rating, inv_type, stock)
VALUES ('BFGoodrich', 'g-Force COMP-2 A/S', 97, 'W', 'All-Season', 45);

INSERT INTO inventory(brand, model, load_rating, speed_rating, inv_type, stock)
VALUES ('Firestone', 'Firehawk Indy 500', 94, 'W', 'Summer', 50);