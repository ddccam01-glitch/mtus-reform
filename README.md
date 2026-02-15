# MTUS Advocacy Website

## 🌐 About This Site

This is a static website presenting personal research and analysis of the Medical Treatment Utilization Schedule (MTUS) system in California workers' compensation.

**Key Features:**
- ✅ Comprehensive legal disclaimers
- ✅ Error reporting mechanism via GitHub issues
- ✅ Downloadable research documents
- ✅ Contact form for documentary inquiries
- ✅ Mobile-responsive design
- ✅ SEO-optimized meta tags

## 🚀 Deploy to Vercel

### Step 1: Push to GitHub
```bash
git add mtus-advocacy-site/
git commit -m "Add MTUS advocacy website"
git push
```

### Step 2: Connect to Vercel
1. Go to [vercel.com](https://vercel.com) and sign up/login with GitHub
2. Click "Add New Project"
3. Import your GitHub repository (`ddccam01-glitch/claw-memory`)
4. Configure:
   - **Framework Preset:** Other (static)
   - **Root Directory:** `mtus-advocacy-site`
   - **Build Command:** (leave empty)
   - **Output Directory:** `.`
5. Click Deploy

### Step 3: Custom Domain (Optional)
1. In Vercel dashboard, go to project settings → Domains
2. Add your domain (e.g., `mtus-reform.org`)
3. Follow DNS configuration instructions

## 📁 Site Structure

```
mtus-advocacy-site/
├── index.html          # Main page with disclaimers
├── docs/               # Research documents (PDFs/TXTs)
│   ├── MTUS_EXECUTIVE_SUMMARY_14th_Amendment_Constitutional_Violation.pdf
│   ├── MTUS_CONSTITUTIONAL_VIOLATION_MASTER_REPORT.txt
│   └── ... (other documents)
├── assets/             # Images, CSS (if needed later)
└── README.md           # This file
```

## ⚖️ Legal Protection Features

1. **Prominent Disclaimer Banner** - Visible on every page load
2. **Opinion Language** - Framed as personal analysis, not facts
3. **AI Disclosure** - Transparency about AI-assisted research
4. **Fair Use Notation** - Proper trademark usage
5. **Error Reporting** - Mechanism for corrections
6. **No Legal Advice** - Clear statement this is not legal counsel

## 📝 Before Publishing

### Update These Items:
- [x] Contact email set to: dddccam01@gmail.com
- [x] Contact form implemented (Formspree)
- [x] Documents added to `docs/` folder
- [ ] Set up Formspree account (see below)
- [ ] Review all disclaimers for completeness
- [ ] Test mobile responsiveness
- [ ] Verify all download links work
- [ ] Set up GitHub issue template properly

### Optional Enhancements:
- [ ] Add Google Analytics (track visitors)
- [ ] Add social media sharing meta tags
- [ ] Create /blog section for updates
- [ ] Add search functionality
- [ ] Multi-language support

## 🔒 Security Considerations

- No user data collection (GDPR/CCPA compliant)
- Static site = no database to hack
- GitHub issues for contact = no email scraping
- Vercel provides HTTPS automatically

## 📧 Contact Setup

### Formspree Configuration (Recommended)

The site uses **Formspree** for spam-protected contact forms:

1. Go to [formspree.io](https://formspree.io)
2. Sign up with your email: **dddccam01@gmail.com**
3. Create a new form
4. Get your form endpoint URL (looks like: `https://formspree.io/f/xnqk...`)
5. Update the form action in `index.html`:
   ```html
   <form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
   ```

**Benefits:**
- Email address never exposed to bots
- Built-in spam protection
- 50 submissions/month free
- Auto-reply options available

### Alternative: Email Obfuscation
If you prefer direct email:
- Email is set to: **dddccam01@gmail.com**
- Consider JavaScript obfuscation for additional protection
- Or use a service like Cloudflare Email Routing

## 🎬 Documentary Pitch

When ready, update the contact section:
- Add film trailer/embed
- Add press kit PDF
- Add media coverage links
- Add testimonials

## ⚠️ Maintenance

**Regular checks:**
- Monitor GitHub issues for error reports
- Update documents as research evolves
- Check for broken links
- Review analytics (if enabled)

**Legal review:**
- Consider having an attorney review disclaimers
- Monitor for any cease & desist notices
- Keep records of all corrections made

---

**Remember:** This site presents opinions and analysis. It is not legal advice and makes no factual allegations against any person or entity.
