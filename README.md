# Ansible-managed Router Setup for a "Lafayette" Home Network

TODO details.

To run:

```sh
poetry install
```

```sh
poetry run ansible-playbook -K -i inventory/01_marquis.yaml playbooks/main.yaml
```

> `-K` is included so Ansible can ask for a sudo password to use.
