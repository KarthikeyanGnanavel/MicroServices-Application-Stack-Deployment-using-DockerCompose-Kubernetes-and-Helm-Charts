#!/bin/bash
mongosh <<EOF
use user_db;
db.createCollection("users");
EOF
