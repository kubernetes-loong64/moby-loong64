# Docker for LoongArch64

<p align="center"><a href="README.md">English</a> | <a href="README-zh.md">中文</a></p>

<p align="center"><img src="https://img.shields.io/badge/Docker%20LoongArch64%20%E9%BE%99%E8%8A%AF%E6%9E%B6%E6%9E%84%E5%8F%91%E8%A1%8C%E7%89%88-blue?logo=docker&logoColor=white" alt="Docker LoongArch64 龙芯架构发行版"></p>

Build [Docker (Moby)](https://github.com/moby/moby) binaries for the **LoongArch64 (loong64)** architecture via CI/CD.

## How it works

A GitHub Actions workflow clones the specified moby version, cross-compiles with
`GOOS=linux GOARCH=loong64` in a Debian 13 container, and builds `dockerd` and `docker-proxy` into the
`bundles/binary/` directory. Target platform: `linux/loong64`.

See [Discussion #6 — Why Use container: debian:13?](https://github.com/orgs/kubernetes-loong64/discussions/6) for the
rationale behind the Debian 13 container choice.

## Branch naming

Push a branch named `loong64-<moby-version>` (e.g. `loong64-docker-v29.5.1`) to trigger a build. Append `+<build>`
(e.g. `loong64-docker-v29.5.1+0`) to include build metadata.

## [Release](https://github.com/kubernetes-loong64/moby-loong64/releases)

Push a tag matching `release-loong64-<moby-version>` (e.g. `release-loong64-docker-v29.5.1+0`) to publish
a GitHub Release with the built binaries.

The `+<build>` suffix provides build metadata (e.g. `+0`, `+1-alpha.1`).

The suffix in the build metadata indicates the release stage:

| Suffix  | Stage         |
|---------|---------------|
| `alpha` | Internal beta |
| `beta`  | Public beta   |
| `rc`    | Pre-release   |
| (none)  | Stable        |

## Release artifacts

Each release includes the following files:

| File           | Description          |
|----------------|----------------------|
| `dockerd`      | Docker daemon binary |
| `docker-proxy` | Docker proxy binary  |

## License

[Apache License 2.0](LICENSE)
