# Docker ML Project

This is a simple project of a dockerised application, that contains Frontend/Backend database and inference servers – all run via docker-compose. It's a souly practitionary project, to understand how to create dockerised apps.

It's a website service, that runs inference on passed images in order to detect if a person (or people) and heads that are present on the picture. Afterwards if detector model retuns bounding boxes, of classes, they are drawn on passed image and displayed on apps website. Then passed image is saved locally, and it's name as a key is passed alongside with bounding boxes - as a value - to the redis database.


This is a image detection service, that allows user to quickly analyze images for the presence of people and heads.  [Deepakcrk's](https://github.com/deepakcrk/yolov5-crowdhuman) model runs inference on passed image and returns bounding boxes for any detected individuals or heads. These bounding boxes will be drawn on the image and displayed on app's website. The processed image will also be saved locally. its name and bounding box data will be stored in a Redis database for easy retrieval later on
## Getting Started

In order to get started you need to have couple of things installed on your machine.

### Prerequisites

- Docker
- Docker Compose
- Git
- ML model [LINK](https://drive.google.com/file/d/1gglIwqxaH2iTvy6lZlXuAcMpd_U0GCUb/view)

### Installing

1. Clone the repository to your local machine and enter project's directory:

```console
git clone git@github.com:Bartoliinii/docker_ml_project.git
cd docker_ml_project
```

2. Put ML model into ML/recognition_routers/utils/ directory:
```console
mv /path/to/ML/Model.pt ML/recognition_routers/utils/
```

3. Build docker image:
```console
docker-compose build
```

### Running and avalible commands
- To run the application enter this command:
```console
docker-compose up
```

- While the docker containers are running, you may enter command:
```console
docker-compose front_back_end python get_data.py
```
It will retrive all data from the database, write into dump.json in FrontEnd folder.

### Shuting down
To shut down this application simply use this command:
```console
docker-compose stop
```
Or simply press Ctrl-C to stop the docker-compose.


@deepakcrk: Thanks for releasing your model to the public.

