CREATE TABLE if not exists users(
	id int(6) unsigned auto_increment primary key,
    firstname varchar(30) not null,
    lastname varchar(30) not null,
    email varchar(50)
)

/* 
	auto_increment: instantly adds new primary key number every new entry of an instance
    unsigned: Does not include negative numbers
    not null: Data cannot be empty
*/

insert into users(firstname, lastname, email) values (
	"otto",
    "dobretsberger",
    "something@something.com"
)

select * from users 