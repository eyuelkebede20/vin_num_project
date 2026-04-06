#!/bin/bash

# Root directory
PROJECT_NAME="vin_decoder_project"

# Create folders
mkdir -p $PROJECT_NAME/data
mkdir -p $PROJECT_NAME/db
mkdir -p $PROJECT_NAME/core

# Create files
touch $PROJECT_NAME/data/raw_data.csv

touch $PROJECT_NAME/db/schema.sql
touch $PROJECT_NAME/db/setup_db.py

touch $PROJECT_NAME/core/__init__.py
touch $PROJECT_NAME/core/decoder.py
touch $PROJECT_NAME/core/validator.py

touch $PROJECT_NAME/main.py
touch $PROJECT_NAME/requirements.txt

echo "Project structure created successfully!"