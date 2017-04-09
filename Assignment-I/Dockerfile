######################################################################
# Source: Official CentOS repository CentOS6
# Install: Apache Tomcat 7, MongoDB, Python 2.7
# Port: 27017, 8080
# External: 7080
######################################################################
FROM centos:centos6 
MAINTAINER sgsshankar

#######################################################################
# Prerequisite Update and Utilities.
#######################################################################

RUN  yum -y update  && \
     yum -y install wget && \
     yum -y install tar  && \
     yum -y install epel-release && \
     yum clean all                      

#######################################################################
# Environment Variables
#######################################################################

ENV JAVA_HOME /opt/java 
ENV CATALINA_HOME /opt/tomcat 
ENV PATH $PATH:/usr/bin:$JAVA_HOME/bin:$CATALINA_HOME/bin:$CATALINA_HOME/scripts

ENV JAVA_VERSION 7u79 
ENV JAVA_BUILD 7u79-b15
ENV TOMCAT_MAJOR 7 
ENV TOMCAT_VERSION 7.0.77

#######################################################################
# Software Installation
#######################################################################

# Python 2.7
RUN  yum -y install centos-release-scl  && \
     yum -y install python27  \
     python27-pip  \ 
     python27-virtualenv                

# MongoDB 
RUN  yum -y install mongodb-server  && \
     mkdir -p /data/db               

# Java 7
RUN wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" \
    http://download.oracle.com/otn-pub/java/jdk/${JAVA_BUILD}/jdk-${JAVA_VERSION}-linux-x64.tar.gz && \
    tar -xvf jdk-${JAVA_VERSION}-linux-x64.tar.gz && \
    rm jdk*.tar.gz && \
    mv jdk* ${JAVA_HOME}

# Tomcat 7
RUN wget http://ftp.riken.jp/net/apache/tomcat/tomcat-${TOMCAT_MAJOR}/v${TOMCAT_VERSION}/bin/apache-tomcat-${TOMCAT_VERSION}.tar.gz && \
    tar -xvf apache-tomcat-${TOMCAT_VERSION}.tar.gz && \
    rm apache-tomcat*.tar.gz && \
    mv apache-tomcat* ${CATALINA_HOME} &&\
    chmod +x ${CATALINA_HOME}/bin/*sh

#######################################################################
# Post Installation Configuration
#######################################################################

ADD create_admin_user.sh $CATALINA_HOME/scripts/create_admin_user.sh
ADD tomcat.sh $CATALINA_HOME/scripts/tomcat.sh
RUN chmod +x $CATALINA_HOME/scripts/*.sh
RUN groupadd -r tomcat && \
    useradd -g tomcat -d ${CATALINA_HOME} -s /sbin/nologin  -c "Tomcat user" tomcat && \
    chown -R tomcat:tomcat ${CATALINA_HOME}

#######################################################################
# Port Mapping
#######################################################################

EXPOSE 27017
EXPOSE 8080

#######################################################################
# Application Execution
#######################################################################

CMD ["/usr/bin/mongod"]
WORKDIR /opt/tomcat
USER tomcat 
CMD ["tomcat.sh"]