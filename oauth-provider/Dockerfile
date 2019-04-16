FROM tonisormisson/dev-lemp

ADD ./app/ /var/www/html/

RUN cd /var/www/html/ && \
    service mysql start && \
    mysql -u root -proot < db.sql && \
    git clone https://github.com/bshaffer/oauth2-server-php.git -b master

EXPOSE 80
