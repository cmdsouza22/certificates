# Code Test for Apple 
WorkFlow = main.yaml 
Python Program = get_ssl_certs.py

Part 1 complete - Program  scans given list of websites, captures SSL Server Certificate security details, sorts Certificates' data as per their validity, and export .csv file.

Part-2 Not completed due to issues / errors :Create a CICD job to run the program in a container when the list of websites stored in git changes.
In Progress:
Docker image creation
Github to DockerHub connection setup 
Github workflow created to run when code changes 


Issues:
1.) Building image :
docker build -t  ssl_certs_check_image .
Sending build context to Docker daemon   7.68kB
Step 1/6 : FROM python:3.9
Get https://registry-1.docker.io/v2/: net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers)
cdsouza2@CeeCee2 python-docker % cat /etc/resolv.conf

2.)  Github Action workflow error in main.yml 


