sudo apt-get -y update
sudo apt-get -y install python3.4-dev python-virtualenv git libevent-dev

# Import app
mkdir /var/www
mkdir /var/www/nasanomics

/bin/bash -c "rsync -av \
    --exclude='/vagrant/nasanomics/vps/packer' \
    --exclude='/vagrant/nasanomics/vps/vagrant' \
    /vagrant/nasanomics/ /var/www/nasanomics"

# Setup dependencies
cd /var/www/nasanomics
make venv
source /var/www/nasanomics/venv/bin/activate
make install

# UWSGI Setup
sudo apt-get -y install uwsgi uwsgi-plugin-python
mkdir /var/www/run
chown www-data:www-data /var/www/run
touch /var/log/uwsgi/emperor.log
chown www-data:www-data /var/log/uwsgi/emperor.log
touch /var/log/uwsgi/app/nasanomics.log
chown www-data:www-data /var/log/uwsgi/app/nasanomics.log
cp /vagrant/nasanomics/vps/vagrant/uwsgi.conf /etc/init
cp /vagrant/nasanomics/vps/vagrant/uwsgi_config.ini /etc/uwsgi/apps-available/
ln -s /etc/uwsgi/apps-available/uwsgi_config.ini /etc/uwsgi/apps-enabled

# NGINX Setup
sudo apt-get -y install nginx
rm /etc/nginx/sites-enabled/default
cp /vagrant/nginx_config /etc/nginx/sites-available/
ln -s /etc/nginx/sites-available/nginx_config /etc/nginx/sites-enabled

# Start UWSGI and NGINX
service nginx restart
service uwsgi restart