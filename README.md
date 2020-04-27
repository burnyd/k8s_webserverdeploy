# k8s_webserverdeploy
Simple test web server deployment with kubernetes 

This is a simple k8s deployment that will upon using will apply a kubernetes deployment exposing a webserver deployment, 3 pods and 1 service exposing port 32150.

For example

root@node3:/home/burnyd# curl http://10.1.1.221:32150/info

hello from webserver-deployment-59f97cf76-krfzc with operating system of Linux-4.15.0-96-generic-x86_64-with-Ubuntu-18.04-bionicroot
