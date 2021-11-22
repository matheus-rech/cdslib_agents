[![PyPI](https://img.shields.io/pypi/v/cdslib-agents?color=color=%2310d510)](https://pypi.org/project/cdslib-agents/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cdslib-agents?color=%2310d510)](https://pypi.org/project/cdslib-agents/)
[![license](https://img.shields.io/github/license/fenfisdi/cdslib_agents)](./LICENSE)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=fenfisdi_cdslib_agents&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=fenfisdi_cdslib_agents)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=fenfisdi_cdslib_agents&metric=bugs)](https://sonarcloud.io/summary/new_code?id=fenfisdi_cdslib_agents)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=fenfisdi_cdslib_agents&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=fenfisdi_cdslib_agents)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=fenfisdi_cdslib_agents&metric=coverage)](https://sonarcloud.io/summary/new_code?id=fenfisdi_cdslib_agents)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=fenfisdi_cdslib_agents&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=fenfisdi_cdslib_agents)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=fenfisdi_cdslib_agents&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=fenfisdi_cdslib_agents)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=fenfisdi_cdslib_agents&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=fenfisdi_cdslib_agents)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=fenfisdi_cdslib_agents&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=fenfisdi_cdslib_agents)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=fenfisdi_cdslib_agents&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=fenfisdi_cdslib_agents)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=fenfisdi_cdslib_agents&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=fenfisdi_cdslib_agents)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=fenfisdi_cdslib_agents&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=fenfisdi_cdslib_agents)


# CDSLib - Agents

Welcome to **CDSLib - Agents** package.

![repo_logo](https://raw.githubusercontent.com/fenfisdi/cdslib_agents/dev/images/CDSLib_agents_white-background.png "CDSLib - Agents Logo")

## Description

As part of the **Contagious Disease Simulation Library**, the
**CDSLib - Agents** package is intended to be used for modelling and simulating
contagious diseases using Agent-Based Models and it has been used for the development
of the [Contagious Disease Simulation Laboratory](https://github.com/fenfisdi/cdslab).

The package consists of different implementations of a heterogeneous population
of agents following rules of behavior that determine their movement and the evolution
of their infectious and clinical states.

The current implementation allows Agents to move in a bidemensional space following
a distribution of velocities based on population data. This can be achieved thanks to
the inclusion Distribution module which is a wrapper for different tools that provides
distribution-like function support.

In regards to the disease states, the current implementation also allows the user to
add as much states as preferred, and to create custom natural history of the disease
(i.e. the design a custom graph for evolution of disease states).

For more information, please refer to the official documentation of the project.

## Main contributors

This package was made with thanks to the leadership of
[Camilo Hincapié](https://www.linkedin.com/in/camilo-hincapie-gutierrez/)
and the contributions of
[Ian Mejía](https://github.com/IanMejia),
[Carolina Rojas Duque](https://github.com/carolinarojasd),
[Emil Rueda](https://www.linkedin.com/in/emil-rueda-424012207/),
[Nicole Rivera](https://github.com/nicolerivera1) and
[Alejandro Campillo](https://www.linkedin.com/in/alucardcampillo/).

## Contact us

For any suggestion on the development of this type of models, please our official
channels of [dicussions](https://github.com/fenfisdi/cdslib_agents/discussions)
provided by GitHub.

## License

[GNU General Public License v3 (GPLv3)](./LICENSE)
