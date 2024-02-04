CREATE TABLE if not exists drinks(
	id int(6) unsigned auto_increment primary key,
    drinkname varchar(30) not null,
    price float(6, 2) not null,
    color varchar(50),
    descript varchar(100)
)

INSERT INTO drinks(drinkname, price, color, descript) VALUES (
	'Martini', 8.99, 'Clear', 'Classic cocktail with gin and vermouth'
)

INSERT INTO drinks(drinkname, price, color, descript) VALUES (
	'Margarita', 7.50, 'Yellow', 'Tequila-based cocktail with lime and triple sec'
)

INSERT INTO drinks(drinkname, price, color, descript) VALUES (
	'Old Fashioned', 9.75, 'Brown', 'Whiskey cocktail with sugar and bitters'
)

INSERT INTO drinks(drinkname, price, color, descript) VALUES (
	'Cosmopolitan', 10.25, 'Pink', 'Vodka-based cocktail with cranberry juice and triple sec'
)

INSERT INTO drinks(drinkname, price, color, descript) VALUES (
	'Negroni', 11.50, 'Red', 'Bitter cocktail with gin, vermouth, and Campari'
)

INSERT INTO drinks(drinkname, price, color, descript) VALUES (
	'Whiskey Sour', 8.75, 'Golden', 'Whiskey cocktail with lemon juice and simple syrup'
)

INSERT INTO drinks(drinkname, price, color, descript) VALUES (
	'Piña Colada', 9.99, 'White', 'Tropical cocktail with rum, coconut cream, and pineapple juice'
)

INSERT INTO drinks(drinkname, price, color, descript) VALUES (
	'Mai Tai', 12.50, 'Amber', 'Tiki cocktail with rum, lime, and orgeat syrup'
)

INSERT INTO drinks(drinkname, price, color, descript) VALUES (
	'Moscow Mule', 7.95, 'Copper', 'Vodka-based cocktail with ginger beer and lime'
)

INSERT INTO drinks(drinkname, price, color, descript) VALUES (
	'Manhattan', 10.75, 'Dark Red', 'Classic cocktail with whiskey, vermouth, and bitters'
)

SELECT * FROM drinks
