# Docker ML Project

This is a image detection service, that allows user to quickly analyze images for the presence of people and heads.  [Deepakcrk's](https://github.com/deepakcrk/yolov5-crowdhuman) model runs inference on passed image and returns bounding boxes for any detected individuals or heads. These bounding boxes will be drawn on the image and displayed on app's website. The processed image will also be saved locally. Its name and bounding box data will be stored in a Redis database for later retrieval. 
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

