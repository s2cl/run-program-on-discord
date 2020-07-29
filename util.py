from time import sleep

import requests

from exceptions import WandBoxServiceError

BASE_URL = "https://wandbox.org/api"

COMPILER_MAP = {
    "python3"    :   "cpython-head",
    "c"          :   "gcc-head-c",
    "c++"        :   "gcc-head",
    "OCaml"      :   "ocaml-4.06.1",
    "php"        :   "php-head",
    "JavaScript" :   "nodejs-head",
    "ruby"       :   "ruby-head",
    "Go"         :   "go-head",
    "Rust"       :   "rust-head"
}


def run_prog(lang, code):
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

    param = dict(
        compiler=COMPILER_MAP[lang],
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


def pull_out_codeblock(text, block_suffix='```'):
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
