#!/usr/bin/env bash

uwsgi --socket 127.0.0.1:8080 --protocol http --wsgi-file "wsgi.py" --virtualenv "/Users/tomasrasymas/.virtual_envs/mamamamailt-backend"