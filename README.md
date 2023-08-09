# Docker ML Project

This is an image detection service, that allows users to quickly analyze images for the presence of humans.  [Deepakcrk's](https://github.com/deepakcrk/yolov5-crowdhuman) model runs inference on passed images and returns bounding boxes for any detected individuals or their heads. These bounding boxes will be drawn on the image and displayed on the app's website. The processed image will also be saved locally. Its name and bounding box data will be stored in a Redis database for later retrieval. 
## Getting Started

In order to get started you need to have a couple of things installed on your machine.

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

3. Build a docker image:
```console
docker-compose build
```

### Running and available commands
- To run the application enter this command:
```console
docker-compose up
```
The app will be available on [0.0.0.0:8001](http://0.0.0.0:8001)

- While the docker containers are running, you may enter the command:
```console
docker-compose exec web_app python get_data.py
```
It will retrieve all data from the database, and write it into dump.json in the FrontEnd folder.

### Shutting down
To shut down this application simply use this command:
```console
docker-compose stop
```
Or simply press Ctrl-C to stop the docker-compose.


@deepakcrk: Thanks for releasing your model to the public.

