<div align="center">
  <a href="https://github.com/andrewtavis/slides"><img src="https://raw.githubusercontent.com/andrewtavis/slides/main/.github/resources/SlidesLogoGitHubBanner.png" width=1024 alt="Slides logo"></a>
</div>

[![issues](https://img.shields.io/github/issues/andrewtavis/slides?label=%20&logo=github)](https://github.com/andrewtavis/slides/issues)
[![license](https://img.shields.io/github/license/andrewtavis/slides.svg?label=%20)](LICENSE.txt)
[![coc](https://img.shields.io/badge/Contributor%20Covenant-ff69b4.svg)](.github/CODE_OF_CONDUCT.md)

### Presentations related to open source

This repo contains various presentations for open-source software related topics. The slides are created using [Slidev](https://github.com/slidevjs/slidev).

Suggestions for how to improve the content of these slides are more than welcome! ✨ Edits will mainly be made in the corresponding `slides.md` file for each presentation. Please see the [contributing guide](CONTRIBUTING.md) if you'd like to help.

## **Contents**

- [OSS Community Building](https://github.com/andrewtavis/slides/tree/main/oss_community_building)
  - How to build efficient and fun communities
- [OSS Maintenance](https://github.com/andrewtavis/slides/tree/main/oss_maintenance)
  - Tips for maintaining open-source software

## Building Slides

First clone this repository or your fork:

```bash
git clone https://github.com/andrewtavis/slides.git
# git clone https://github.com/<your-username>/slides.git
```

Setup [Prettier](https://prettier.io/) to format `slides.md` files via the top level [package.json](package.json) and [.prettierrc](.prettierrc) files via one of the commands below:

```bash
yarn install
npm install
pnpm install
```

Then navigate to the slides you'd like to run and execute the `run dev` command for your package manager of choice:

```bash
cd SLIDES_OF_CHOICE

# Run one of the following commands to build and open the slides:
yarn run dev
npm run dev
pnpm run dev
```

Once finished you can visit <http://localhost:3030> to view the slides. Follow the prompts in your terminal to close them or do other actions.
