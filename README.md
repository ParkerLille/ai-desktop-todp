# AI Desktop Todo

AI Desktop Todo is a Windows desktop todo application built as a pnpm monorepo.

## Repository layout

- `apps/desktop` — Tauri desktop app
- `apps/ai-service` — Python AI service scaffold
- `packages/contracts` — shared contracts and types
- `packages/ui` — shared UI primitives
- `packages/config` — shared app configuration

## Scripts

From the repository root:

- `pnpm dev:desktop` — start the desktop app in development mode
- `pnpm dev:ai` — start the AI service in development mode
- `pnpm lint` — run lint checks across the workspace
- `pnpm typecheck` — run TypeScript type checks across the workspace
- `pnpm test` — run tests across the workspace
- `pnpm build` — build all workspace packages

## Environment

Copy `.env.example` to `.env` and adjust local values as needed.
