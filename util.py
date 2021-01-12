from time import sleep

import requests

from exceptions import WandBoxServiceError
from languages import Language


BASE_URL = "https://wandbox.org/api"


def run_prog(lang: Language, code: str):
    """Function that sends code of argument to program execution api 
    and returns standard output.
    
    argument
        Language : lang
            programing langage
        str : code
            program code

    return
        str : stdout
    """

    param = dict(
        compiler=lang.value,
        code=code
    )
    try:
        response = requests.post(BASE_URL + "/compile.json", json=param)
        if response.status_code != 200:
            raise WandBoxServiceError(
                status=response.status_code, body=response.text)

        r = response.json()

        stdout = ""

        if "program_message" in r:
            stdout += f"```\n{r['program_message']}```"
        if "compiler_message" in r:
            stdout += f"```\n{r['compiler_message']}```\n"
    except WandBoxServiceError as e:
        return str(e)

    return stdout


def pull_out_codeblock(text: str, block_suffix: str = '```'):
    """Function that pull out codeblock in `text`
    argument
        str : text
            target text.
        str : block_suffix
            end of codeblock.

    return
        str : pulled out codeblock
    """
    i = text.rfind(block_suffix)
    if i == -1:
        return text
    return text[:i]
