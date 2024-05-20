to remove image : 
docker image rm <Image ID>

to create a docker image: 
    docker build -t 'aliakbari1997/'+<image-name> <address>
    example : docker build -t ticket-img .

to run a docker image :
    docker run -d -p exposed port:port <image-name>
    example : docker run -d -p 8000:8000 ticket-img


to push to docker hub : 
    docker push 'aliakbari1997'/+<image-name>:<tag>