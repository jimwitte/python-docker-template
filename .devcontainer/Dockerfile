# Start with base image
FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# Create SSH directory and set permissions
RUN mkdir -p /home/vscode/.ssh \
    && chmod 700 /home/vscode/.ssh \
    && chown vscode:vscode /home/vscode/.ssh

# Add GitHub to known_hosts to avoid authenticity prompts
RUN touch /home/vscode/.ssh/known_hosts \
    && chown vscode:vscode /home/vscode/.ssh/known_hosts \
    && ssh-keyscan -t rsa github.com >> /home/vscode/.ssh/known_hosts

# SSH Agent Forwarding for SSH-based commit signing
ENV SSH_AUTH_SOCK=/ssh-agent

# Configure Git inside the container for SSH-based commit signing
RUN git config --global user.name "Jim Witte" \
    && git config --global user.email "jim@thunderingbison.com" \
    && git config --global gpg.format ssh \
    && git config --global commit.gpgsign true

# Switch to vscode user
USER vscode
