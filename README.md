NGS Database
============


Installation
------------


Quickstart
----------


Deploying Test Instance
-----------------------

0. Cleanup

   0a. check for any service stacks currently running
   
       docker stack ls
       
   0b. remove any unwanted service stacks
   
       docker stack rm <service name>


1. If you haven't already pull postgres image from Dockerhub

   docker pull postgres

2. deploy service stack

   docker stack deploy -c docker-compose.yaml postgres

3. connect to database, create missing tables

   3a. enter python interactive terminal
   3b. import orm
   3c. use init_db function to connect

       e.g. uri for sqlalchemy:

       uri = 'postgresql+psycopg2://postgres@localhost:5432/postgres'
       db = orm.init_db(uri)


Jupyterlab
----------

- rebuild jupyter lab's frontend after nbdime is installed:

  jupyter lab clean && jupyter lab build


- integrate nbdime with git

  nbdime config-git --enable


- make conda environment available as kernel

  python -m ipykernel install --user --name ngsdb --display-name "ngsdb"


Alembic: Migrating Database Schema
----------------------------------

1. initialize migration environment (only once per project)

   alembic init alembic

2. create migration script

   alembic revision -m 'update samples table'

3. modify revision script
4. execute migration


Alembic: Quick Tips
-------------------

- migrate to specific version

  alembic upgrade <target-revision> || alembic downgrade <target-revision>


- list all migrations (from newest to oldest)

  alembic history


- downgrading schema

  # revert to previous schema
  alembic downgrade -1
  
  # revert to specific schema
  alembic downgrade <version-id>


sqlacodegen
-----------

- Auto-generate candidate declarative database schema

  sqlacodegen <db-uri>
