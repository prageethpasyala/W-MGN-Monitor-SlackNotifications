![Alt text](mgn-alert.png?raw=true "Title")


1. Create a SNS topic  
2. Create EventBridge rule to trigger SNS for all cloudtrail events
3. Create the Lambda function and add SNS trigger 
4. Create a IAM User and get AccessID and SecretKey
5. Launch a EC2 instance in US-East-2 
6. Run the command to download mgn agent (Chnage region name to your destination region, eg eu-west-2)
   (https://docs.aws.amazon.com/mgn/latest/ug/linux-agent.html)
        wget -O ./aws-replication-installer-init.py https://aws-application-migration-service-eu-west-2.s3.eu-west-2.amazonaws.com/latest/linux/aws-replication-installer-init.py
        wget -O ./aws-replication-installer-init.py https://aws-application-migration-service-us-east-1.s3.us-east-1.amazonaws.com/latest/linux/aws-replication-installer-init.py

7. Once the Agent installer has successfully downloaded, copy and input the installer command into the command line on your source server in order to run the installation script.
        sudo python3 aws-replication-installer-init.py

8. Enter your destination region which you are planing to imgrate to.

9. Enter your Mgt-user details
Access id :         
Secret key : 

1.  Create the second Lambda function ( Error alert)
  
2.    Open your Slack app and see all notifications 





create a new channel on your slack account 
crete new webhook under 
create app and select the new chanel 
