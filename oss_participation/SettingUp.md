# OSS Participation Slides

This project contains a Slidev presentation for OSS participation.
It is built using **Slidev**, and requires the **latest Node.js** and **latest Yarn (v4+)** to run.

---

## Prerequisites

1. **Node.js** (latest v20+ recommended)
   Download from [Node.js official website](https://nodejs.org/en/download/).

2. **Corepack** (bundled with Node.js >=16.10)
   Corepack is used to manage the correct Yarn version.

3. **Yarn** (latest stable, v4+)
   Corepack can activate the correct Yarn version automatically.

---

## Setup Instructions

### 1. Enable Corepack

```bash
corepack enable
```

### 2. Activate the project Yarn version

```bash
corepack prepare yarn@4.10.3 --activate
```

> This ensures the project uses the exact Yarn version defined in `package.json`.

### 3. Install project dependencies

From the project root:

```bash
yarn install
```

---

## Running the Slides

To start the Slidev development server:

```bash
yarn dev
```

You should see output like:

```
➜  Local: http://localhost:3030/
```

Open the provided URL in your browser to view the slides.

---

## Notes

* Make sure your shell is using **the latest Node.js**:

```bash
node -v
npm -v
```

* Make sure Corepack is enabled and the correct Yarn version is active:

```bash
yarn --version
```

* If you see path or version issues, refresh your shell hash:

```bash
hash -r
```

or run Yarn using the full path:

```bash
/usr/local/bin/yarn install
/usr/local/bin/yarn dev
```

* Slidev is a live development server — changes to `slides.md` will automatically update in the browser.

---

## References

* [Slidev Official Docs](https://sli.dev/)
* [Yarn Corepack Guide](https://yarnpkg.com/getting-started/qa#using-corepack)

