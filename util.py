import requests
from time import sleep

def run_prog(lang, code, api="paiza"):
    """Function that sends code of argument to program execution api 
    and returns standard output.
    
    argument
        str : lang
            programing langage
        str : code
            program code

    return
        str : stdout
    """

    if api == "paiza":
        # Set URL of paiza.io
        # docs : http://api.paiza.io/docs/swagger/#!/runners/
        url_create = "http://api.paiza.io:80/runners/create"
        url_get_status = "http://api.paiza.io:80/runners/get_status"
        url_get_detail = "http://api.paiza.io:80/runners/get_details"
        # Send a program to get an ID
        params = dict(source_code=code,language=lang,api_key="guest")
        response = requests.post(url_create, params=params).json()
        run_id = response["id"]
        # Check execution status every second, and return standard output when finished.
        # if it exceeds 30 seconds, Stop checking.
        for i in range(30):
            tmp = requests.get(url_get_status, params=dict(id=run_id,api_key="guest")).json()
            if tmp["status"] == "completed":
                res = requests.get(url_get_detail, params=dict(id=run_id,api_key="guest")).json()
            
                stdout = res["build_stderr"] if res["build_stderr"] else ""
                stdout +=res["stdout"] if res["stdout"] else ""
                stdout +=res["stderr"] if res["stderr"] else ""
                return stdout
            sleep(1)
        return False

    elif api == "wandbox":
        # Set URL of wandbox
        pass
        
    return False
