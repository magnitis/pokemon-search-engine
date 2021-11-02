# Pokemon Search Engine

Simple search engine which given a valid Pokemon name, returns its Shakespearean description.

## Overview

This project is developed with a **React** front-end (*Node.js v16*) and a **Flask** API back-end (*Python 3.9*). The front-end connects to the back-end by making HTTP requests for desired data. React and Flask are containerized and managed with **Docker Compose**.

### How to run with Docker

Make sure you have [Docker desktop](https://www.docker.com/products/docker-desktop) or [Docker](https://www.docker.com/) installed.

Create a local copy of this repository and run

    docker-compose build

This spins up Compose and builds a local development environment according to the specifications in [docker-compose.yml](https://github.com/magnitis/pokemon-search-engine/blob/master/docker-compose.yml). Keep in mind that this file contains settings for development, and not production.

After the containers have been built (this may take a few minutes), run

    docker-compose up

This will boot up a local server for Flask (on port 5000) and React (on port 3000). Open [http://localhost:3000](http://localhost:3000) to view the search engine in the browser.

### How to run manually

#### Prerequisites

* Node.Js v16 installed -- <https://nodejs.org/en/blog/release/v16.3.0/>

* Python 3.9.x installed -- <https://installpython3.com>

* Python 3 PIP installed -- <https://pip.pypa.io/en/stable/installing>

#### Installation

    git clone https://github.com/magnitis/pokemon-search-engine.git
    cd pokemon-search-engine
    pip install -r api/requirements.txt


To spin up the front-end run

    cd client && yarn start

Then to spin up the back-end, open a new terminal and run

    cd client && yarn start-api

The app will be running in development mode. Open [http://localhost:3000](http://localhost:3000) to view it in the browser.


#### Running tests

React front-end. Launches the test runner in the interactive watch mode.

    cd client && yarn test

Flask back-end. Running both unit and integration tests.

    cd api && pytest -q tests

