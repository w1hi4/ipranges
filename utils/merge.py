import argparse

import netaddr


def iter_networks(source):
    for line_number, raw_value in enumerate(source, start=1):
        value = raw_value.strip()
        if not value:
            continue

        try:
            yield netaddr.IPNetwork(value)
        except netaddr.AddrFormatError as exc:
            raise SystemExit(f'Invalid IP or CIDR on line {line_number}: {value!r}') from exc


def main():
    parser = argparse.ArgumentParser(description='Merge IP addresses into the smallest possible list of CIDRs.')
    parser.add_argument('--source', nargs='?', type=argparse.FileType('r'), required=True, help='Source file path')
    args = parser.parse_args()

    for addr in netaddr.cidr_merge(iter_networks(args.source)):
        print(addr)


if __name__ == '__main__':
    raise SystemExit(main())
