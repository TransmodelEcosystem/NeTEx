# Negative examples (must-fail)

Each file carries one deliberate defect and must therefore be **rejected** by the
schema for a specific, expected reason. The cases — file, schema and expected
constraint — are declared in `.github/scripts/validate-should-fail.sh` (run in CI).

Run locally: `XMLLINT_BIN=$(which xmllint) ./.github/scripts/validate-should-fail.sh`
