# `dnsmasq`

This role sets up a `dnsmasq` DNS server. Notes:

- The server runs via a Podman container _run as root_, so "become" is required for using this role. Since this container is supposed to support DHCP (which means listening to broadcast traffic), host networking is necessary.

- The used image is a custom-built Alpine-based image. By tweaking configuration, it's possible to use other images.

- Configuration is done using a `conf.d` dropin directory (see below).

- The default setup uses no DNS upstreams. Enable `dnsmasq_resolv` or add further configuration if this is necessary.

## Role configuration

| Variable                  | Default                | Purpose                                                                                                               |
| ------------------------- | ---------------------- | --------------------------------------------------------------------------------------------------------------------- |
| dnsmasq_dir               | /opt/lafayette/dnsmasq | Host location for holding the various necessary files                                                                 |
| dnsmasq_image             | lafayette-dnsmasq      | Tag to use for the image                                                                                              |
| dnsmasq_image_build       | true                   | Build the image to use?                                                                                               |
| dnsmasq_container_name    | lafayette-dnsmasq      | Name to use for the container                                                                                         |
| dnsmasq_dns_port          | 5353                   | Port to bind for DNS queries                                                                                          |
| dnsmasq_interfaces        | []                     | List of interfaces to bind to; empty list means using the dnsmasq `bind-dynamic` directive                            |
| dnsmasq_except_interfaces | []                     | Interfaces to _not_ bind to (the `except-interfaces` block)                                                           |
| dnsmasq_resolv            | false                  | Respect /etc/resolv.conf                                                                                              |
| dnsmasq_neg_cache         | true                   | Cache negative lookups (disable for debugging)                                                                        |
| dnsmasq_cache_size        | 999999                 | Self-explanatory                                                                                                      |
| dnsmasq_log_queries       | false                  | Log all queries, for debugging                                                                                        |
| dnsmasq_address_records   | []                     | A/AAAA records to add. Values are objects of the shape `{ "addresses": [ "1.2.3.4" ], "domains": [ "example.com"] }`. |

## Further configuration and triggers

Generated configuration files:

- `{{ dnsmasq_dir }}/conf.d/00-dns.conf` &mdash; basic configuation file
- `{{ dnsmasq_dir }}/podman-{{ dnsmasq_container_name }}.service` &mdash; Systemd service file, linked to `/etc/systemd/system/...`

To perform further configuration, modify these files, then trigger the appropriate Ansible handler:

- `net.lafayette.dnsmasq :: Link Systemd service`
- `net.lafayette.dnsmasq :: Reload Systemd`
- `net.lafayette.dnsmasq :: Restart dnsmasq`
