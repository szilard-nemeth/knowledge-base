## Docker cleanup

### Docker free space
```
docker system df
```

### Remove all stopped containers
```
docker container prune
```


### Remove all all unused containers, networks, images (both dangling and unreferenced), and optionally, volumes, in one command.
```
docker system prune
```
or 
```
docker system prune --force
```

### Remove all dangling images
https://docs.docker.com/reference/cli/docker/image/prune/

```
docker image prune
```

### Remove first N images
```
docker images | awk '{print $3}' | tail -n 80 | xargs docker rmi
```

### Remove images by grepping name
```
docker images | grep \"DEX-9645\|DEX-7712\|DEX-7051\" | awk '{print \$3}' | xargs docker rmi
docker images | grep 1.19.0-dev | awk '{print \$3}' | xargs docker rmi
docker images | grep \"DEX-\" | grep -v \"DEX-7325\" | awk '{print \$3}' | xargs docker rmi -f
docker images | grep \"dex\" | awk '{print \$3}' | xargs docker rmi -f
docker images | grep \"thunderhead\" | awk '{print \$3}' | xargs docker rmi -f
```

### Remove images older than specific date
https://forums.docker.com/t/simple-script-needed-to-delete-all-docker-images-over-4-weeks-old/28558/6
More time-based commands: https://dirask.com/posts/Docker-remove-images-older-than-some-specific-period-of-time-DnzWbD

```
docker image prune --all --filter \"until=504h\"
```

### Remove dangling images
```
docker rmi \$(docker images --filter \"dangling=true\" -q --no-trunc)
```
