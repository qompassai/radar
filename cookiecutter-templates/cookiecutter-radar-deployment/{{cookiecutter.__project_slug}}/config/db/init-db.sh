#!/usr/bin/env bash
set -e

psql -v ON_ERROR_STOP=1 --username "${POSTGRES_USER}" --dbname "${POSTGRES_DB}" <<-EOSQL
	CREATE USER "radar";
	CREATE DATABASE "restapi";
	CREATE DATABASE "mlflow-tracking";
	REVOKE ALL ON DATABASE "restapi" FROM "public";
	REVOKE ALL ON DATABASE "mlflow-tracking" FROM "public";
	GRANT ALL PRIVILEGES ON DATABASE "restapi" TO "radar";
	GRANT ALL PRIVILEGES ON DATABASE "mlflow-tracking" TO "radar";
	ALTER ROLE "radar" ENCRYPTED PASSWORD '${POSTGRES_USER_RADAR_PASSWORD}';
EOSQL

psql -v ON_ERROR_STOP=1 --username "${POSTGRES_USER}" --dbname "restapi" <<-EOSQL
	REVOKE USAGE ON SCHEMA "public" FROM "public";
	REVOKE CREATE ON SCHEMA "public" FROM "public";
	GRANT USAGE ON SCHEMA "public" TO "radar";
	GRANT CREATE ON SCHEMA "public" TO "radar";
EOSQL

psql -v ON_ERROR_STOP=1 --username "${POSTGRES_USER}" --dbname "mlflow-tracking" <<-EOSQL
	REVOKE USAGE ON SCHEMA "public" FROM "public";
	REVOKE CREATE ON SCHEMA "public" FROM "public";
	GRANT USAGE ON SCHEMA "public" TO "radar";
	GRANT CREATE ON SCHEMA "public" TO "radar";
EOSQL
