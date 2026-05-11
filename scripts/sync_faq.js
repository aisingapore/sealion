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


async function getPageContent(pageId) {
  const baseUrl = getEnv("CONFLUENCE_BASE_URL");
  const authHeader = `Basic ${Buffer.from(`${getEnv("CONFLUENCE_USERNAME")}:${getEnv("CONFLUENCE_API_TOKEN")}`).toString("base64")}`;
  const headers = { Authorization: authHeader, Accept: "application/json" };
  const url = `${baseUrl}/wiki/rest/api/content/${pageId}?expand=body.export_view`;

  const res = await fetch(url, { headers });
  if (!res.ok) throw new Error(`Confluence API error: ${res.status} for page ${pageId}`);

  const data = await res.json();
  const html = data.body.export_view.value;

  const turndown = new TurndownService({ headingStyle: "atx", bulletListMarker: "-" });
  return turndown.turndown(html);
}

async function main() {
  const pageId = getEnv("CONFLUENCE_PAGE_ID");
  const targetFile = getEnv("TARGET_FILE");

  const markdown = await getPageContent(pageId);
  fs.writeFileSync(targetFile, markdown);
}

main();
