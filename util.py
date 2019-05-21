import requests
from time import sleep

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
    url = "https://wandbox.org/api"
    compiler = {
        "python3"   :   "cpython-head",
        "c"         :   "gcc-head-c",
        "c++"       :   "gcc-head",
        "OCaml"     :   "ocaml-4.06.1",
        "php"       :   "php-head",
        "JavaScript":   "nodejs-head",
        "ruby"      :   "ruby-head",
        "Go"        :   "go-head",
        "Rust"      :   "rust-head"
    }

    param = dict(
        compiler=compiler[lang],
        code=code
        )
    r = requests.post(url+"/compile.json", json=param).json()

    stdout = ""
    
    if "program_message" in r:
        stdout += f"```\n{r['program_message']}```"
    if "compiler_message" in r:
        stdout += f"```\n{r['compiler_message']}```\n"

    return stdout
