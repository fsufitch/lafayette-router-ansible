# `dnsmasq_main`

This role sets up a `dnsmasq` DNS server. Notes:

- This role should be run as root.
- The server runs via a Podman container.
- Configuration files for this server should be placed in `/opt/lafayette/dnsmasq/conf.d/` (configurable; see `defaults/main.yml`). This dir is mounted into the container.
- The Containerfile for building the container is in `/opt/lafayette/dnsmasq/Containerfile`.
- The base configuration in the dir is in a file called `00_base.conf`. Don't overwrite it later.
- The container is configured to run with **host networking**. It must be run as root. This is necessary so it can appropriately bind to DHCP broadcast ports, if so configured.
- The default setup only includes enough DNS to cover a DHCP use case. It does not forward queries to any upstream source.

## Configuration

| Variable                  | Default                | Purpose                                                                                    |
| ------------------------- | ---------------------- | ------------------------------------------------------------------------------------------ |
| dnsmasq_dir               | /opt/lafayette/dnsmasq | Host location for holding the various necessary files                                      |
| dnsmasq_image             | lafayette-dnsmasq      | Tag to use for the image                                                                   |
| dnsmasq_image_build       | true                   | Build the image to use?                                                                    |
| dnsmasq_container_name    | lafayette-dnsmasq      | Name to use for the container                                                              |
| dnsmasq_dns_port          | 5353                   | Port to bind for DNS queries                                                               |
| dnsmasq_interfaces        | []                     | List of interfaces to bind to; empty list means using the dnsmasq `bind-dynamic` directive |
| dnsmasq_except_interfaces | []                     | Interfaces to _not_ bind to (the `except-interfaces` block)                                |
| dnsmasq_resolv            | false                  | Respect /etc/resolv.conf                                                                   |
| dnsmasq_neg_cache         | true                   | Cache negative lookups (disable for debugging)                                             |
| dnsmasq_cache_size        | 999999                 | Self-explanatory                                                                           |
| dnsmasq_log_queries       | false                  | Log all queries, for debugging                                                             |
