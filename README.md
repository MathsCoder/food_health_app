# Food APP Setup Guide

Instructions for running this Flask application using a Conda environment.

## Steps:

1. Create the environment
2. Install dependencies
3. Initialise the database

## Prerequisites

Before you begin, ensure you have the following installed:

- [Anaconda or Miniconda](https://www.anaconda.com/products/individual)
- Virtualenv can also be used instead of conda

## Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https
cd your-repository
mkdir logs # if it doesn't exist
```

## Step 2: Create the environment

```bash
conda create -n food_app python=3.11
conda activate food_app
```

## Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Download .pkl file

Download the `.pkl` file from [here](https://drive.google.com/file/d/1-88jnloMkVaWrKwW7LO6QjzzwimVXUtk/view?usp=sharing)
and place it in `application/uploads/` directory of the project.

## Step 5: Initialise the database

```bash
export FLASK_APP=app.py
flask shell
from application import db
db.create_all()
```

## Step 6: Run the application

```bash
flask --app app --debug run --port 5000
```


