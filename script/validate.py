from result_output import *
import sys
import json
import importlib.util
import urllib.request
from google.oauth2 import service_account
from googleapiclient import discovery
from pprint import pprint
from google.cloud import logging

class Activity():

    def testcase_check_Migrate_SourceName(self,test_object,credentials,project_id):
        testcase_description="Check AWS Source Name"
        expected_result="liftandshift"
        list_of_entries=[]
        i=0
        
        try:
            is_present = False
            actual = 'Source name is not '+ expected_result
            logger_name = "vmmigration.googleapis.com%2Fsource"
            logging_client = logging.Client(credentials=credentials)

            try:
                logger = logging_client.logger(logger_name)

                from google.cloud.logging import DESCENDING
                for entry in logger.list_entries(order_by=DESCENDING):
                    i=i+1
                    if i>=100:
                        break
                    if ((entry.resource.labels["source"] == expected_result) and (entry[3] == "ERROR")):
                        is_present=False
                        break
                    if ((entry.resource.labels["source"] == expected_result) and (entry[3] == "INFO")):
                        is_present=True
                        actual=expected_result
                        break
            except Exception as e:
                is_present = False

            test_object.update_pre_result(testcase_description,expected_result)
            if is_present==True:
                test_object.update_result(1,expected_result,actual,"Congrats! You have done it right!"," ") 
            else:
                return test_object.update_result(0,expected_result,actual,"Check AWS Source Name","https://cloud.google.com/migrate/virtual-machines/docs/5.0/how-to/create-an-aws-source")   

        except Exception as e:    
            test_object.update_result(-1,expected_result,"Internal Server error","Please check with Admin","")
            test_object.eval_message["testcase_check_Migrate_SourceName"]=str(e)                

    def testcase_check_Migrate_TargetRegion(self,test_object,credentials,project_id):
        testcase_description="Check GCP Target Region"
        expected_result="asia-south1"
        list_of_entries=[]
        i=0
        
        try:
            is_present = False
            actual = 'GCP Region is not '+ expected_result
            logger_name = "vmmigration.googleapis.com%2Fsource"
            logging_client = logging.Client(credentials=credentials)

            try:
                logger = logging_client.logger(logger_name)

                from google.cloud.logging import DESCENDING
                for entry in logger.list_entries(order_by=DESCENDING):
                    i=i+1
                    if i>=100:
                        break
                    if ((entry.resource.labels["source"] == "liftandshift") and (entry[3] == "ERROR")):
                        is_present=False
                        break
                    if ((entry.resource.labels["source"] == "liftandshift") and (entry[3] == "INFO") and (entry.resource.labels["location"] == expected_result)):
                        is_present=True
                        actual=expected_result
                        break
            except Exception as e:
                is_present = False

            test_object.update_pre_result(testcase_description,expected_result)
            if is_present==True:
                test_object.update_result(1,expected_result,actual,"Congrats! You have done it right!"," ") 
            else:
                return test_object.update_result(0,expected_result,actual,"Check AWS Source Name","https://cloud.google.com/migrate/virtual-machines/docs/5.0/how-to/create-an-aws-source")   

        except Exception as e:    
            test_object.update_result(-1,expected_result,"Internal Server error","Please check with Admin","")
            test_object.eval_message["testcase_check_Migrate_SourceName"]=str(e)                

            
def start_tests(credentials, project_id, args):

    if "result_output" not in sys.modules:
        importlib.import_module("result_output")
    else:
        importlib.reload(sys.modules[ "result_output"])
    
    test_object=ResultOutput(args,Activity)
    challenge_test=Activity()
    challenge_test.testcase_check_Migrate_SourceName(test_object,credentials,project_id)
    challenge_test.testcase_check_Migrate_TargetRegion(test_object,credentials,project_id)

    json.dumps(test_object.result_final(),indent=4)
    return test_object.result_final()

