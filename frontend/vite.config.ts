import path from "node:path"
import { TanStackRouterVite } from "@tanstack/router-vite-plugin"
import preact from "@preact/preset-vite"
import { defineConfig } from "vite"

// https://vitejs.dev/config/
export default defineConfig({
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
      "react": "preact/compat",
      "react-dom": "preact/compat",
    },
  },
  plugins: [preact(), TanStackRouterVite()],
})
