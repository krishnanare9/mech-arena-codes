MECHNOVA YOUTUBE AUTO-FEED PACKAGE

Included:
- index.html: site HTML with latest public YouTube uploads rendered from data/youtube-videos.json
- scripts/update_youtube_feed.py: fetches and parses the channel's public YouTube feed
- .github/workflows/update-youtube-feed.yml: refreshes feed data every 6 hours and commits changes
- data/youtube-videos.json: generated data file (starts empty; existing manually configured cards remain as fallback)

SETUP
1. Back up your current website file.
2. Copy index.html into your website repository as the site's main HTML file (commonly index.html), replacing the current version only after reviewing it.
3. Copy the scripts/, .github/workflows/, and data/ folders into the same repository, preserving folder paths.
4. In GitHub, open Settings > Actions > General > Workflow permissions and select "Read and write permissions". Save.
5. Push the files to the default branch. In the repository's Actions tab, run "Update MechNova YouTube Videos" once using Run workflow.
6. Once the workflow succeeds and the site redeploys, the latest public uploads should appear in the MechNova Videos & Gameplay area. The scheduled workflow refreshes about every 6 hours. YouTube feed outages can delay a refresh; a failed run leaves the prior JSON untouched.

No YouTube API key or Firebase Storage is used. This reads the public channel feed and embeds thumbnails from YouTube. Channel feed endpoint may occasionally be unavailable.

Brand assets: The channel ID does not provide downloadable logo/banner image files to this package. Set logo/banner in the site's existing editor using a public HTTPS image URL or images stored in your GitHub repository. Keep the fan-project disclaimer.
