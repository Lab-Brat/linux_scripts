import os
import yaml


class SSH_Config:
    def __init__(self, yaml_config=None) -> None:
        home_dir = os.getenv("HOME")
        config_dir = ".ladm"
        default_conf = f"{home_dir}/{config_dir}/ssh_conf.yaml"

        yaml_config = yaml_config if yaml_config else default_conf
        self.config = self.read(yaml_config)

    def read(self, yaml_config):
        with open(yaml_config, "r") as file:
            return yaml.safe_load(file)

    def write(self, output_yaml):
        with open(output_yaml, "w+") as file:
            yaml.dump(self.config, file)


if __name__ == "__main__":
    output_conf = "./new_ssh_conf.yaml"
    SSH_Config().write(output_conf)
