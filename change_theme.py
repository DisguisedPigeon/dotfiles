import json
import sys

configs = {
        "kitty" : "./config/kitty/color.ini",
        "qtile" : "./config/qtile/config.py",
        "nitrogen" : "./config/nitrogen/bg-saved.cfg",
        }


def load_theme(file):
    with open(file, 'r') as f:
        contents = f.read()

    configs = ""
    for i in contents:
        configs += i

    configs = json.loads(configs)
    return configs

def read_configs():
    global configs
    files = {}
    with open(configs["kitty"], 'r') as f:
        files["kitty"] = f.readlines()

    with open(configs["qtile"], 'r') as f:
        files["qtile"] = f.readlines()

    with open(configs["nitrogen"], 'r') as f:
        files["nitrogen"] = f.readlines()


    return files

def write_files(contents):
    global configs

    with open(configs["kitty"], "w") as f:
        f.write(contents["kitty"])

    with open(configs["qtile"], "w") as f:
        f.write(contents["qtile"])

    with open(configs["nitrogen"], "w") as f:
        f.write(contents["nitrogen"])


def apply_configs(theme, files):
    aux = ""
    for i, val in enumerate(files["kitty"]):
        for j in theme["kitty"].keys():
            if val != "\n" and val.split()[0] == j:
                if theme["kitty"][j] == None:
                    other = j[:5] + str(int(j[5:]) - 8)
                    theme["kitty"][j] = theme["kitty"][other]
                val = val[: -len(val) + len(j)] + "\t" + str(theme["kitty"][j]) + "\n"
        aux += val
    files["kitty"] = aux
    
    aux = ""
    for i, val in enumerate(files["qtile"]):
        for j in theme["qtile"].keys():
            if val.strip().startswith("\"" + j):
                val = val[:-11] + "\"" + theme["qtile"][j] +"\",\n"

        aux += val
    files["qtile"] = aux

    aux = ""
    for i, val in enumerate(files["nitrogen"]):
        for j in theme["nitrogen"].keys():
            if val.startswith(j):
                val = val[:len(j)+1]+ theme["nitrogen"][j] +"\n"
        aux += val
    files["nitrogen"] = aux

    write_files(files)

def main(args):
    theme = load_theme("./themes/"+args)
    files = read_configs()
    apply_configs(theme, files)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("invalid number of arguments")
        sys.exit()
    main(sys.argv[1])
