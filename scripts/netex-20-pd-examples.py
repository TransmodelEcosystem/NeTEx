import re
import sys
from pathlib import Path

VERSION = 'ntx:2.0'

pattern = re.compile(
    rb'<PublicationDelivery\b[^>]*>'
)


def update_file(path: Path) -> None:
    content = path.read_bytes()

    def replace(match: re.Match[bytes]) -> bytes:
        tag = match.group()

        if re.search(rb'\bversion\s*=', tag):
            return re.sub(
                rb'\bversion\s*=\s*(["\']).*?\1',
                f'version="{VERSION}"'.encode(),
                tag,
            )

        return tag[:-1] + f' version="{VERSION}">'.encode()

    updated = pattern.sub(replace, content, count=1)

    if updated != content:
        path.write_bytes(updated)
        print(f'Updated: {path}')
    else:
        print(f'Unchanged: {path}')


def main() -> None:
    file_list = Path(sys.argv[1])

    for line in file_list.read_text().splitlines():
        filename = line.strip()

        if filename:
            update_file(Path(filename))


if __name__ == '__main__':
    main()
