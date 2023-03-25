# Howto: https://www.gitpod.io/docs/config-docker
# You can find the new timestamped tags here: https://hub.docker.com/r/gitpod/workspace-full/tags
FROM gitpod/workspace-full

# Install custom tools, runtime, etc.
#RUN brew install fzf
RUN sudo apt update && sudo apt upgrade -y

# Install custom tools, runtime, etc.
# base image only got `apt` as the package manager
# install-packages is a wrapper for `apt` that helps skip a few commands in the docker env.
RUN sudo install-packages shellcheck tree glances htop curl pigz par2 build-essential
 