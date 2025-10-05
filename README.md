# hack-demo-61n

## How to use

### Create venv and install dependencies

Enter the venv.

You can find Python requirements from requirements.txt. You need docker with mysql image.

```console
docker pull mysql
```
### Boot up MySQL servers with start_demo.sh

Create tables to MySQL servers, use processdata.py. Data creation with processdata.py could be possible, but if it doesn't work, just connect to the MySQL servers and commit them yourself. Mock data can be found from mock.sql

### Start Flask 

Start flask with `flask run`.