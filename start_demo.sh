docker run --name auto_db -p 3307:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=auto_demo -d mysql
docker run --name tulli_db -p 3308:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=tulli_demo -d mysql
docker run --name yritys_db -p 3309:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=yritys_demo -d mysql
docker run --name demo_db -p 3311:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=demo_demo -d mysql
