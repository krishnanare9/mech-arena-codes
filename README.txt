MECHNOVA WEBSITE — MAINTENANCE NOTES

Live site:
https://mechnovaofficial.github.io/

Repository:
https://github.com/mechnovaofficial/mechnovaofficial.github.io

YOUTUBE VIDEO FEED
- The homepage reads latest public uploads from data/youtube-videos.json.
- scripts/update_youtube_feed.py fetches the channel's public YouTube RSS feed and writes the latest entries.
- The single scheduled workflow is .github/workflows/refresh-youtube-feed.yml.
- It runs every 3 hours and can also be started manually from GitHub Actions with "Run workflow".
- If YouTube's feed is unavailable or returns no usable entries, the script fails without overwriting the existing JSON.
- GitHub Actions needs repository Actions write permission for the workflow to commit changed feed data.
- After a successful commit, GitHub Pages may take a short time to publish the update. A browser hard refresh can help bypass cached page assets.

PROMO CODES
- Promo codes are displayed from the built-in list, with Firestore used for optional remote updates.
- MIDGAMECHANNEL4ALL is listed for all players with a stated expiry of December 1, 2026.
- The website does not guarantee live redemption; the game publisher determines eligibility and validity.
- Never add account passwords, OTPs, or other secrets to website code or promo-code reports.

PRIVACY AND ANALYTICS
- analytics.js loads Google Analytics only after a visitor accepts optional analytics consent.
- Keep the privacy policy and consent controls aligned if analytics behavior changes.

MAINTENANCE
- Keep the independent Mech Arena fan-project disclaimer.
- Check internal navigation and mobile layout after significant HTML/CSS changes.
- Do not change sitemap.xml unless the sitemap task is explicitly being worked on.
