# Farmstack example implementation

<img src="workspace-architect.png"  height="250">

## Description
This project is a reference implementation of farmstack. There is one provider and one consumer, both running a FarmStack p2p connector. The connectors mutually authenticate and encrypt data through the SSL certificates provided to them from a simulated certificate authority. 

<!-- Add UC readme -->

The code provided here lets run both the connectors on same machine. The section below gives description of how to run the connectors as it is and how to separarte them on distirbuted instances of data provider and consumer.

### Folder structure

Config/ 
 - Includes the configuration related files: 
   - Docker configuration for provider and consumer connectors (yaml files) 
   - Data routing configurations of provider and consumer (xml files)        
</br>

Src/  
 - Includes the demo nodejs application code 
</br>

Cert stores/
 - Includes the certificate files issued by certificate authority


### To run connectors on single machine

1. To run provider node </br>
        change directory to IDSA-FS-DEMO/configs
        run $docker-compose -f docker-compose-provider.yaml up
        </br>

2. To run the consumer node </br>
        Change directory to IDSA-FS-DEMO/configs
        run $docker-compose -f docker-compose-consumer.yaml up
        </br>


 ### To run connectors separately on provider and consumer
 
  #### Add following lines in the respective files
   
   a. In the directory Configs/ add in the file docker-compose-provider.yaml following line </br>
        extra_hosts:
            - "consumer-core:your-consumer-machine-ip"
            
   b. In the directory Configs/ add in the file docker-compose-consumer.yaml following line </br>
        extra_hosts:
            - "provider-core:your-provider-machine-ip"
        

