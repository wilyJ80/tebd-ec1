#!/bin/bash

# Load original script (prerequisite: sqlite3 binary on path)
sqlite3 olap.db < olap.sql

# Generate diagrams (needs tbls installed and on PATH)
tbls doc sqlite:./olap.db
