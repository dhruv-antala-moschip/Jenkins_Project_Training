import argparse
from jenkinsapi.jenkins import Jenkins
import logging
import xml.etree.ElementTree as Tree
from xml.dom import minidom

JENKINS_URL = "http://localhost:8080"
JENKINS_USER = "dhruv_antala1"
JENKINS_PASS = "Dhruv.antala##1"

logger=logging.getLogger("log_info")
logger.setLevel(logging.INFO)
logging.basicConfig(filename='logreport.log', filemode='w')

consoleHandler=logging.StreamHandler()
consoleformater=logging.Formatter('%(asctime)s- %(levelname)s-%(message)s')
consoleHandler.setFormatter(consoleformater)
logger.addHandler(consoleHandler)
logger.info("Hello")


def get_all_jobs(jenkins_obj):
    jobs = jenkins_obj.get_jobs()
    job_list = [job[0] for job in jobs]
    logger.info("List of available jobs:")
    logger.info("-------------------------")
    for job in job_list:
        logger.info(job)


def change_job_name(jenkins_obj, job_name, job_new_name):
    jenkins_obj.rename_job(job_name, job_new_name)
    logger.info(f"Name changed from {job_name} to {job_new_name}")
    logger.info("\n")


def get_no_builds(jenkins_obj):
    job = jenkins_obj.get_job("Demo")
    job_builds = list(job.get_build_ids())
    no_builds = len(job_builds)
    logger.info(f"Number of available builds = {no_builds}")


def get_last_build_details(jenkins_obj:Jenkins, job_name):
    job = jenkins_obj.get_job(job_name)
    job_last_build = job.get_last_build()
    logger.info(
        f"{job_last_build.get_timestamp().strftime('%d-%m-%Y %H:%M:%S'), job_last_build.get_build_url(), 'build no:-',job_last_build.buildno}")


try:
    jenkins = Jenkins(JENKINS_URL, JENKINS_USER, JENKINS_PASS)
    get_all_jobs(jenkins)
    get_no_builds(jenkins)
    parser= argparse.ArgumentParser()
    parser.add_argument('--job',type=str,required=True)
    args = parser.parse_args()
    job_name=args.job
    logger.info(args.job)
    get_last_build_details(jenkins,job_name)
except ConnectionError as e:
    print(f"Error :- {e}")

# Build xml tree
root = Tree.Element("testsuites")
log_details = []

with open('logreport.log', 'r') as log_file:
    for index, line in enumerate(log_file):
        if index <= 10:
            log_details.append(f"{index}: {line.strip()}")

for data in range(10):
    testsuite = Tree.Element("testsuite", {
        "name": f"Suite-{data}",
        "tests": "0",
        "failures": "1",
        "errors": "0",
        "skipped": "0",
        "time": "0.2"
    })

    testcase = Tree.Element("testcase", {
        "name": log_details[data],
        "classname": f"Suite-{data}",
        "time": "0.123"
    })

    if data % 2 != 0:
        failure = Tree.Element("failure", {
            "message": f"Failed test{data}",
            "type": "AssertionError"
        })
        failure.text = f"more detail about failure-{data}."
        testcase.append(failure)
    elif data >= 6:
        skipped = Tree.Element("skipped", {
            "message": f"this test {data} was skipped by user"
        })
        testcase.append(skipped)
    testsuite.append(testcase)
    root.append(testsuite)

rough_string = Tree.tostring(root, 'utf-8')
parsed = minidom.parseString(rough_string)
pretty_xml = parsed.toprettyxml(indent="  ")
with open('report.xml', 'w') as file:
    file.write(pretty_xml)
