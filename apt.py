#!/usr/bin/python3

import requests
import re
import os
import time

PREINSTALLED = ["apt", "dpkg", "debconf", "tar", "wget", "zlib", "zip", "python2", "gzip"]

def parse_dependency_field(field_value):
    dependencies = []
    for dep in field_value.split(","):
        dep = dep.strip()
        match = re.match(r"([^\s(]+)(?: \((.+)\))?", dep)
        if match:
            package = match.group(1)
            version = match.group(2) if match.group(2) else None
            dependencies.append({
                "package": package,
                "version": version
            })
    return dependencies
def parse_packages_file(file_path):
    packages = []
    package_info_temp = {
        "Full-Raw": ""
    }
    package_info = dict(package_info_temp)
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line == "":
                if package_info:
                    packages.append(package_info)
                    package_info = dict(package_info_temp)
            else:
                package_info["Full-Raw"] += line
                if ": " in line:
                    key, value = line.split(": ", 1)
                    if key in ["Pre-Depends", "Depends", "Suggests", "Replaces"]:
                        package_info[key] = parse_dependency_field(value)
                    else:
                        package_info[key] = value
                else:
                    if package_info:
                        last_key = list(package_info.keys())[-1]
                        package_info[last_key] += f"\n{line}"
        if package_info and package_info.get("Package") is not None:
            packages.append(package_info)
    return packages
def get_package(parsed_data, package_name):
    for x in parsed_data:
        if package_name == x.get("Package", ""):
            return x
def search_packages(parsed_data, package_name):
    founds = []
    for x in parsed_data:
        if (package_name.lower() in x.get("Package", "")) or (package_name.lower() in x.get("Description", "").lower()):
            founds.append(x)
    return founds
def get_pools(parsed_data, package_name, donewith = []):
    package = get_package(parsed_data, package_name)
    if (package_name in donewith+PREINSTALLED) or (package is None):
        return []
    donewith.append(package_name)
    pools = []
    for x in package.get("Pre-Depends", []):
        pools += get_pools(parsed_data, x["package"], donewith)
    pools += [[package_name, package["Filename"]]]
    for x in package.get("Depends", []):
        pools += get_pools(parsed_data, x["package"], donewith)
    return pools

this_py_file_path = os.path.abspath(".")+"/"
print("Parsing APT Packages file...")
parsed_data = parse_packages_file(this_py_file_path+"ManticAPT")
time.sleep(1)
print("APT Packages file since September 2023. Ubuntu Mantic.")
time.sleep(0.2)
print("Seek medical attention.")
os.makedirs(this_py_file_path+"/deb/", exist_ok=True)
while True:
    time.sleep(1.5)
    command = input("~ $ apt ").split(" ")
    if command[0] == "install":
        command.pop(0)
        time.sleep(1)
        if len(command) > 0:
            packages_exist = True
            for x in command:
                if get_package(parsed_data, x) is None:
                    print("Could not find package \""+x+"\".")
                    packages_exist = False
                    break
            if packages_exist:
                print("Reading nothing... Done")
                time.sleep(0.5)
                print("Creating dependency list... ", end="")
                pools = []
                for x in command:
                    pools += get_pools(parsed_data, x)
                time.sleep(0.75)
                print("Done")
                print("Reading nothing again... Done")
                time.sleep(0.5)
                if len(pools) > 0:
                    print("The following packages will be DOWNLOADED:")
                    print("  ", end="")
                    size = 0
                    for x in pools:
                        if size + len(x[0]) > 40:
                            print("\n  ", end="")
                            size = 0
                        print(x[0]+" ", end="")
                        size += len(x[0])+1
                    print()
                    endpoint="http://us-east-1.ec2.archive.ubuntu.com/ubuntu/"
                    failed = 0
                    for x in pools:
                        print("Downloading package "+x[0]+"...", end="")
                        downloadfile = this_py_file_path+"deb/"+x[1].split("/")[-1]
                        downloadurl = endpoint+x[1]
                        try:
                            download = requests.get(downloadurl)
                            with open(downloadfile, "wb") as f:
                                f.write(download.content)
                            print("Done")
                        except:
                            failed += 1
                            print("Failed")
                    if failed > 0:
                        print(str(failed)+"/"+str(len(pools))+" of packages failed to download!")
                    else:
                        print("Successfully downloaded packages.")
                else:
                    print("Dependency list is empty. Perhaps you're trying to install something listed as PREINSTALLED already?")
        else:
            print("Missing required arguments: package1")
    elif command[0] == "search":
        command.pop(0)
        time.sleep(1.75)
        if len(command) > 0:
            print("Sorting nothing... Done")
            time.sleep(0.5)
            print("Finding string by string using in... ", end="")
            results = search_packages(parsed_data, " ".join(command))
            time.sleep(0.5)
            print("Done")
            for x in results:
                time.sleep(0.01)
                print(x["Package"]+"/mantic")
                print("  "+x.get("Description", "*No description.*"))
        else:
            print("Missing required arguments: query")
    elif command[0] == "exit":
        time.sleep(2)
        break
    else:
        time.sleep(0.25)
        print("APT Package Manager - vblablabla")
        if len(command[0]) > 0:
            print("APT - Invalid command \""+command[0]+"\"")
        print("List of commands:")
        print("  install - download a deb package")
        print("  search - search packages")
        print("  exit - ")
        print("             This APT has no powers.")