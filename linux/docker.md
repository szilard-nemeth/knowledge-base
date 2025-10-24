# Docker

1. print environment variables of container

```docker exec <container> bash -c 'echo "$ENV_VAR"'```

2. Peek into container
```docker run --name container-name -it image-name /bin/bash```


## How to add containers to same network in Docker
Details: https://stackoverflow.com/questions/50721424/how-to-add-containers-to-same-network-in-docker

First, define your user-defined bridge network:
```
docker network create your-network-name
```

Then, connect your containers to the network that you just created:
```
docker network connect your-network-name container-name
```

Or connect with the run command:
```
docker run --network=your-network-name your-image
```

Now, containers in the same network your-network-name can talk to each others via container name.


## Run a Docker image as a container
https://stackoverflow.com/questions/18497688/run-a-docker-image-as-a-container
Reference: https://docs.docker.com/engine/reference/run/

With a name (let's use Ubuntu):
```
$ docker run -i -t ubuntu:12.04 /bin/bash
```

Without a name, just using the ID: 
```
$ docker run -i -t 8dbd9e392a96 /bin/bash

```

### Overriding entrypoint
https://www.warp.dev/terminus/docker-run-bash

```
$ docker run --entrypoint /bin/bash -it <image>
```

### Run docker image and execute some commands (oneliner)
DETAILS: https://stackoverflow.com/questions/56752548/docker-run-command-to-achieve-few-steps-with-a-single-line-of-command

```
docker run --rm -dit --name test -v /root/tools:/var/local alpine ash -c "date"
```

Keep it running
```
docker run --rm -it --name test alpine ash -c "date; tail -f /dev/null"
```

## DOCKER TUTORIALS
https://stackify.com/docker-build-a-beginners-guide-to-building-docker-images/

## Stop and remove all containers
https://stackoverflow.com/questions/45357771/stop-and-remove-all-docker-containers
https://stackoverflow.com/a/51316176

```
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```

# Knowledge
What are the appropriate names for the parts of a docker image's name? https://stackoverflow.com/questions/55277250/what-are-the-appropriate-names-for-the-parts-of-a-docker-images-name

FULL: `my-registry/my-image:0.1.0`

`my-registry` is the registry
`my-registry/my-image` is the (image) name
`0.1.0` is the tag (name)