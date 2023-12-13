
CHANGELOG
=========

## [v0.0.54] - 2023-12-13
### :bug: Bug Fixes
- [`36f50f5`](https://github.com/athril/sparc.client/commit/36f50f5eb30d9d47081a8f3f2d9ffadfa1aedd6e) - cleaning pyproject.toml *(commit by [@athril](https://github.com/athril))*


## [v0.0.53] - 2023-12-13
### :sparkles: New Features
- [`c8df965`](https://github.com/athril/sparc.client/commit/c8df9657232c8bb2bdb7df39632d3a1b1eccad90) - dynamic versioning - works? *(commit by [@athril](https://github.com/athril))*

### :bug: Bug Fixes
- [`c4a022c`](https://github.com/athril/sparc.client/commit/c4a022cfb9eff8fb59d6a4a4a3fb2eccb8d841ec) - __init__ error *(commit by [@athril](https://github.com/athril))*
- [`bc1805c`](https://github.com/athril/sparc.client/commit/bc1805caf1d874ef5f068854239a056cc91561a6) - pyproject fix *(commit by [@athril](https://github.com/athril))*


## [v0.0.50] - 2023-12-12
### :bug: Bug Fixes
- [`6b7bdb3`](https://github.com/athril/sparc.client/commit/6b7bdb393017b877d4500e3022334857a8908ba2) - metadata fix *(commit by [@athril](https://github.com/athril))*


## [v0.0.46] - 2023-12-12
### :sparkles: New Features
- [`a3c6885`](https://github.com/athril/sparc.client/commit/a3c68857adab0b41581506394e4e8aa657feff4b) - Dynamic versioning *(commit by [@athril](https://github.com/athril))*

### :bug: Bug Fixes
- [`2d8892a`](https://github.com/athril/sparc.client/commit/2d8892a69d0038b9b400b0f0cac33638fe47d9d6) - package versioning *(commit by [@athril](https://github.com/athril))*


## [v0.0.45] - 2023-12-12
### :bug: Bug Fixes
- [`57a0581`](https://github.com/athril/sparc.client/commit/57a05811c9d395cc0da291c04e68fb27db12d0ee) - imports update *(commit by [@athril](https://github.com/athril))*


## [v0.0.42] - 2023-12-12
### :sparkles: New Features
- [`3124672`](https://github.com/athril/sparc.client/commit/31246720c92a0acbeaaf648878d5c46e5747c99d) - improving release mechanism *(commit by [@athril](https://github.com/athril))*



## [v0.2.0] 
### :sparkles: New features
- Added O2SparcService service:
   * Introduced a `O2SparcSolver` class which is the main class for running computational jobs on o²S²PARC. This class holds the following methods:
   * `submit_job`
   * `get_job_progress`
   * `job_done`
   * `get_results`
   * `get_job_log`
- Introduced `get_solver` method to `O2SparcService` which returns a `O2SparcSolver` object
- Scaffold Retrieval:
   * Introducing the ability to use `sparc.client` to retrieve scaffolds or scaffold descriptions.
   * The retrieved scaffold or scaffold description files can now be converted to a commonly used mesh format, such as VTK.
   * Reuse of packages from the mapping tools codebase ensures efficient and standardized mesh conversion.
- MBF Segmentation Export:
   * Added support for exporting MBF Segmentation data to a commonly used mesh format, like VTK.
- Segmentation Data Analysis:
   * New functionality to analyze a given segmentation data file for suitability in the mapping tools fitting workflow, and provide a clear and informative report.
- Updated Documentation:
   * Added the [SPARC Python Zinc Client tutorial](https://github.com/nih-sparc/sparc.client/blob/main/docs/tutorial-zinc.ipynb) to reflect the features related to Zinc.


## [v0.1.0] 
### :bug: Bug Fixes
- download multiple files from Pennsieve #12
- pennsieve Download file API #14
- Github action updates: Reviewdog should run whenever a PR is modified after opening #15
- new tutorial in Jupyter Notebook
- README.md update


## [v0.0.2] 
Alpha2 release of Python Sparc Client.
### :sparkles: New features
- Code coverage at 100%
- Sphinx documentation with Github Pages

## [v0.0.1] 
Alpha release of Python Sparc Client.
### :sparkles: New features
- automatic/manual module loading
- ServiceBase class for adding new modules
- Pennsieve module with basic functionalities: 
   * listing datasets, files, records
   * downloading files
   * Basic API support (GET/POST) 



[v0.0.42]: https://github.com/athril/sparc.client/compare/v0.0.41...v0.0.42
[v0.0.45]: https://github.com/athril/sparc.client/compare/v0.0.44...v0.0.45
[v0.0.46]: https://github.com/athril/sparc.client/compare/v0.0.45...v0.0.46
[v0.0.50]: https://github.com/athril/sparc.client/compare/v0.0.49...v0.0.50
[v0.0.53]: https://github.com/athril/sparc.client/compare/v0.0.52...v0.0.53
[v0.0.54]: https://github.com/athril/sparc.client/compare/v0.0.53...v0.0.54