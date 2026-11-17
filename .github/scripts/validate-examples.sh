#!/bin/bash
# Validate all OJP XML examples from the examples/ directory against the OJP XSD schema
#
# You need the binary `xmllint`
# apt-get install libxml2-utils

# The -e flag causes the script to exit as soon as one command returns a non-zero exit code
set -e

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

echo "Validating NeTEx XML examples ..."

if /usr/bin/find examples/functions examples/standards -type f -name "*.xml" -print0 | xargs -0 $SCRIPT_DIR/xmllint --noout --schema xsd/NeTEx_publication.xsd; then
  echo -e '\033[0;32mValidating NeTEx XML examples succeeded\033[0m'
else
  echo -e '\033[0;31mValidating NeTEx XML examples failed\033[0m'
  exit 1
fi
