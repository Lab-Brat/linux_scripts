#!/bin/bash

conf_dir="$HOME/.config/linux_scripts_adm"
template_dir=$(dirname $(dirname $(readlink -f $0)))

# create config directory if it doesn't exist
if [[ ! -d $conf_dir ]]; then
    mkdir -p $conf_dir
    echo "Created $conf_dir"
fi

# create a default Vagrantfile if the config dir is empty
if [[ ! -e $conf_dir/Vagrantfile ]]; then
    cp $template_dir/templates/Vagrantfile $conf_dir/Vagrantfile
    echo "Copied Vagrantfile to $conf_dir/Vagrantfile"
fi

# create a key to be used by Vagrantfile
if [[ ! -e $conf_dir/vagrant_key && ! -e $conf_dir/vagrant_key.pub ]]; then
    ssh-keygen -P '' -q -f $conf_dir/vagrant_key
    echo "SSH keys created at $conf_dir"
fi

# configue VAGRANT_CWD variable
#!/bin/bash

var_name="VAGRANT_CWD"
var_value="$conf_dir"

# Check if the environment variable is already defined
if [ -z "${!var_name}" ]; then
    echo "Environment variable $var_name is not defined. Setting it now..."

    export $var_name=$var_value
    echo "" >>~/.zshrc
    echo "export $var_name=$var_value" >>~/.zshrc

    echo "Environment variable $var_name has been set to '$var_value' and added to ~/.zshrc."
fi

echo ""
echo "Nothing else to do :)"
