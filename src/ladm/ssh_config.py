import os
import yaml
from pprint import pprint

home_dir = os.getenv("HOME")


class YAML_Config:
    def __init__(self, input_conf=None) -> None:
        default_conf = f"{home_dir}/.ladm/ssh_conf.yaml"
        yaml_config = input_conf if input_conf else default_conf
        self.yaml_config = self._yaml_read(yaml_config)

    def _yaml_read(self, yaml_config):
        with open(yaml_config, "r") as file:
            return yaml.safe_load(file)

    def _yaml_write(self, output_yaml=None):
        output_yaml = output_yaml if output_yaml else f"{home_dir}/.ladm/ssh_conf.yaml"
        with open(output_yaml, "w+") as file:
            yaml.dump(self.yaml_config, file)

    def yaml_show(self):
        pprint(self.yaml_config)

    def _replace_setting(self, pair, setting, update):
        pairings = self.yaml_config["pairings"]
        pairings[pair][setting] = update
        self._yaml_write()

    def yaml_update(self, *args):
        split = args[0].split()
        pair = split[0]
        setting = split[1]
        action = split[2]
        update = split[3]

        match action:
            case "x":
                self._replace_setting(pair, setting, update)
            case "+":
                pass
            case "-":
                pass
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
            host = " ".join(self.yaml_config["hosts"][pair["host"]])
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

    def create_config(self):
        general_settings = self.yaml_config["general_settings"]
        pairings = self.yaml_config["pairings"]
        self._create_general_settings(general_settings)
        self._create_host_settings(pairings)
        self._write_ssh_config("./")
        pprint(self.ssh_config)


if __name__ == "__main__":
    yaml_conf = YAML_Config()
    yaml_conf.yaml_update("labbrat identity x labbrat")
    # SSH_Config(yaml_conf).create_config()
