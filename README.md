# Api4TimeKeeping
- `docker-compose build` to build image (recommend: once time to execute)
- `docker-compose up -d` to start (recommend: once time to execute)
- `docker-compose restart` to rebuild and restart 
- `docker-compose down` to stop (recommend: once time to execute)


## My database
```
Create table Employee(id int PRIMARY KEY AUTO_INCREMENT, 
                        firstName text NOT NULL, 
                        lastName text NOT NULL, 
                        img LONGBLOB, 
                        username text NOT NULL, 
                        password text NOT NULL);

Create table Product (id int PRIMARY KEY AUTO_INCREMENT, 
                name text NOT NULL,  
                price float NOT NULL);

Create table TimeKeeping( id int PRIMARY KEY AUTO_INCREMENT,
                idEmployee int, 
                dateTimeKeeping datetime, 
                FOREIGN KEY(idEmployee) REFERENCES Employee(id));

Create table InfoTimeKeeping( idTime int , idProduct int,  num1Pro int NOT NULL, num0Pro int NOT NULL,  PRIMARY KEY(idTime,idProduct), FOREIGN KEY(idTime) REFERENCES TimeKeeping(id), FOREIGN KEY(idProduct) REFERENCES Product(id));

```
