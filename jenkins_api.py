"""
module :- pip install jenkinsapi
use :- Used to directly interact with the jenkins from our local system using python script.
"""
import sys
from jenkinsapi.jenkins import Jenkins

JENKINS_URL = "http://localhost:8080"
JENKINS_USER = "dhruv_antala1"
JENKINS_PASS = "Dhruv.antala##1"

def get_all_jobs(jenkins_obj):
    """
    This function will give the available jobs name from the localhost:8080
    :param jenkins_obj:
    :return:
    """
    jobs = jenkins_obj.get_jobs()
    job_list = [job[0] for job in jobs]
    print("List of available jobs:")
    print("-------------------------")
    for job in job_list:
        print(job)
    print()

def change_job_name(jenkins_obj, job_name, job_new_name):
    """
    This function will perform rename operation for the given job_name and convert it to the new job name.
    :param jenkins_obj:
    :param job_name:
    :param job_new_name:
    :return:
    """
    jenkins_obj.rename_job(job_name, job_new_name)
    print(f"Name changed from {job_name} to {job_new_name}")
    print()

def get_no_builds(jenkins_obj):
    """
    This function will print the number of builds that we did for the particular job.
    :param jenkins_obj:
    :return:
    """
    print("=================================================")
    job = jenkins_obj.get_job("Demo")
    job_builds = list(job.get_build_ids())
    no_builds = len(job_builds)
    print(f"\t\tNumber of available builds = {no_builds}")
    print("=================================================")
    print()

def get_last_build_details(jenkins_obj:Jenkins, job_name):
    """
    This function will print the data about the last build of the job.
    :param jenkins_obj:
    :return:
    """
    print("=============================================================================")
    job = jenkins_obj.get_job(job_name)
    job_last_build = job.get_last_build()
    print(job_last_build.get_timestamp().strftime('%d-%m-%Y %H:%M:%S'), job_last_build.get_build_url(), 'build no:-', job_last_build.buildno)
    print("=============================================================================")
    print()

try:
    jenkins = Jenkins(JENKINS_URL, JENKINS_USER, JENKINS_PASS)

    get_all_jobs(jenkins)
    get_no_builds(jenkins)

    # To change the name of the job from old_name to new_name.
    # change_job_name(jenkins, "Run_Serial_Simulator", "Run_Serial_Simulator")

    job_name = sys.argv[1]
    get_all_jobs(jenkins)
    get_last_build_details(jenkins, job_name)
except ConnectionError as e:
    print(f"Error :- {e}")
