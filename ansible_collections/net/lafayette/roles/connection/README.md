# `net.lafayette.connection`

This role sets up a network connection, using NetworkManager (via `nmcli`). It requires "become".

## Configuration

| Name                 | Default   | Purpose                                                      |
| -------------------- | --------- | ------------------------------------------------------------ |
| connection_interface |           | Interface to use                                             |
| connection_name      |           | Name of the connection                                       |
| connection_ip_manual | false     | Configure the connection IP manually (`true` means use DHCP) |
| connection_ipv4      |           | IPv4 address to use for manual configuration                 |
| connection_ipv4_cidr | 24        | Subnet to use for manual configuration                       |
| connection_zone      | lafayette | Firewalld zone to set for this connection                    |
