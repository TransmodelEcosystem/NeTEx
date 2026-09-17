#!/bin/bash
# Negative examples: documents that MUST be rejected by the schema.
#
# Each case is "<file>|<expected error substring>". We assert BEHAVIOUR (the
# document is rejected, and its output contains the declared substring) - not a
# specific constraint name, and each case carries its own clause.
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

# "<file>|<expected error substring>"
NS="{http://www.netex.org.uk/netex}"
CASES=(
  "examples/should-fail/duplicate-GroupOfLinkSequences.xml|Element '${NS}GroupOfLinkSequences': Duplicate key-sequence ['TEST:GroupOfLinkSequences:1', '1.0']"
  "examples/should-fail/duplicate-ValidBetween.xml|Element '${NS}ValidBetween': Duplicate key-sequence ['TEST:ValidBetween:1', '1.0']"
  "examples/should-fail/duplicate-ValidityPeriod.xml|Element '${NS}ValidityPeriod': Duplicate key-sequence ['TEST:ValidityPeriod:1', '1.0']"
)

files=()
for c in "${CASES[@]}"; do files+=("${c%%|*}"); done
out=$("${XMLLINT}" --noout --schema "${SCHEMA}" "${files[@]}" 2>&1)

fail=0
echo "Checking NeTEx 'should-fail' negative examples ..."
for c in "${CASES[@]}"; do
  f="${c%%|*}"; expected="${c#*|}"
  if printf '%s\n' "${out}" | grep -Fqx "${f} validates"; then
    echo "SHOULD HAVE FAILED  ${f} — accepted (must be rejected)"; fail=1
  elif printf '%s\n' "${out}" | grep -F "${f}:" | grep -Fq "${expected}"; then
    echo "OK                  ${f}"
  else
    echo "ERROR               ${f} — rejected, but not matching '${expected}'"; fail=1
  fi
done

exit "${fail}"
