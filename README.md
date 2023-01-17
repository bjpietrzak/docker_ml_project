# Docker ML Project

This is a simple project of a dockerised application, that contains Frontend/Backend database and inference servers – all run via docker-compose. It's a souly practitionary project, to help me understand how to create dockerised apps.

It's a website service, that runs inference on passed images in order to detect if a person (or people) are present on a picture. That

## Getting Started

In order to get started you need to have couple of things installed on your machine.

### Prerequisites

- Docker
- Docker Compose
- Git

### Installing

1. Clone the repository to your local machine:

```console
git clone git@github.com:Bartoliinii/docker_ml_project.git
```

2. Build docker image:
```console
docker-compose build
```

3. Run the application:
```console
docker-compose up
```
