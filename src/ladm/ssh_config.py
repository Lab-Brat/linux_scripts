import os
import yaml
from pprint import pprint

home_dir = os.getenv("HOME")
default_dir = f"{home_dir}/.ladm"


class YAML_Config:
    def __init__(self, input_conf=None) -> None:
        self.default_conf = f"{default_dir}/ssh_conf.yaml"
        yaml_config = input_conf if input_conf else self.default_conf
        self.yaml_config = self._yaml_read(yaml_config)
        self.yaml_config["pairings"] = self._ensure_options(self.yaml_config)

    def _yaml_read(self, yaml_config):
        with open(yaml_config, "r") as file:
            return yaml.safe_load(file)

    def _yaml_write(self, output_yaml=None):
        output_yaml = output_yaml if output_yaml else self.default_conf
        with open(output_yaml, "w+") as file:
            yaml.dump(self.yaml_config, file)

    def _ensure_options(self, yaml_config):
        pairings = yaml_config["pairings"]
        for pair in pairings:
            options = pairings[pair].get("options", [])
            pairings[pair]["options"] = options

        return pairings

    def yaml_show(self, host="all"):
        if host == "all":
            pprint(self.yaml_config)
        else:
            host_config = self.yaml_config["pairings"].get(host)
            if host_config:
                pprint(host_config)
            else:
                print("Host configuration not found")
                print("Existing configurations:", end = " ")
                for key in self.yaml_config["pairings"]:
                    print(key, end = " ")

    def _replace_setting(self, pair, setting, update):
        pairings = self.yaml_config["pairings"]
        pairings[pair][setting] = update
        self._yaml_write()

    def _add_option(self, pair, update):
        pairings = self.yaml_config["pairings"]
        if update in pairings[pair]["options"]:
            print("Option already defined")
            print("Current options:")
            print(pairings[pair]["options"])
            exit()
        pairings[pair]["options"].append(update)
        self._yaml_write()

    def _remove_option(self, pair, update):
        pairings = self.yaml_config["pairings"]
        if update not in pairings[pair]["options"]:
            print("Option not defined")
            print("Current options:")
            print(pairings[pair]["options"])
            exit()
        pairings[pair]["options"].remove(update)
        self._yaml_write()

    def yaml_update(self, *args):
        split = args[0].split(" ", 3)
        pair = split[0]
        setting = split[1]
        action = split[2]
        update = split[3]

        match action:
            case "x":
                self._replace_setting(pair, setting, update)
            case "+":
                self._add_option(pair, update)
            case "-":
                self._remove_option(pair, update)
            case _:
                pass


class SSH_Config:
    def __init__(self, yaml_config: YAML_Config) -> None:
        self.yaml_config = yaml_config.yaml_config
        self.indent = "  "
        self.ssh_config = []

    def _create_general_settings(self, settings):
        self.ssh_config.append("Host *")
        for setting in settings:
            self.ssh_config.append(f"{self.indent}{setting}")
        self.ssh_config.append("")

    def _create_host_settings(self, pairings):
        for pair in pairings:
            pair = self.yaml_config["pairings"][pair]
            host = " ".join(pair["host"])
            cred = self.yaml_config["identities"][pair["identity"]]
            opts = cred + pair["options"]
            self.ssh_config.append(f"Host {host}")
            for opt in opts:
                self.ssh_config.append(f"{self.indent}{opt}")
            self.ssh_config.append("")

    def _write_ssh_config(self, location=home_dir):
        with open(f"{location}/config", "w+") as file:
            for line in self.ssh_config:
                file.write(f"{line}\n")

    def create_config(self, alternative_path=None):
        general_settings = self.yaml_config["general_settings"]
        pairings = self.yaml_config["pairings"]
        self._create_general_settings(general_settings)
        self._create_host_settings(pairings)
        ssh_config_path = (
            f"{home_dir}/.ssh" if not alternative_path else alternative_path
        )
        self._write_ssh_config(ssh_config_path)
