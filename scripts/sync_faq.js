import fs from "fs";
import TurndownService from "turndown";

function getEnv(key) {
  const val = process.env[key];
  if (!val) {
    console.error(`Missing required env var: ${key}`);
    process.exit(1);
  }
  return val.trim();
}

function stripConfluenceMacros(html) {
  return html
    .replace(
      /<ac:structured-macro[^>]*ac:name="code"[^>]*>[\s\S]*?(?:<ac:parameter ac:name="language">([^<]*)<\/ac:parameter>)?[\s\S]*?<ac:plain-text-body><!\[CDATA\[([\s\S]*?)\]\]><\/ac:plain-text-body>[\s\S]*?<\/ac:structured-macro>/g,
      (_, lang, code) => `<pre><code class="language-${lang || ""}">${code}</code></pre>`
    )
    .replace(
      /<ac:structured-macro[^>]*ac:name="(info|note|warning|tip)"[^>]*>[\s\S]*?<ac:rich-text-body>([\s\S]*?)<\/ac:rich-text-body>[\s\S]*?<\/ac:structured-macro>/g,
      (_, type, body) =>
        `<blockquote><p><strong>${type.toUpperCase()}:</strong></p>${body}</blockquote>`
    )
    .replace(/<ac:emoticon[^>]*ac:emoji-fallback="([^"]*)"[^>]*\/>/g, (_, emoji) => emoji)
    .replace(/<ac:emoticon[^>]*\/>/g, "")
    .replace(/<\/?ac:[^>]*>/g, "");
}

async function getPageContent(pageId) {
  const baseUrl = getEnv("CONFLUENCE_BASE_URL");
  const authHeader = `Basic ${Buffer.from(`${getEnv("CONFLUENCE_USERNAME")}:${getEnv("CONFLUENCE_API_TOKEN")}`).toString("base64")}`;
  const headers = { Authorization: authHeader, Accept: "application/json" };
  const url = `${baseUrl}/wiki/rest/api/content/${pageId}?expand=body.storage`;

  const res = await fetch(url, { headers });
  if (!res.ok) throw new Error(`Confluence API error: ${res.status} for page ${pageId}`);

  const data = await res.json();
  const html = stripConfluenceMacros(data.body.storage.value);

  const turndown = new TurndownService();
  return turndown.turndown(html);
}

async function main() {
  const pageId = getEnv("CONFLUENCE_PAGE_ID");
  const targetFile = getEnv("TARGET_FILE");

  const markdown = await getPageContent(pageId);
  fs.writeFileSync(targetFile, markdown);
}

main();
