# North County Bidding Internal Directory (NCBID)
## Requirements
_* Command instructions are based on Debian-Ubuntu_

#### Download pip requirements

`pip install -r requirements.txt`

## Setting up the PostgreSQL Database

Install [PostgreSQL](https://www.postgresql.org/download/) and psycopg2:

```bash
sudo apt-get install postgresql
```

#### Configure PostgreSQL
1. Login as the user "postgres":

    `sudo -i -u postgres`

2. Create a database called "nchsauction":

  `createdb nchsauction`
3. Run `psql` on the database "nchsauction" and create a user:
  ```PosgreSQL
  psql -d nchsauction
  CREATE USER nchsauction WITH LOGIN PASSWORD 'password';
  \q
  exit
  ```  
  This user for the Django's database has the following credentials:  
  __Username:__ nchsauction  
  __Password:__ password

4. Modify the configuration file `pg_hba.conf` in the directory `/etc/postgresql/<version>/main/`. The path may vary depending on the version of PostgreSQL.

    `sudo nano /etc/postgresql/9.5/main/pg_hba.conf`

    Modify the "peer" authentication method to "md5".
    ```
    # "local" is for Unix domain socket connections only
    local   all             all                      peer
    ```
    After modification, your configuration should look like this:
    ```
    # "local" is for Unix domain socket connections only
    local   all             all                      md5
    ```
    Save the `pg_hba.conf` file and restart the PostgreSQL service:

    `sudo service postgresql restart`
5. You should successfully login to the "shenandoah" database with this command. Provide the password for the user "shenandoah" as necessary:

  `psql -d nchsauction -U nchsauction -W`

  To exit, return `\q`

6. Now you can migrate PostgreSQL in Django:

  `python manage.py migrate`
