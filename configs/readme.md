## File structure

docker-compose-provider.yaml :</br>
    Instantiates the configuration of docker containers on provider connector like ports, networks etc. </br>
    This is the file that needs to be executed to run the provider connector. To run the provider connector execute the command, docker-compose -f docker-compose-provider.yaml up</br>

docker-compose-consumer.yaml : </br> 
    Instantiates the configuration of docker containers on consumer connector like ports, networks etc. </br>
    This is the file that needs to be executed to run the consumer connector. To run the provider connector execute the command, docker-compose -f docker-compose-consumer.yaml up</br>

example-provider-routes.xml :</br>
    Configures data routing at the provider connector using [CAMEL](https://camel.apache.org/).

example-consumer-routes.xml :</br>
    Configures data routing at the consumer connector using [CAMEL](https://camel.apache.org/).
