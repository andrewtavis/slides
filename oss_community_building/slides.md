---
theme: default
title: OSS Community Building
info: |
  ## OSS Community Building Presentation
  My experiences building engaged and fun communities around open-source projects.
class: text-center
transition: none
mdc: true
hideInToc: true
---

# OSS Community Building

My experiences building engaged and fun communities around open-source projects

<!--
Slide notes.
-->

---
class: text-left
transition: slide-left
hideInToc: true
---

# About me

## Andrew / Andy

- Data Analyst focussed on Linked Open Data products at Wikimedia Deutschland
- Initiator and maintainer of a few open-source, user-facing applications

## [activist.org](https://github.com/activist-org)

- Platform for political activism (organizations, working groups, events, link dump resources and more)

## [Scribe](https://github.com/scribe-org)

- Wikidata based language tools (keyboards that help second language learners, data processing tools)

<br/>

> Thanks to all of the amazing people in the above communities! ❤️

---
class: text-left
transition: slide-left
hideInToc: true
---

# Contents

<Toc minDepth="1" maxDepth="1" />

---
class: text-left
transition: slide-left
hideInToc: false
---

# Open-source roles

## Contributor (and above)

- Writes code for the issues they're assigned
- Communicates with community on their issues

## Reviewer (and above)

- Reviews code contributions from others
- Assigns issues to contributors and supports them (triage)
- Communicates with the community on issues they're familiar with

## Maintainer

- Prioritizes issues and guides projects via their roadmaps
- Facilitates community discussions (brings in reviewers and other maintainers)

---
class: text-left
transition: slide-left
hideInToc: false
---

# Preparing your project

## Tools

