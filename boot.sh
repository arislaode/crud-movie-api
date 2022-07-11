#!/bin/sh

exec gunicorn --reload -b :8082 --access-logfile - --error-logfile - api:app -t 240
