# `load` function

The `load` function is responsible for loading the configuration data from a YAML file. It takes an optional `config_file` parameter, which specifies the path to the YAML file. If `config_file` is not provided, the function uses the default `HOME_CONFIG_FILE` path.

The function first checks if the specified `config_file` exists. If it doesn't exist, it falls back to the `ETC_CONFIG_FILE` path. If that also doesn't exist, it raises an exception indicating that no configuration file was found.

The function then opens the configuration file and uses the `YAML` module from the `ruamel.yaml` package to load the YAML data. The loaded data is then used to create a `Config` object.

The function returns the created `Config` object.

# `Config` class

The `Config` class is a simple container for storing configuration data. It takes a dictionary-like object as input when instantiated.

The class has two attributes:

1. `token`: Represents the token configuration value retrieved from the data dictionary. It can be accessed using the `token` attribute of an instance of the class.
2. `chat`: Represents the chat configuration value retrieved from the data dictionary. It can be accessed using the `chat` attribute of an instance of the class.

# Constants

There are two constants defined at the beginning of the code:

1. `WAV_THRESHOLD`: Represents a threshold value for WAV files. The purpose of this constant is not mentioned in the given code, but it is a configuration value related to WAV files.

2. `ETC_CONFIG_FILE`: Represents the path to the configuration file located at `/etc/piwalkie/config.yaml`. This file is used as a fallback if the specified `config_file` or the default `HOME_CONFIG_FILE` does not exist.

3. `HOME_CONFIG_FILE`: Represents the path to the configuration file located in the user's home directory at `.config/piwalkie/config.yaml`. This is the default file path used if no `config_file` parameter is provided to the `load` function.

# TODO

There is a `TODO` comment indicating that the threshold and other configuration values should be made configurable.

The given code defines a `load` function and a `Config` class that are used to load configuration data from a YAML file. The code assumes the existence of two possible configuration files, one located in the user's home directory and another located at `/etc/piwalkie/config.yaml`. If neither file exists, an exception is raised.

The loaded configuration data is stored in a `Config` object, which provides easy access to the configuration values through its attributes (`token` and `chat`).

Overall, this code allows for the loading and retrieval of configuration data in a concise and organized manner.