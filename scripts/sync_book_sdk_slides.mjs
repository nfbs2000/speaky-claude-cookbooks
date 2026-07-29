import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const targetDir = path.join(repoRoot, "docs", "slides", "book-sdk-ko");
const targetHtml = path.join(targetDir, "index.html");
const targetManifest = path.join(targetDir, "artifact.json");

function valueAfter(flag) {
  const index = process.argv.indexOf(flag);
  return index >= 0 ? process.argv[index + 1] : undefined;
}

function sha256(filePath) {
  return crypto.createHash("sha256").update(fs.readFileSync(filePath)).digest("hex");
}

function verify() {
  const manifest = JSON.parse(fs.readFileSync(targetManifest, "utf8"));
  const actualHash = sha256(targetHtml);
  if (actualHash !== manifest.build.sha256) {
    throw new Error(`Book SDK slide hash mismatch: ${actualHash}`);
  }
  console.log(`verified Book SDK slides: ${manifest.build.sceneCount} scenes, ${actualHash}`);
}

if (process.argv.includes("--verify")) {
  verify();
} else {
  const sourceDir = valueAfter("--source");
  const sourceCommit = valueAfter("--source-commit");
  if (!sourceDir || !sourceCommit) {
    throw new Error("Usage: node scripts/sync_book_sdk_slides.mjs --source <dist> --source-commit <sha>");
  }

  const sourceHtml = path.resolve(sourceDir, "index.html");
  const sourceContract = path.resolve(sourceDir, "recording", "replay-site-contract.json");
  if (!fs.existsSync(sourceHtml) || !fs.existsSync(sourceContract)) {
    throw new Error(`Book SDK slide dist is incomplete: ${path.resolve(sourceDir)}`);
  }

  const contract = JSON.parse(fs.readFileSync(sourceContract, "utf8"));
  fs.mkdirSync(targetDir, { recursive: true });
  fs.copyFileSync(sourceHtml, targetHtml);
  fs.writeFileSync(targetManifest, `${JSON.stringify({
    schemaVersion: "book-sdk.public-slide.v1",
    publicUrl: "https://nfbs2000.github.io/speaky-claude-cookbooks/slides/book-sdk-ko/",
    source: {
      repository: "nfbs2000/vibe-with-claude-code-education",
      path: "slide/book-sdk-ko/site",
      commit: sourceCommit,
    },
    build: {
      sha256: sha256(targetHtml),
      bytes: fs.statSync(targetHtml).size,
      sceneCount: contract.metadata?.sceneCount ?? null,
    },
  }, null, 2)}\n`);
  verify();
}
