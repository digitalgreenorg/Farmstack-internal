The file `demo-app.tar` contains the docker image for the UC demo.

The file was built as follows:
```
docker build ./example-server -t demo-app -q
docker save demo-app > demo-app.tar
```
Note the hash output of the first command, it is the local hash of the image
required for the provider XML!

Import the docker image as follows: 
```
docker load -i demo-app.tar
docker tag <image hash> demo-app
```