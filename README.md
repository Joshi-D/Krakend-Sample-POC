A sample boiler plate to use krakend for various purposes.

Each folder have a separate krakend json file for performing different things.


Below is the command to run krakend
krakend run -c <krakend file name>.json
1. Basic 
This folder contains two flask microservices running on different ports; 5001 and 5002 ports respectively. The services are services by krakend on port 8080. 

2. Extra configs
Apart from hosting urls of different microservices on the same port, krakend also provides extra configurations which can be used to change the request response on the gateway level itself.
For ex: The user_service_formatted_response.py file has the key 'email_address' in the response. But, the final API response contains the key 'email' because it is configured on the gateway level by krakend.

3. Token
This folder depicts the functionality of generating the JWT token by krakend based on the jwk.json file present in the token folder. The url login will generate the JWT token and return it in response.