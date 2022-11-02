#!/usr/bin/python3.6
import urllib3
import json
http = urllib3.PoolManager()
def lambda_handler(event, context):
    url = "https://hooks.slack.com/services/xxxxx"
    
    json_data = event['Records'][0]['Sns']['Message']
    # json_object = json.dumps(json_data)
    b = json.loads(json_data)
    print(json_data)
    # print(b['detail']['state'])
    
    # NotifyAgentDisconnectedForMgn
    
    eventName = b['detail']['eventName']
    
    
    if eventName == "RegisterAgentForMgn" :
        msg = {
        "channel": "#cloud_watch",
        "username": "U0373TEQLNN",
        "text": ":sparkle: MGN Agent Register for Mgn : "+b['detail']['eventName']+"\n sourceIPAddress : "+b['detail']['sourceIPAddress']+"\n User : "+b['detail']['userIdentity']['userName'],
        "icon_emoji": ""
        } 
    elif eventName == "StartCutover" : 
        msg = {
        "channel": "#cloud_watch",
        "username": "U0373TEQLNN",
        "text": ":large_orange_circle: MGN_status - starts StartCutover, Please Wait..  : " + b['detail']['eventName'] ,
        "icon_emoji": ""
        }
    elif eventName == "StartTest":
        msg = {
        "channel": "#cloud_watch",
        "username": "U0373TEQLNN",
        "text": ":large_orange_circle: MGN_status - Launching test instance..please wait..  : "+b['detail']['eventName'],
        "icon_emoji": ""
        }   
    elif eventName == "FinalizeCutover" :
        msg = {
        "channel": "#cloud_watch",
        "username": "U0373TEQLNN",
        "text": ":recycle: Cutover completed and wating for MARK AS ARCHIVIED : "+b['detail']['eventName'],
        "icon_emoji": ""
        }
    elif eventName == "MarkAsArchived" :
        msg = {
        "channel": "#cloud_watch",
        "username": "U0373TEQLNN",
        "text": ":white_check_mark: Congratulation !! MGN Process has Completed : "+b['detail']['eventName'],
        "icon_emoji": ""
        } 
    elif eventName == "DisconnectFromService" :
        msg = {
        "channel": "#cloud_watch",
        "username": "U0373TEQLNN",
        "text": ":red_circle: ALERT SourceServer has been disconnected! : "+b['detail']['eventName'],
        "icon_emoji": ""
        } 
    elif eventName == "ChangeServerLifeCycleState" :
        msg = {
        "channel": "#cloud_watch",
        "username": "U0373TEQLNN",
        "text": ":recycle: MGN ChangeServer LifeCycle State changed: Launch test instance | Launch Cutover instance: "+b['detail']['requestParameters']['lifeCycle']['state'],
        "icon_emoji": ""
        }
    elif eventName == "UpdateAgentConversionInfoForMgn" :
        msg = {
        "channel": "#cloud_watch",
        "username": "U0373TEQLNN",
        "text": ":hourglass: Login to the Console and keep on eye \n Data replication status \n Lifecycle Launch status complete \n Finalize cutover \n EventName : "+b['detail']['eventName'],
        # "text": "test3"+json_data,
        "icon_emoji": ""
        }     
    elif eventName == "CreateSnapshot" :
        msg = {
        "channel": "#cloud_watch",
        "username": "U0373TEQLNN",
        "text": ":large_orange_circle: MGN_status - Snapshot created successfully, Proceed to Launch Instance : \n Event :"+b['detail']['eventName']+ "\n sourceIPAddress: " +b['detail']['sourceIPAddress'],
        "icon_emoji": ""
        } 
    
   
    elif eventName == "NotifyMigrationTaskState" and b['detail']['requestParameters']['task']['statusDetail'] == "Initial Sync":
        msg = {
        "channel": "#cloud_watch",
        "username": "U0373TEQLNN",
        "text": ":large_orange_circle: MGN_status : \n Event :"+b['detail']['eventName']+ "\n statusDetail: " +b['detail']['requestParameters']['task']['statusDetail']+ "\n Status: " +b['detail']['requestParameters']['task']['status'],
        "icon_emoji": ""
        } 
    elif eventName == "NotifyMigrationTaskState" and b['detail']['requestParameters']['task']['statusDetail'] == "Continuous Data Replication":
        # statusDetail = b['detail']['requestParameters']['task']['statusDetail']
        # if statusDetail == "Continuous Data Replication":
        msg = {
        "channel": "#cloud_watch",
        "username": "U0373TEQLNN",
        "text": ":large_green_circle: MGN_status : READY FOR NEXT ACTION!",
        "icon_emoji": ""
        } 
    elif eventName == "RunInstances" :
        msg = {
        "channel": "#cloud_watch",
        "username": "U0373TEQLNN",
        "text": ":large_orange_circle: MGN_status - Instance starts, Please wait..  \n eventName : "+b['detail']['eventName']+ "\n Instance Name : " +b['detail']['responseElements']['instancesSet']['items'][0]['tagSet']['items'][0]['value'],
        "icon_emoji": ""
        } 
    elif eventName == "StartInstances":
        msg = {
        "channel": "#cloud_watch",
        "username": "U0373TEQLNN",
        "text": ":large_green_circle: MGN_status - Destination Instance created successfully, Complete testing and mark as 'Ready for cutover | Finalize cutover : \n eventName : "+b['detail']['eventName']+ "\n sourceIPAddress : " +b['detail']['sourceIPAddress'],
        "icon_emoji": ""
        } 
    
    elif eventName == "DetachVolume":
        msg = {
        "channel": "#cloud_watch",
        "username": "U0373TEQLNN",
        "text": ":large_orange_circle: MGN_status - Starting cutover the Replication server, Please wait..  \n eventName : "+b['detail']['eventName']+ "\n sourceIPAddress : " +b['detail']['sourceIPAddress'],
        "icon_emoji": ""
        } 
    else:
        msg = {
        "channel": "#cloud_watch",
        "username": "U0373TEQLNN",
        # "text": "MGN State : "+b['detail']['eventName'],
        "icon_emoji": ""
        }
    
    encoded_msg = json.dumps(msg).encode('utf-8')
    resp = http.request('POST',url, body=encoded_msg)
    print({
            
        "message": b['detail']['eventName'],
        "status_code": resp.status, 
        "response": resp.data
    })
        
    print("------ALARM-------------")
