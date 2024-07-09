## Flask over SaladCloud

#### Deploy the image on SaladCloud
image Source: saladtechnologies/misc:0.0.2-flask2 

Replica Count: any 

Container Gateway: Enable, 8000

#### Use the generated Access Domain Name to access the applicaiton

https://XXXXXXX-xxxxx-ufw34ufoq2rvktjj.salad.cloud

## Gradio over SaladCloud 

We don't recommend deploying UI-related apps on interruptible nodes, but test is fine. You can create one container group for each user and the replica count can only be 1.

#### Deploy the image on SaladCloud
image Source: saladtechnologies/misc:0.0.1-gradio

Replica Count: can only be 1

Container Gateway: Enable, 5000

#### Use the generated Access Domain Name to access the applicaiton

https://XXXXXXX-xxxxx-ufw34ufoq2rvktjj.salad.cloud