- [GitHub](https://github.com/) or [GitLab](https://about.gitlab.com/) (code) + \[insert email/calendar app\] + [Matrix](https://matrix.org/) (communication) + [Weblate](https://weblate.org/en/) (localization)
  - People are confused by Matrix, so suggest they use [Element](https://element.io/) in your documentation

## Documentation

> Borrow liberally from other open-source projects

- Readme: Logo at the top, project description, everything to start developing
  - About logos: A PNG banner with the project name over a color is more inviting than just text
- License: For both the code and the content
- Contributing guide: More advanced setup, all testing procedures, learning resources, etc
- Code of Conduct: [Contributor Covenant](https://www.contributor-covenant.org/) or similar
- Other: Style guide, security file, privacy policy, 3rd party software notice, localization guide, etc

---
class: text-left
transition: slide-left
hideInToc: false
---

# Finding contributors

> ... besides social media

## Issue aggregators

- [Up For Grabs](https://up-for-grabs.net/#/), [First Contributions](https://firstcontributions.github.io/), [CodeTriage](https://www.codetriage.com/) (label issues `help-wanted` / `good-first-issue`)
- [Hacktoberfest 🎃](https://hacktoberfest.com/) and [24 Pull Requests 🎁](https://24pullrequests.com/)
  - A certain number of quality contributions in a specific month or season
  - Can lead to very high quality contributors (OSS buzz during October)

## Internships

> Advertise your participation in your documentation!

- [Outreachy](https://www.outreachy.org/) ([Software Freedom Conservancy](https://sfconservancy.org/))
- [Google Summer of Code](https://summerofcode.withgoogle.com/)
- [Linux Foundation Mentorship Program (LFX)](https://lfx.linuxfoundation.org/tools/mentorship/)

---
class: text-left
transition: slide-left
hideInToc: false
---

# Who you'll find

> Either of the following groups can contribute long term

> Keep calls with contributors in mind to onboard, explain the project and pair code ☎️

## Students

- Many students need to contribute to open-source for classes
- If they are working on a school project, always ask them what the deadline is
- Positive interactions with one student can lead to others from the same school joining

## Professionals

- Often times switching careers or in-between jobs
- Ask experienced professionals to critique and write issues

---
class: text-left
transition: slide-left
hideInToc: false
---

# Supporting your community

> The following is not required, but will help build and keep people in the community

## Students

- Mentorship and working towards internships (Outreachy, GSoC, LFX)
  - They need to earn the internship over new applicants (ex: review other contributions)

## Professionals

- Help them find work via recommendations and connecting them to your network

## All

- CV, resume and application checks
- Let their interests drive their contributions (especially if you're not paying them)
- Share ownership (of part of the code, of a project, of the organization)

---
class: text-left
transition: slide-left
hideInToc: false
---

# Code repository roles

## Contributor

- Read (0: can clone project and open issues **\*Is OSS**)
- Triage (1: can manage issues and contributions)
  - ~3-6 months of regular contributions and good communication (advertise this in documentation)

## Reviewer

- Promote triage level reviewers to organization members
- Write (2: can directly commit to the project **\*2FA**)

## Maintainer

- Maintain (3: can control some project settings **\*2FA**)
- Admin (4: can control all project settings - i.e. delete it **\*2FA**)

<!--
- There being read rights means the project is open-source.
- The roles marked with 2FA need to have two factor authentication on their devices.
-->

---
class: text-left
transition: slide-left
hideInToc: false
---

# Rituals

## Dev syncs 🧑‍💻♻️

- Every two weeks on a Saturday (~15:00/16:00 UTC)
- Regular office hours for support, pair coding and people meeting one another
- Take notes in an Etherpad or other open-source notes app
- Send recap to the development channel so people who aren't there can stay caught up

## Others

- Time based: Code Nights 🌙, Code Brunches 🍞☕, whatever your community comes up with
  - In-person, hybrid and remote all possible
  - Often times attended by core contributors and those wanting to contribute more
- Deployment calls 🚀
  - Great opportunity to celebrate and teach community members

---
class: text-left
transition: slide-left
hideInToc: true
---

# Dev sync example

```
Your Project Dev Sync YYYY/MM/DD

Participants Section (please list yourself if you'd like to)

Topics
  Recap done by: NAME
  All: Introductions 👋
  All: Does anyone want a calendar invite to the dev sync?
  All: Go through the project board: LINK_TO_PROJECT_BOARD
  Name: Topic of discussion

Tasks Section

Recap Section

Here's the recap for today/yesterday/Saturday's dev sync 🧑‍💻♻️

...

The next dev sync will be [Saturday the DAY of MONTH at 16:00 UTC](ZONESTAMP_URL_FOR_NEXT_SYNC).

Nice outro 😊
```

---
class: text-left
transition: slide-left
hideInToc: false
---

# Ritual workflows

- There's a lot of work involved in keeping to your rituals, so try to automate what you can
- [Dev sync reminder message](https://github.com/scribe-org/Organization/blob/main/.github/workflows/matrix_dev_sync_reminder.yml)
  - Each Wednesday before the dev sync
  - Fully explain it as this is more for new people (others have calendar invites)
  - When it is in UTC with a [ZoneStamp](https://zonestamp.toolforge.org/)
  - Have it create the notes pad and add links to anything else a new person needs
- [Community Spotlight message 👥🎉](https://github.com/scribe-org/Organization/blob/main/.github/workflows/community_spotlight_message.yml)
  - At the end of every month run a workflow to calculate the top contributors for the period
  - Send a message with a thank you to them with links to their accounts and contributions
  - Filter out organization members so the focus is on people new to the community
  - Use this as a reminder to share things about your contributors on social media

---
class: text-left
transition: slide-left
hideInToc: false
---

# Important points

- Going above and beyond with community support builds comradery that will extend beyond yourself
- With the above in mind, please watch out for burnout
  - Take care of yourself, have a life, set boundaries and respect when people need to step away
- Include the community by saying "we" instead of "I" wherever possible
- Keep your communication positive! (but be mindful of cultural interpretations)

  - :) 😊 😀 👏 🚀 ✨ ⭐ 🌟 💫 🤩 😍 🥳 🙌 🎉 ❤️ 🧡 💛 💚 💙 🩵 💜 🩷 🤎

- Don't "lgtm": Contextualize the contribution, thank them and say you're looking forward to the next time!
- Enjoy the friendships you'll make ❤️

---
class: text-left
transition: slide-left
hideInToc: true
---

# Thank you!

- Questions, comments and suggestions are very welcome :)
- And consider joining one of the communities! We'd love to work with you! 😊

[QR codes for communities and slides]
