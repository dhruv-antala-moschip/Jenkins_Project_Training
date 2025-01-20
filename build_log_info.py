"""
module :- pip install jenkinsapi
use :- Used to directly interact with the jenkins from our local system using python script.
"""
import argparse
import sys
from jenkinsapi.jenkins import Jenkins
import logging

JENKINS_URL = "http://localhost:8080"
JENKINS_USER = "dhruv_antala1"
JENKINS_PASS = "Dhruv.antala##1"

logger=logging.getLogger("log_info")
logger.setLevel(logging.INFO)

consoleHandler=logging.StreamHandler()
consoleformater=logging.Formatter('%(asctime)s- %(levelname)s-%(message)s')
consoleHandler.setFormatter(consoleformater)
logger.addHandler(consoleHandler)
logger.info("Hello")

def get_all_jobs(jenkins_obj):
    """
    This function will give the available jobs name from the localhost:8080
    :param jenkins_obj:
    :return:
    """
    jobs = jenkins_obj.get_jobs()
    job_list = [job[0] for job in jobs]
    logger.info("List of available jobs:")
    logger.info("-------------------------")
    for job in job_list:
        logger.info(job)


def change_job_name(jenkins_obj, job_name, job_new_name):
    """
    This function will perform rename operation for the given job_name and convert it to the new job name.
    :param jenkins_obj:
    :param job_name:
    :param job_new_name:
    :return:
    """
    jenkins_obj.rename_job(job_name, job_new_name)
    logger.info(f"Name changed from {job_name} to {job_new_name}")
    logger.info()

def get_no_builds(jenkins_obj):
    """
    This function will print the number of builds that we did for the particular job.
    :param jenkins_obj:
    :return:
    """
    logger.info("=================================================")
    job = jenkins_obj.get_job("Demo")
    job_builds = list(job.get_build_ids())
    no_builds = len(job_builds)
    logger.info(f"\t\tNumber of available builds = {no_builds}")
    logger.info("=================================================")


def get_last_build_details(jenkins_obj:Jenkins, job_name):
    """
    This function will print the data about the last build of the job.
    :param jenkins_obj:
    :return:
    """
    logger.info("=============================================================================")
    job = jenkins_obj.get_job(job_name)
    job_last_build = job.get_last_build()
    logger.info(job_last_build.get_timestamp().strftime('%d-%m-%Y %H:%M:%S'), job_last_build.get_build_url(), 'build no:-', job_last_build.buildno)
    logger.info("=============================================================================")


try:
    jenkins = Jenkins(JENKINS_URL, JENKINS_USER, JENKINS_PASS)

    get_all_jobs(jenkins)
    get_no_builds(jenkins)

    # To change the name of the job from old_name to new_name.
    # change_job_name(jenkins, "Run_Serial_Simulator", "Run_Serial_Simulator")
    parser= argparse.ArgumentParser()
    parser.add_argument('--job',type=str,required=True)
    args = parser.parse_args()
    logger.info(args.job)
    # get_all_jobs(jenkins)
    # get_last_build_details(jenkins, job_name)
except ConnectionError as e:
    print(f"Error :- {e}")
