[[_TOC_]]

# Introduction

This repository is for testing EPEC product.

Repository uses ATE as a Git submodule.
ATE submodule is meant to contain shared python APIs towards test setup with various devices.

Following chapters describes the content of this repository and meaning of each folder.

# Repository structure

## Apps

Folder which contain all applications used in testing EPEC product.

Applications in this folder are created using [EPEC Multitool Creator](https://extranet.epec.fi/Public/Manuals/MultiToolWebhelp/MultiTool.html#t=ProjectTopics%2F1_general.htm) code base or plain [Codesys](https://www.codesys.com/).

## ext/ATE

ATE repository is added as a [Git submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules).

This way all libraries and other functionalities are commonly used from ATE across all products which are tested on ATE tester.

Sometimes to be able to test something on ATE it requires changes to ATE code used as a submodule, the easiest way to do this is to clone ATE Git repository into separate folder.

When changes are done from this repository you can point to your custom branch commit using SHA or later on to latest commit SHA in main branch.

Here are some useful Git commands required to work with submodule.

**Cloning this repository:**

```git
git clone https://epectfssrv.ad.epec.fi/tfs/Epec%20Products/EnvironmentalTestingSystem/_git/SL8X1-0001
```

**Please note that this will not fetch submodules, following commands is needed for that:**

```git
git submodule init
git submodule update
```

**When changes are done in ATE repository separately, following command sets to point certain commit to ATE:**

```git
cd ext/ATE
git checkout <SHA>
```

```git
cd ext/ATE
git checkout b12638e475a41478b1a461af0f4e27d241d3d866
```

**Add submodule SHA update to commit of this repository:**

```git
cd ..
cd ..
git add ext/ATE
git commit -m "submodule updated."
git push
```


## Pipelines

[Pipeline](ext/ATE/pipelines) folder contain pipeline definition files in YAML format.
These files are used to define what kind of pipeline is used for this repository.

Pipelines can be used from azure and current pipelines are [Manual](pipelines/manual.yaml) and [Release](pipelines/release.yaml) pipeline.

- Manual pipeline is used in test development phase so user can execute tests remotely from Azure.
- Release pipeline is used when all test suites are executed for certain FW release.

## Robot

[Robot](ext/ATE/robot) folder contain Robot Framework test suites and resource files.

## Veristand

[Veristand](ext/ATE/veristand) folder contains NI Veristand project which goal is to define mapping and configuration used in ATE test setup.

More information about ATE see [README](ext/ATE/README.md) from ext/ATE folder.

## Pylintrc

[.pylintrc](.pylintrc) file contains rules for python [linter](https://marketplace.visualstudio.com/items?itemName=ms-python.pylint).

*"Linting highlights syntactical and stylistic problems in your Python source code, which often helps you identify and correct subtle programming errors or unconventional coding practices that can lead to errors."*

## Robocop

[.robocop](.robocop) file contains rules for Robot Framework [linter](https://github.com/MarketSquare/robotframework-robocop).

*"Robocop is a tool that performs static code analysis of Robot Framework code.
It uses official Robot Framework parsing API to parse files and runs number of checks, looking for potential errors or violations to code quality standards (commonly referred as linting issues)."*

## Create aliases

[Batch script](create_aliases.bat) is made to be executed when aliases mapping to hardware IOs is updated using National Instrument's [Veristand](https://www.ni.com/en/shop/data-acquisition-and-control/application-software-for-data-acquisition-and-control-category/what-is-veristand.html) software.

This executes script which parses Veristand XML file and generates Robot Framework resource file with ALIASES variables. These variables from resource file can be used in Robot test suites instead of physical Veristand IO channel mapping.

## Run tests

[Run tests batch script](run_tests.bat) is made to execute all tests from robot/tests folder.

Batch script can be modified by user based on the needs when developing tests by adding different execution path or Robot Framework tags etc. Script is handy when more than one test suite needs to be executed.

Please note that When executing one test or suite, then RobotCode plugin is way to go.

Test tags:
| Tag  | Meaning |
| ------------- | ------------- |
| epic_12345  | Epic ticket number from Azure backlogs.  |
| robot:skip-on-failure  | Runs test but skips rest of test case on failure, visible in log / report.  |
| robot:skip  | Skip test case, visible as skipped in log / report.  |
| robot:exclude  | Exclude test from execution, test not included in log / report.  |

See more information about test execution from [ATE repository guidelines](ext/ATE/docs/GUIDELINES.md).