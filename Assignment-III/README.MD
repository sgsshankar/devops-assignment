Assignment III
===================

Assumptions
-------------

> - The complete application is packed as WAR file and deployed in Apache
> - The complete setup is to be migrated to AWS making it cloud enabled using AWS Tools and services replacing the existing ones
> - It requites some rewrite/replacement of modules to effectively make use of AWS
> - Source control is maintained to host all the files

Architecture
-------------

![Please look at Architecture.png](./Architecture.png?raw=true)

List of AWS Services
-------------

#### Elastic Beanstalk

It is used for hosting the application. It consists of EC2 instances with Apache server in an Autoscaling group with an Elastic Loadbalancer (ELB) that is packed into single stack that is easy to manage. Very useful for Monolithic applications.

####  RDS

Amazon RDS lets us provision Oracle Database in a cluster that is provisioned and managed by AWS. Scalable and has less DBA overhead for maintenance.

#### SQS

Amazon Simple Queue Service is the Queue service similar to Active MQ. Reliable, fast and easy to query.

#### Dynamo DB

Amazon's managed Document DB on the cloud. Dynamo DB offers scalable NoSQL document store similar to MongoDB that can hold and process humongous amount of data. 

> **Note:** Although Dynamo DB is similar to MongoDB, it lacks advanced capabilities like aggregation pipeline and Map-reduce that MongoDB offers. If MongoDB is essential, it can be deployed on EC2 with ELB and Autoscaling or Dockerized using EC2 Container Service

#### S3

AWS S3 can be used to store file objects like images, files, etc so that it can be accessed by all of the running instances making it easy for the app to remain stateless

#### Route53

Route53 is used as the DNS service to point the application domain (example.com) to the ELB URL of the Elastic Beanstalk (*.elasticbeanstalk.com)

#### Code Build

Code Build is used to build the source code into packed WAR file along with necessary dependencies using Maven. It is linked with the source control system (github, bitbucket, gitlabs, AWS Code Commit, etc)

#### Code Deploy

AWS Code Deploy can be used to deploy the packed application to multiple nodes in the Elastic Beanstalk. It is used for Blue-Green Deployment

