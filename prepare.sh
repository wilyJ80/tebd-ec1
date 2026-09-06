#!/bin/bash

# Remove previous tables
rm oltp.db
rm olap.db

# Load OLTP script  (prerequisite: sqlite3 binary on path)
sqlite3 oltp.db < oltp.sql

# Load OLAP script
sqlite3 olap.db < olap.sql
