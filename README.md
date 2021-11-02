# Pokemon Search Engine

Simple search engine which given a valid Pokemon name, returns its Shakespearean description.

## Overview

This project is developed with a **React** front-end (*Node.js v16*) and a **Flask** API back-end (*Python 3.9*). The front-end connects to the back-end by making HTTP requests for desired data. React and Flask are containerized and managed with **Docker Compose**.

### How to run with Docker

Make sure you have [Docker desktop](https://www.docker.com/products/docker-desktop) or [Docker](https://www.docker.com/) installed.

Create a local copy of this repository and run

    % docker-compose build

This spins up Compose and builds a local development environment according to the specifications in [docker-compose.yml](https://github.com/magnitis/pokemon-search-engine/blob/master/docker-compose.yml). Keep in mind that this file contains settings for development, and not production.

After the containers have been built (this may take a few minutes), run

    % docker-compose up

This will boot up a local server for Flask (on port 5000) and React (on port 3000). Open [http://localhost:3000](http://localhost:3000) to view the search engine in the browser.

### How to run manually

#### Prerequisites

* Node.Js v16 installed -- <https://nodejs.org/en/blog/release/v16.3.0/>

* Python 3.9.x installed -- <https://installpython3.com>

* Python 3 PIP installed -- <https://pip.pypa.io/en/stable/installing>

#### Installation

    % git clone https://github.com/magnitis/pokemon-search-engine.git
    % cd pokemon-search-engine
    % pip install -r api/requirements.txt

### `yarn start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `yarn test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `yarn build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `yarn eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `yarn build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
