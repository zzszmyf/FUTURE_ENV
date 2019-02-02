import sys
import yaml
import os

conf = {}
def read_yaml(filepath):
    f = open(filepath)
    res = yaml.load(f)
    return res


def init(*argv):
    argv = argv[0]
    container_name = conf["base"]["container_name"]
    container_path = conf["base"]["container_path"]
    local_path = conf["base"]["local_path"]
    use_sudo = conf["base"]["use_sudo"]
    code_path = conf["base"]["code_path"]
    image_name = conf["init"]["image_name"]
    from_var = conf["init"]["from"]
    git_var = conf["init"]["git"]
    user_var = conf["init"]["user"]
    def make_Dockfile(filename, from_var, user_var, code_path, git_var):
        with open(filename, "w") as f:
            f.write("FROM " + from_var + "\n")
            f.write("USER " + user_var + "\n")
            f.write("WORKDIR " + code_path + "\n")
            f.write("RUN git clone " + git_var + "\n")
    make_Dockfile("./Dockerfile", from_var, user_var, code_path, git_var)
    sudo_flag = ""
    name_arg = "--name " + container_name 
    if use_sudo == 1:
        sudo_flag = "sudo"
    build_cmd = sudo_flag + " docker build -f " + "./Dockerfile ./ -t " + image_name
    print build_cmd
    volumn_arg = local_path + ":" + container_path
    run_cmd = "cp -r " + code_path + " " + container_path
    base_cmd = "docker run -it -v"
    cmd = " ".join([sudo_flag, base_cmd, volumn_arg, name_arg, image_name, run_cmd])
    print cmd
    os.system(build_cmd)
    os.system("rm ./Dockerfile")
    os.system(cmd)


def build(*argv):
    print argv


def run(*argv):
    print argv


run_fun = {"init":init, "build":build, "run":run}
if __name__ == "__main__":
    conf = read_yaml("./conf.yaml")
    print conf
    func = run_fun[sys.argv[1]](sys.argv[1:])


