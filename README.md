<div align="center">
  <a href="https://github.com/andrewtavis/slides"><img src="https://raw.githubusercontent.com/andrewtavis/slides/main/.github/resources/SlidesGitHubBanner.png" width=1024 alt="Slides logo"></a>
</div>

[![issues](https://img.shields.io/github/issues/andrewtavis/slides?label=%20&logo=github)](https://github.com/andrewtavis/slides/issues)
[![license](https://img.shields.io/github/license/andrewtavis/slides.svg?label=%20)](LICENSE.txt)
[![coc](https://img.shields.io/badge/Contributor%20Covenant-ff69b4.svg)](.github/CODE_OF_CONDUCT.md)

### Presentations related to open source

This repo contains various presentations for open-source software related topics. The slides are created using [Slidev](https://github.com/slidevjs/slidev).

Suggestions for how to improve the content of these slides are more than welcome! ✨ Edits will mainly be made in the corresponding `slides.md` file for each presentation. Please see the [contributing guide](CONTRIBUTING.md) if you'd like to help.

## **Contents**

- [OSS Maintenance and Community Building](https://github.com/andrewtavis/slides/tree/main/oss_maintenance_and_community_building)
  - My experiences building engaged and fun communities around open-source projects

## Building Slides

First clone this repository or your fork:

```bash
git clone https://github.com/andrewtavis/slides.git
# git clone https://github.com/<your-username>/slides.git
```

Navigate to the `slides` project and install the dependencies for all presentations:

```bash
cd slides

# Based on your package manager:
yarn install
npm install
pnpm install
```

Build and open your slides of choice by navigating to its directory, linking it to the shared dependencies and executing the `run dev` command for your package manager:

```bash
cd SLIDES_OF_CHOICE

# Based on your package manager:
yarn install
yarn run dev

npm install
npm run dev

pnpm install
pnpm run dev
```

Once finished you can visit <http://localhost:3000> to view the slides. Follow the prompts in your terminal to close them or do other actions.
