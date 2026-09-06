#!/bin/bash

# Load OLTP script  (prerequisite: sqlite3 binary on path)
sqlite3 oltp.db < oltp.sql

# Load OLAP script
sqlite3 olap.db < olap.sql

# Generate diagrams (needs tbls installed and on PATH)
tbls doc sqlite:./olap.db
