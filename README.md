# Python + MongoDB CRUD (AAC Dataset)

Reusable **Python CRUD module** using **PyMongo**, plus a Jupyter notebook that tests **Create** and **Read** against the Austin Animal Center outcomes dataset.

> This is part of the SNHU CS-340 coursework. It lays the foundation to connect a client-side dashboard to a MongoDB backend.

## Features
- Object-oriented, importable module: `AnimalShelter`
- **Create**: insert a document (`insert_one`)
- **Read**: query many documents using `find()` (cursor → list)
- Robust error handling and inline documentation
- Simple test notebook: import, connect, insert, read-back

## Tech Stack
- Python 3
- PyMongo
- MongoDB Community
- Jupyter Lab/Notebook

## Dataset
Austin Animal Center outcomes CSV (`aac_shelter_outcomes.csv`).

## Setup

### 1) Import data and create user
```bash
cd ./datasets
mongoimport --type=csv --headerline --db aac --collection animals --drop ./aac_shelter_outcomes.csv

mongosh
use admin
db.createUser({
  user: "aacuser",
  pwd: passwordPrompt(),
  roles: [ { role:"readWrite", db:"aac" } ]
})
 Python + MongoDB CRUD (AAC Dataset)

R
