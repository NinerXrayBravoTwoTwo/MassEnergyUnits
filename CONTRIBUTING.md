# Contributing to MassEnergyUnits

Thank you for considering a contribution! This repository maintains a custom definition file for the GNU `units` tool that treats **time as distance** (`c = 1` natural units) and makes mass–energy equivalence (\(E = mc^2\)) easy to explore.

## How to contribute

### 1. Reporting issues or suggestions

Open an [Issue](https://github.com/NinerXrayBravoTwoTwo/MassEnergyUnits/issues) for:

- Better unit definitions or aliases
- Updated values (e.g. more accurate bomb yield estimates, new astronomical references)
- Typos, broken links, or clarity improvements
- Ideas that tie into spacetime geometry, entropy, or relativity education

### 2. Submitting changes (pull requests)

1. Fork the repository
2. Create a branch (`git checkout -b my-improvement`)
3. Change `massenergy.units`, `minkowski_entropy/`, and/or the docs (`README.md`, this file, etc.)
4. Test locally:

   **GNU Units** (load the **system** units database first, then this file):

   ```bash
   # Interactive session
   units -f /usr/share/units/definitions.units -f ./massenergy.units

   # One-shot checks
   units -f /usr/share/units/definitions.units -f ./massenergy.units '1 g' 'kton'
   units -f /usr/share/units/definitions.units -f ./massenergy.units 'hiroshima' 'g'
   units -f /usr/share/units/definitions.units -f ./massenergy.units 'nagasaki' 'hiroshima'
   ```

   On macOS with Homebrew, use  
   `"$(brew --prefix)/share/units/definitions.units"` instead of `/usr/share/units/definitions.units`.

   **Python package** (from the repository root):

   ```bash
   python minkowski_entropy/spacetime_entropy.py
   python minkowski_entropy/half_double.py double 100 400 10
   ```

5. Commit with a clear message
6. Open a pull request against `master`

## Guidelines

- Keep the spirit of the project: educational, approachable, and focused on the insight that time and space share geometry so mass and energy convert directly.
- Prefer SI and natural units where possible.
- Keep `massenergy.units` **small and commented**.
- When adding or revising yields, link device names to the yield name (e.g. `gadget` → `trinity`) so mass–energy stays consistent under `c = 1`.
- Prefer aliases for synonyms (`dinokill` → `chicxulub`, `ton_e` → `ton_tnt`) rather than duplicating numbers.
- Add a short comment for any new definition (source or rationale if the value is an estimate).
- Keep the light-second scale consistent: **299792.458 km** (`LIGHT_SECOND_KM` in Python, `s` in the units file).
- Update `README.md` (and module docs) if usage examples, the built-in names table, or install steps change.
- Philosophical or historical notes are welcome when they stay accurate and help non-specialists.

## Development setup

You only need [GNU Units](https://www.gnu.org/software/units/) (e.g. `apt install units`, `brew install units`).

Optional convenience alias (adjust the path to your clone):

```bash
# Linux / WSL
alias lightunits='units -vf /usr/share/units/definitions.units -f /path/to/MassEnergyUnits/massenergy.units'
alias lightunits='(units -vf "" -f /usr/share/units/massenergy.units)'

# macOS Homebrew
alias lightunits='units -vf "$(brew --prefix)/share/units/definitions.units" -f /path/to/MassEnergyUnits/massenergy.units'
```

Or permanently include the file from your personal units data:

```bash
echo "!include /full/path/to/massenergy.units" >> ~/.units
```

See `README.md` for full install notes.

## License

By contributing, you agree that your contributions are licensed under the project’s [MIT License](LICENSE).

## Questions or discussions?

Open an Issue on the repo. Contributions that make these ideas more accessible to non-physicists—while staying accurate—are especially welcome.

Happy hacking — may your conversions always be enlightening!
