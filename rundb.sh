docker build -t mysql_db database
docker run --rm -d -p 3306:3306 --name db mysql_db