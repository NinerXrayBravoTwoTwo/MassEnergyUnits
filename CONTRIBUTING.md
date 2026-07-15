# Contributing to MassEnergyUnits

Thank you for considering a contribution! This repository maintains a custom definition file for the `units` command-line tool that treats **time as distance** (c = 1 natural units) and makes mass-energy equivalence (E=mc²) easy to explore.

## How to Contribute

### 1. Reporting Issues or Suggestions
- Open an [Issue](https://github.com/NinerXrayBravoTwoTwo/MassEnergyUnits/issues) for:
  - Better unit definitions or aliases
  - Updated values (e.g., more accurate bomb yield estimates, new astronomical references)
  - Typos, broken links, or clarity improvements
  - Ideas that tie into spacetime geometry, entropy, or relativity education

### 2. Submitting Changes (Pull Requests)
1. Fork the repository
2. Create a new branch (`git checkout -b my-improvement`)
3. Make your changes to `massenergy.units` (and/or documentation)
4. Test locally:
   ```bash
   units -f massenergy.units
   # Try examples like:
   #   1 kton
   #   hiroshima in grams
   #   1 gram in joules
   ```
5. Commit with a clear message
6. Open a Pull Request against the master branch

### Guidelines

* Keep the spirit of the project: educational, fun, and focused on the insight that time and space are the same geometric thing, making mass and energy interchangeable.
* Prefer SI / natural units where possible.
* Add comments explaining any new definitions.
* Update the README if your changes affect usage examples.
* Feel free to expand the philosophical or historical notes — this project grew out of explorations of entropy, causality, and spacetime.

### Development Setup
You only need the standard units package (available via apt, brew, etc.).
Example alias for convenience:

```bash
alias lightunits='units -vf "" -f /path/to/massenergy.units'
```

### Questions or Discussions?
Open an Issue or reach out via the repo. Contributions that help make these concepts more accessible to non-physicists (while staying accurate) are especially welcome.
Happy hacking — may your conversions always be enlightening!