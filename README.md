#### The Voice API


**Pre-requisites**
- Docker (preferred version 17.12.0-ce)


**Quick deploy**
- Commands to spin-up and destroy containers

        docker-compose up
        # - Spinup two containers,
        #   thevoice app and postgres db
        # - Execute management commands to
        #   create db, migrate schema and apply fixtures
        # - Run test cases
        # - Start server

        docker-compose down
        # - Take down containers


**User types**
- Admin

        username: admin
        password: thevoiceadmin

- Mentors

        username: seal.seal
        password: thevoiceseal

        username: delta.goodrem
        password: thevoicedelta

        username: kelly.rowland
        password: thevoicekelly

        username: boy.george
        password: thevoiceboy


**Django rest framework web api / Django admin panel**

    Django rest framework web api:  http://localhost:8000/
    Django admin panel:             http://localhost:8000/admin/


**Usage**
- Login as below, response will be JWT token

        curl -X POST "http://localhost:8000/login/" -H  "Content-Type: application/json" -d "{\"password\":\"thevoiceseal\",\"username\":\"seal.seal\"}"

        {"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6InNlYWwuc2VhbCIsImV4cCI6MTUxODA5NDk3MywiZW1haWwiOiIifQ.ZypimbRniPs34T2ip1E5YOqnPg52e9PFe01y1m_JkX8"}

- Lets save token as environment variables

        export VOICE_TOKEN=Authorization:JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6InNlYWwuc2VhbCIsImV4cCI6MTUxODA5NDk3MywiZW1haWwiOiIifQ.ZypimbRniPs34T2ip1E5YOqnPg52e9PFe01y1m_JkX8

- List teams and their members for logged in mentor/admin

        curl -X GET "http://localhost:8000/teams/" -H  "accept: application/json" -H $VOICE_TOKEN

- List candidate performances. In case of mentor - performances will be listed only if candidate belongs to one the logged in mentors team

        curl -X GET "http://localhost:8000/performances/candidate/19/" -H  "accept: application/json" -H $VOICE_TOKEN

- List performance scores. In case of mentor - scores will be listed only if candidate belongs to one the logged in mentors team

        curl -X GET "http://localhost:8000/scores/performance/4/" -H  "accept: application/json" -H $VOICE_TOKEN

- Others

        curl -X GET "http://localhost:8000/teams/1/" -H  "accept: application/json" -H $VOICE_TOKEN

        curl -X GET "http://localhost:8000/performances/" -H  "accept: application/json" -H $VOICE_TOKEN
        curl -X GET "http://localhost:8000/performances/1/" -H  "accept: application/json" -H $VOICE_TOKEN

        curl -X GET "http://localhost:8000/scores/" -H  "accept: application/json" -H $VOICE_TOKEN
        curl -X GET "http://localhost:8000/scores/1/" -H  "accept: application/json" -H $VOICE_TOKEN

        # NOTE: Above are not really required by the UI
