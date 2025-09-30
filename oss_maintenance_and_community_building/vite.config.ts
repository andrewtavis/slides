// SPDX-License-Identifier: CC0-1.0
import { defineConfig } from "vite";

export default defineConfig({
  resolve: {
    alias: {
      "@images": "../public/images",
    },
  },
});
