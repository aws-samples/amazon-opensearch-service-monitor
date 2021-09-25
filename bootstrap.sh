#!/bin/bash

# create the virtual environment
python3 -m venv .env
# Install into the virtual environment
source .env/bin/activate
# download requirements
.env/bin/python -m pip install -r requirements.txt --use-deprecated=legacy-resolver
# Load dependency for lambda functions
.env/bin/python -m pip install --target monitoring-py/ -r monitoring-py/requirements.txt

# create the key pair
region_default="us-west-2"
echo -e
read -p "Please enter your region to bootstrap the env [$region_default]: " region
region="${region:-$region_default}"

aws ec2 create-key-pair --key-name amazon_opensearch_monitoring --query 'KeyMaterial' --output text > amazon_opensearch_monitoring.pem --region $region
# update key_pair permissions
chmod 400 amazon_opensearch_monitoring.pem
# move key_pair to .ssh
mv -f amazon_opensearch_monitoring.pem $HOME/.ssh/amazon_opensearch_monitoring.pem
# start the ssh agent
eval `ssh-agent -s`
# add your key to keychain
ssh-add -k ~/.ssh/amazon_opensearch_monitoring.pem 

# Add e-mail for the notification
email_default="user@example.com"
echo -e
read -p "Please enter an e-mail for alert [$email_default]: " email
email="${email:-$email_default}"
sed -i -e 's/user@example.com/'$email'/g' monitoring_cdk/monitoring_cdk_stack.py

