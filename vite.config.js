import path from "node:path";
import { defineConfig } from "vite";

export default defineConfig({
  root: path.join(__dirname, "./assets_source/"),
  base: "/assets/",
  build: {
    outDir: path.join(__dirname, "./assets_compiled/"),
    manifest: "manifest.json",
    assetsDir: "bundled",
    rollupOptions: {
      input: ["assets_source/script.js", "assets_source/styles.scss"],
    },
  },
});
