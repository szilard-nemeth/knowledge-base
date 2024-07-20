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


## DOCKER TUTORIALS
https://stackify.com/docker-build-a-beginners-guide-to-building-docker-images/