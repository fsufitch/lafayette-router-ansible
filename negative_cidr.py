import ipaddress
import click


@click.command()
@click.option(
    "--start",
    type=str,
    default="0.0.0.0/0",
    help="What network to start from",
)
@click.option("--commas", is_flag=True, help="Use commas instead of newlines in output")
@click.argument("cidr", type=str, nargs=-1, required=True)
def main(cidr: list[str], start: str, commas: bool) -> None:
    """ "Subtract some CIDR networks from one network"""

    result_nets = [ipaddress.ip_network(start)]
    for subtracted in cidr:
        subtracted_net = ipaddress.ip_network(subtracted)
        next_result_nets = []
        for current_net in result_nets:
            if current_net.overlaps(subtracted_net):
                next_result_nets.extend(current_net.address_exclude(subtracted_net))  # type: ignore
            else:
                next_result_nets.append(current_net)

        result_nets = next_result_nets

    result_nets.sort()

    if commas:
        print(",".join(str(net) for net in result_nets))
    else:
        print("\n".join(str(net) for net in result_nets))


if __name__ == "__main__":
    main()
