#!/bin/bash
# Negative examples: documents that MUST be rejected by the schema.
#
# Each case is declared as: should_fail <schema> <file> <expected error substring>.
# We assert BEHAVIOUR (the document is rejected, and its output contains the
# declared substring) - not a specific constraint name.
#
# Cases are grouped by schema and validated in ONE xmllint call per schema (one
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

PUB="xsd/NeTEx_publication.xsd"
TT="xsd/NeTEx_publication_timetable.xsd"

schemas=(); files=(); expected=()
should_fail() { schemas+=("$1"); files+=("$2"); expected+=("$3"); }

should_fail "${PUB}" examples/should-fail/duplicate-GroupOfLinkSequences.xml           "Duplicate key-sequence ['TEST:GroupOfLinkSequences:1', '1.0']"
should_fail "${PUB}" examples/should-fail/duplicate-TemplateVehicleJourney.xml         "Duplicate key-sequence ['TEST:TemplateVehicleJourney:1', '1.0']"
should_fail "${PUB}" examples/should-fail/duplicate-ValidBetween.xml                   "Duplicate key-sequence ['TEST:ValidBetween:1', '1.0']"
should_fail "${PUB}" examples/should-fail/duplicate-ValidityPeriod.xml                 "Duplicate key-sequence ['TEST:ValidityPeriod:1', '1.0']"

out=""
for schema in "${PUB}" "${TT}"; do
  batch=()
  for i in "${!files[@]}"; do [ "${schemas[$i]}" = "${schema}" ] && batch+=("${files[$i]}"); done
  [ "${#batch[@]}" -eq 0 ] && continue
  out+=$("${XMLLINT}" --noout --schema "${schema}" "${batch[@]}" 2>&1)$'\n'
done

# Failures are printed as GitHub annotations: shown on the case file in the pull request.
fail=0
echo "Checking NeTEx 'should-fail' negative examples ..."
for i in "${!files[@]}"; do
  f="${files[$i]}"; exp="${expected[$i]}"; schema="${schemas[$i]}"
  if printf '%s\n' "${out}" | grep -Fqx "${f} validates"; then
    echo "::error file=${f}::accepted by ${schema}, but must be rejected with: ${exp}"; fail=1
  elif printf '%s\n' "${out}" | grep -F "${f}:" | grep -Fq "${exp}"; then
    echo "OK  ${f}"
  else
    echo "::error file=${f}::rejected by ${schema}, but not matching: ${exp}"; fail=1
  fi
done

exit "${fail}"
