import os
import yaml
from pprint import pprint

home_dir = os.getenv("HOME")


class SSH_Config:
    def __init__(self, yaml_config=None) -> None:
        config_dir = ".ladm"
        default_conf = f"{home_dir}/{config_dir}/ssh_conf.yaml"

        yaml_config = yaml_config if yaml_config else default_conf
        self.config = self.read(yaml_config)
        # pprint(self.config)
        self.indent = "  "
        self.ssh_config = []

    def read(self, yaml_config):
        with open(yaml_config, "r") as file:
            return yaml.safe_load(file)

    def write(self, output_yaml):
        with open(output_yaml, "w+") as file:
            yaml.dump(self.config, file)

    def _create_general_settings(self, settings):
        self.ssh_config.append("Host *")
        for setting in settings:
            self.ssh_config.append(f"{self.indent}{setting}")
        self.ssh_config.append("")

    def _create_host_settings(self, pairings):
        for pair in pairings:
            pair = self.config["pairings"][pair]
            host = " ".join(self.config["hosts"][pair["host"]])
            cred = self.config["identities"][pair["identity"]]
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
        general_settings = self.config["general_settings"]
        pairings = self.config["pairings"]
        self._create_general_settings(general_settings)
        self._create_host_settings(pairings)
        self._write_ssh_config("./")
        pprint(self.ssh_config)


if __name__ == "__main__":
    output_conf = "./new_ssh_conf.yaml"
    SSH_Config().create_config()
