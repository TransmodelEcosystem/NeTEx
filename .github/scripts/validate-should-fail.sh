#!/bin/bash
# Negative examples: documents that MUST be rejected by the schema.
#
# Each case is declared as: should_fail <file> <expected error substring>.
# We assert BEHAVIOUR (the document is rejected, and its output contains the
# declared substring) - not a specific constraint name.
#
# All cases share ONE schema and are validated in a SINGLE xmllint call (one
# compile for many files) to stay fast. Fails closed: accepted, wrong reason, or
# xmllint not running all count as failures.
#
# CI uses the vendored 2025 Linux x86-64 xmllint ("Temporary xmllint master",
# https://github.com/TransmodelEcosystem/NeTEx/pull/915); set XMLLINT_BIN to a local
# xmllint to run this on any other OS or CPU architecture (macOS, Windows, ARM, ...).

set -u
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
ROOT_DIR=$( cd -- "${SCRIPT_DIR}/../.." &> /dev/null && pwd )
XMLLINT="${XMLLINT_BIN:-${SCRIPT_DIR}/xmllint}"
cd "${ROOT_DIR}"

SCHEMA="xsd/NeTEx_publication.xsd"

files=(); expected=()
should_fail() { files+=("$1"); expected+=("$2"); }

should_fail examples/should-fail/duplicate-GroupOfLinkSequences.xml "Duplicate key-sequence ['TEST:GroupOfLinkSequences:1', '1.0']"
should_fail examples/should-fail/duplicate-ValidBetween.xml         "Duplicate key-sequence ['TEST:ValidBetween:1', '1.0']"
should_fail examples/should-fail/duplicate-ValidityPeriod.xml       "Duplicate key-sequence ['TEST:ValidityPeriod:1', '1.0']"

out=$("${XMLLINT}" --noout --schema "${SCHEMA}" "${files[@]}" 2>&1)

fail=0
echo "Checking NeTEx 'should-fail' negative examples ..."
for i in "${!files[@]}"; do
  f="${files[$i]}"; exp="${expected[$i]}"
  if printf '%s\n' "${out}" | grep -Fqx "${f} validates"; then
    echo "SHOULD HAVE FAILED  ${f} — accepted (must be rejected)"; fail=1
  elif printf '%s\n' "${out}" | grep -F "${f}:" | grep -Fq "${exp}"; then
    echo "OK                  ${f}"
  else
    echo "ERROR               ${f} — rejected, but not matching '${exp}'"; fail=1
  fi
done

exit "${fail}"
