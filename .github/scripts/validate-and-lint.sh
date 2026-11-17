#!/bin/bash
# Validate the XML file structure and lint XSD and XML files, e.g. indentation
#
# You need the binary `xmllint`
# apt-get install libxml2-utils

# The -e flag causes the script to exit as soon as one command returns a non-zero exit code
set -e

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

echo "Validating XML file structure and linting XSD and XML files ..."

PARSING_ERROR=0
# Iterate all XML and XSD files
while IFS= read -r -d $'\0' filename; do
  # Prettify the file using xmllint and save the result to ${filename}.pretty
  if XMLLINT_INDENT=$'\t' $SCRIPT_DIR/xmllint --encode UTF-8 --format --pretty 1 "${filename}" >"${filename}.pretty"; then
    # Remove lines containing the term "xmlspy" to get rid of advertising this and save the result as ${filename}
    grep -i -v "xmlspy" "${filename}.pretty" >"${filename}"
  else
    PARSING_ERROR=$?
    echo -e "\033[0;Validating XML structure of file '${filename}' failed\033[0m"
  fi
  # Remove temp file
  rm "${filename}.pretty"
done < <(/usr/bin/find examples xsd -type f \( -name "*.xsd" -or -name "*.xml" \) -print0)

if [ ${PARSING_ERROR} -ne 0 ]; then
  exit ${PARSING_ERROR}
fi
echo -e '\033[0;32mFinished linting XSD and XML files\033[0m'
