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

<div class="pt-3">
My experiences building engaged and fun communities around open-source projects
</div>

---
hideInToc: true
---

# About me

## Andrew / Andy

- Data Analyst focussed on Wikidata and other Linked Open Data products at Wikimedia Deutschland
- Initiator and maintainer of a few open-source, user-facing applications

## [activist.org](https://github.com/activist-org)

- Platform for political activism (organizations, working groups, events, link dump resources and more)

## [Scribe](https://github.com/scribe-org)

- Wikidata based language tools (keyboards that help second language learners, data processing tools)

<br/>

> Thanks to all of the amazing people in these communities! ❤️

---
hideInToc: true
---

# Contents

<Toc minDepth="1" maxDepth="1" />

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

# Preparing your project

## Tools

- [GitHub](https://github.com/) or [GitLab](https://about.gitlab.com/) (code) + \[insert email/calendar app\] + [Matrix](https://matrix.org/) (communication) + [Weblate](https://weblate.org/en/) (localization)
  - People are confused by Matrix federation, so suggest they use [Element](https://element.io/) in your documentation

## Documentation

> Borrow liberally from other open-source projects

- Readme: Project description, everything to start developing, logo at the top
  - Logos: A PNG banner with the project name over a color is more inviting than just text
- License: For both the code and the content
- Contributing guide: More advanced setup, all testing procedures, learning resources, etc
- Code of Conduct: [Contributor Covenant](https://www.contributor-covenant.org/) or similar
- Other: Style guide, security file, privacy policy, 3rd party software notice, localization guide, etc

---

# Finding contributors

> ... besides social media

## Issue aggregators

- Issues and projects searchable on websites (sometimes sent via email)
- [Up For Grabs](https://up-for-grabs.net/#/), [First Contributions](https://firstcontributions.github.io/), [CodeTriage](https://www.codetriage.com/)
  - Label issues `good-first-issue` and/or `help-wanted`
- Seasonal contribution events like [Hacktoberfest 🎃](https://hacktoberfest.com/) and [24 Pull Requests 🎁](https://24pullrequests.com/)

## Internships

> Advertise internship participation in your documentation!

- [Outreachy](https://www.outreachy.org/) ([Software Freedom Conservancy](https://sfconservancy.org/))
- [Google Summer of Code](https://summerofcode.withgoogle.com/)
- [Linux Foundation Mentorship Program (LFX)](https://lfx.linuxfoundation.org/tools/mentorship/)

---

# Who you'll find

> Either of the following groups can contribute long term

> Schedule calls motivated contributors to onboard, explain the project and pair code ☎️

## Students

- Many students need to contribute to open-source for classes
- Positive interactions with one student can lead to others from the same school joining
- If they are working on a school project, always ask them what the deadline is

## Professionals

- Often times switching careers or in-between jobs
- Ask experienced professionals to critique the project and write issues

---

# Supporting your community

> The following is not required, but will help build and keep people in the community

## Students

- Mentorship and working towards internships (Outreachy, GSoC, LFX)
  - They need to earn the internship over new applicants (can review other contributions)

## All community members

- CV, resume and application checks
- Job recommendations and connecting them to your network
- Let their interests drive their contributions (especially if you're not paying them)
- Promote them via repository triage rights, organization membership, write access (**\*2FA**), etc
- Share ownership (of part of the code, of a project, of the organization)

---

# Rituals

## Dev syncs 🧑‍💻♻️

- Every two weeks on a Saturday (~15:00/16:00 UTC)
- Regular office hours for support, pair coding and people meeting one another
- Take notes in an Etherpad or other open-source notes app
- Send recap to the development channel so people who aren't there can stay caught up

## Others

- Bi-monthly Code Nights 🌙, Code Brunches 🍞☕, whatever your community comes up with
  - In-person, hybrid and remote are all possible
  - Generally attended by core contributors and those wanting to contribute more
- Deployment calls 🚀
  - Great opportunity to celebrate and teach community members

---

# Dev sync example

```
Your Community's Dev Sync YYYY/MM/DD

Participants (please list yourself if you'd like to)
- Name

Topics
  All: Introductions 👋
  Recap done by: Name
  All: Does anyone want a calendar invite to the dev sync?
  All: Go through the project board: link_to_project_board
  Name: Topic of discussion

Tasks
- [] Task

Recap

Here's the recap for today/yesterday/Saturday's dev sync 🧑‍💻♻️ ...

The next dev sync will be ...

Nice outro 😊
```

---

# Ritual automation

- There's a lot of work involved in keeping to your rituals, so try to automate what you can
- [Dev sync reminder message](https://github.com/scribe-org/Organization/blob/main/.github/workflows/matrix_dev_sync_reminder.yml)
  - Sent each Wednesday before a dev sync
  - Fully explain it as this is more for new people (others have calendar invites)
  - Time and date in UTC with a [ZoneStamp](https://zonestamp.toolforge.org/)
  - Have it create the notes pad and add links to anything else a new person needs
- [Community Spotlight message 👥🎉](https://github.com/scribe-org/Organization/blob/main/.github/workflows/community_spotlight_message.yml)
  - At the end of every month run a workflow to calculate the top contributors for the period
  - Send a thank you message to the development channel with links to accounts and contributions
  - Filter out organization members so the focus is on people new to the community
  - Use this as a reminder to share things about your contributors on social media

---

# Important points

- Going above and beyond with community support builds comradery that will extend beyond yourself
- With the above in mind, please watch out for burnout
  - Take care of yourself, have a life, set boundaries and respect when people need to step away
- Include the community wherever possible by saying "we" instead of "I"
- Keep your communication positive! (but be mindful of cultural interpretations)

  - :) 😊 😀 👏 🚀 ✨ ⭐ 🌟 💫 🤩 😍 🥳 🙌 🎉 ❤️ 🧡 💛 💚 💙 🩵 💜 🩷 🤎

- Try to bring in contributions and discuss in the community how hard it should be to contribute
- Don't "lgtm": Contextualize the contribution, thank them and say you're looking forward to the next time!
- Enjoy the friendships you'll make ❤️

---
hideInToc: true
---

# Thank you!

- Questions, comments and suggestions are very welcome :)
- And consider joining one of the communities! We'd love to work with you! 😊

<div class="flex justify-center space-x-3 py-6">
  <div class="flex flex-col items-center">
   <img src="@images/activist_org_qr_code.png" class="h-64" alt="QR code to GitHub:activist-org"/>
   <p>GitHub:activist-org</p>
  </div>
  <div class="flex flex-col items-center">
    <img src="@images/scribe_org_qr_code.png" class="h-64" alt="QR code to GitHub:scribe-org"/>
    <p>GitHub:scribe-org</p>
  </div>
  <div class="flex flex-col items-center">
    <img src="@images/oss_community_building_qr_code.png" class="h-64" alt="QR code to a markdown file for the slides"/>
    <p>Slides Content</p>
  </div>
</div>
