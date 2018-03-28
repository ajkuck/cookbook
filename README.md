Cookbook - Recipes from the margins.
====

Often times when cooking or baking, we scour the internet (and physical books) for recipes, and end up making
something that draws from mulitple sources.  Sadly, when we find something that we like, it's hard to recall _which_
sources contributed to what we'd made previous.

This is a small website to index and track the recipes that we actually made.

Installation
----

Copy the sample config file to the correct location:

    $ cp main.sample.ini main.ini
    
You'll need to configure the values in `main.ini` to match what you want. In particular, `SQLALCHEMY_DATABASE_URI` needs
to provide the correct authentication details for your database details. The format is a standard database URI, i.e.:

    driver://username:password@host:port/database
    
For MySQL with PyMySQL as the driver, use `mysql+pymysql://` as the protocol.

---

Log into MySQL using a user that has `CREATE DATABASE` privileges, and create the database using the name you specified
in `main.ini`.

    $ mysql -u root -p
    Enter password: 
    Welcome to the MySQL monitor...
    
    mysql> CREATE DATABASE `cookbook`;
    Query OK, 1 row affected (0.00 sec)

    mysql> exit
    Bye
    
Finally, run `create_database.py` to create the required tables:

    $ python3 create_database.py
    
You should be ready to go - run `python3 application.py` to launch the app, and visit `http://localhost:5000/` to see it
in action.
