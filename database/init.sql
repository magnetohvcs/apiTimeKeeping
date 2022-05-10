create database TimeKeeping;

use TimeKeeping;


Create table Employee(id int PRIMARY KEY AUTO_INCREMENT, 
                        firstName text NOT NULL, 
                        lastName text NOT NULL, 
                        img LONGBLOB, 
                        username text NOT NULL, 
                        password text NOT NULL,
                        FOREIGN KEY(idFactory) REFERENCES Factory(id));

Create table Product (id int PRIMARY KEY AUTO_INCREMENT, 
                name text NOT NULL,  
                price float NOT NULL);

Create table TimeKeeping( id int PRIMARY KEY AUTO_INCREMENT,
                idEmployee int, 
                dateTimeKeeping datetime, 
                FOREIGN KEY(idEmployee) REFERENCES Employee(id));

Create table InfoTimeKeeping( idTime int , idProduct int,  num1Pro int NOT NULL, num0Pro int NOT NULL,  PRIMARY KEY(idTime,idProduct), FOREIGN KEY(idTime) REFERENCES TimeKeeping(id), FOREIGN KEY(idProduct) REFERENCES Product(id));


INSERT INTO Factory values(1,"A");
INSERT INTO Employee values(1,"Nguyen","Van A",1,"","admin","admin");