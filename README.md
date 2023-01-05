# anonmessages
A pyhton discord slash command bot to send anon messages to users by their ID

# Instalation 
 Clone this repository
 
 ```
 git clone
 ```
 
 Edit the .env.example, put your token and rename ir to .env
 
 build the docker image
 
 ```
 docker build . -t the name you want
 ```
 run the docker image
 
 ```
 docker run -d the name you set
 
 ```
 And you have it running 
 
 # Usage
 
 Write the bot via private message ``/enviar <the destiantion user ID> <the message you want to send him>``
  
 NOTE THAT THE BOT WONT BE ABLE TO WRITE MESSAGES TO PEOPLE OUTSIDE THE SERVER HE IS AND PEOPLE WHO HAVE SERVER PRIVATE MDS BLOCKED
