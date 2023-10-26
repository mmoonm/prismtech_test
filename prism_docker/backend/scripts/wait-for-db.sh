#!/bin/sh

set -e
until mysql -uprism -pprism -hprismdb -e 'select 1'; do
  >&2 echo "MySQL is unavailable - sleeping"
  sleep 1
done

  
>&2 echo "MySQL is up - executing command"
exec "$@"

