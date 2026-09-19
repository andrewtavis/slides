<div align="center">
  <a href="https://codeberg.org/andrewtavis/slides"><img src="https://codeberg.org/andrewtavis/slides/raw/branch/main/.github/resources/SlidesGitHubBanner.png" style="width: 100%; max-width: 100%;" alt="Slides logo"></a>
</div>

[![issues](https://img.shields.io/gitea/issues/open/andrewtavis/slides?gitea_url=https://codeberg.org&label=%20&logo=codeberg&logoColor=ffffff)](https://codeberg.org/andrewtavis/slides/issues)
[![license](https://img.shields.io/github/license/andrewtavis/slides.svg?label=%20)](LICENSE.txt)
[![coc](https://img.shields.io/badge/Contributor%20Covenant-ff69b4.svg)](.github/CODE_OF_CONDUCT.md)

### Presentations related to open source and politics

This repo contains various presentations for open-source software related topics. The slides are created using [Slidev](https://github.com/slidevjs/slidev).

Suggestions for how to improve the content of these slides are more than welcome! ✨ Edits will mainly be made in the corresponding `slides.md` file for each presentation. Please see the [contributing guide](CONTRIBUTING.md) if you'd like to help.

## Contents

- [Left-wing Federalism](https://codeberg.org/andrewtavis/slides/src/branch/main/left_wing_federalism)
  - Worker Power, Dissolved Borders and the End of Nationalism
- [OSS Maintenance and Community Building](https://codeberg.org/andrewtavis/slides/src/branch/main/oss_maintenance_and_community_building)
  - My experiences building engaged and fun communities around open-source projects
- [Open Source Software Participation](https://codeberg.org/andrewtavis/slides/src/branch/main/oss_participation)
  - What is open source software and how you can actively participate

## Running Slides

### Prerequisites

1. [Node.js](https://nodejs.org): latest v20+ recommended
2. [Yarn](https://yarnpkg.com/): latest v4+, which will be activated automatically via [Corepack](https://yarnpkg.com/getting-started/qa#using-corepack)

### Building Slides

First clone this repository or your fork:

```bash
git clone https://codeberg.org/andrewtavis/slides.git
# git clone https://codeberg.org/<your-username>/slides.git
```

Navigate to the `slides` project and install the dependencies for all presentations via [Corepack](https://yarnpkg.com/getting-started/qa#using-corepack):

```bash
cd slides

corepack enable
yarn install

# Alternatively:
npm install
pnpm install
```

Build and open your slides of choice by navigating to its directory, linking it to the shared dependencies and executing the `run dev` command:

```bash
cd SLIDES_OF_CHOICE
yarn run dev

# Alternatively:
npm run dev
pnpm run dev
```

Once finished you can visit <http://localhost:3000> to view the slides. Follow the prompts in your terminal to close the slides or do other actions. Note also that [Slidev](https://github.com/slidevjs/slidev) is a live development server — changes to the `slides.md` files for each presentation will automatically be reflected in the browser.
