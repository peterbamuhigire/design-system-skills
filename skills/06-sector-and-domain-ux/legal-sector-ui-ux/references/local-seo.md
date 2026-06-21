# Legal Sector Local SEO Reference

## LocalBusiness + Attorney JSON-LD Schema

Place this schema in the `<head>` of every page. Update bracketed fields per client.

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": ["LegalService", "LocalBusiness"],
      "@id": "[https://www.firmwebsite.com/#organization]",
      "name": "[Firm Name]",
      "url": "[https://www.firmwebsite.com]",
      "logo": "[https://www.firmwebsite.com/images/logo.png]",
      "image": "[https://www.firmwebsite.com/images/office.jpg]",
      "description": "[One-sentence description of the firm and practice areas]",
      "telephone": "[+1-XXX-XXX-XXXX]",
      "email": "[contact@firmwebsite.com]",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "[123 Main Street, Suite 400]",
        "addressLocality": "[City]",
        "addressRegion": "[State abbreviation]",
        "postalCode": "[ZIP]",
        "addressCountry": "US"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": "[latitude]",
        "longitude": "[longitude]"
      },
      "openingHoursSpecification": [
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
          "opens": "09:00",
          "closes": "17:00"
        }
      ],
      "priceRange": "[$ to $$$]",
      "areaServed": [
        {
          "@type": "City",
          "name": "[Primary City]"
        },
        {
          "@type": "City",
          "name": "[Secondary City]"
        }
      ],
      "knowsAbout": [
        "[Practice Area 1]",
        "[Practice Area 2]",
        "[Practice Area 3]"
      ],
      "sameAs": [
        "[https://www.google.com/maps/place/...]",
        "[https://www.avvo.com/attorneys/...]",
        "[https://www.martindale.com/...]",
        "[https://www.linkedin.com/company/...]"
      ]
    },
    {
      "@type": "Attorney",
      "@id": "[https://www.firmwebsite.com/attorneys/attorney-name/#attorney]",
      "name": "[Attorney Full Name]",
      "url": "[https://www.firmwebsite.com/attorneys/attorney-name/]",
      "image": "[https://www.firmwebsite.com/images/attorney-name-headshot.jpg]",
      "jobTitle": "[Attorney / Partner / Associate]",
      "description": "[One sentence about this attorney's practice focus]",
      "telephone": "[+1-XXX-XXX-XXXX]",
      "email": "[attorney@firmwebsite.com]",
      "worksFor": {
        "@id": "[https://www.firmwebsite.com/#organization]"
      },
      "alumniOf": {
        "@type": "EducationalOrganization",
        "name": "[Law School Name]"
      },
      "memberOf": [
        {
          "@type": "Organization",
          "name": "[State Bar Name]"
        },
        {
          "@type": "Organization",
          "name": "[ABA or specialty bar]"
        }
      ],
      "areaServed": {
        "@type": "City",
        "name": "[Primary City]"
      },
      "knowsAbout": [
        "[Primary Practice Area]",
        "[Secondary Practice Area]"
      ]
    }
  ]
}
```

**Schema placement notes**:
- Use `@graph` to combine multiple schema types on the same page
- Add the `Attorney` block for each attorney; link to the firm via `worksFor`
- On practice area pages, add a `Service` schema block for that specific practice
- Validate with Google's Rich Results Test before deploying

---

## Google Business Profile Optimization Checklist for Law Firms

Complete all items before the site launches. An incomplete GBP profile leaves local search rankings on the table.

### Setup and Verification

- [ ] Claim or create the Google Business Profile at business.google.com
- [ ] Verify the listing via postcard, phone, or video verification
- [ ] Confirm the business name matches exactly what appears on the website and all directories — letter for letter, punctuation identical
- [ ] Confirm phone number is in the same format across website, GBP, and all directories

### Categories

- [ ] Primary category: "Law Firm"
- [ ] Add secondary categories matching actual practice areas (e.g., "Personal Injury Attorney," "Family Law Attorney," "Criminal Justice Attorney")
- [ ] Do not add categories for practice areas the firm does not actively handle

### Business Information

- [ ] Full street address (use Suite/Floor if applicable)
- [ ] Local phone number (not a tracking number that changes)
- [ ] Website URL (homepage URL, not a campaign landing page)
- [ ] Business hours — accurate and complete; add holiday hours seasonally
- [ ] For criminal defense firms: mark "Open 24 hours" if 24/7 emergency line is available
- [ ] Service area: add surrounding cities and counties the firm serves

### Profile Content

- [ ] Business description: 750-character limit; include primary practice areas and geographic area in first 250 characters; no claims that violate bar advertising rules
- [ ] Services: add each practice area as a service; include description and price range if applicable (estate planning flat fees convert well here)
- [ ] Products: not typically used for law firms — leave blank unless the firm offers specific packaged services

### Photos

- [ ] Exterior photo: building exterior so clients recognize it
- [ ] Interior photo: reception area or consultation room
- [ ] Team photo: group shot, approachable
- [ ] Individual attorney headshots: minimum one per attorney
- [ ] Cover photo: best-quality office or team photo; 1332 x 750 pixels minimum
- [ ] All photos: real photos of the actual office and attorneys; no stock photography

### Reviews

- [ ] Respond to every existing review before launch — positive and negative
- [ ] Set up a process for requesting reviews post-case-close (see review acquisition template below)
- [ ] Target: 10+ Google reviews before considering the profile "established"

### Posts

- [ ] Publish at least one Google post before launch (blog article summary or announcement)
- [ ] Maintain a posting cadence: minimum one post every two weeks

---

## Keyword Structure: Practice Area + Location Patterns

### Primary Keyword Formula

`[practice area] attorney [city] [state]`
`[practice area] lawyer [city] [state]`

Both "attorney" and "lawyer" are searched; build pages targeting both where content supports it.

### Keyword Matrix for Common Practice Areas

| Practice Area | Primary Keywords | Secondary / Long-Tail |
|---------------|-----------------|----------------------|
| Personal Injury | personal injury attorney [city], car accident lawyer [city] | truck accident attorney [city], slip and fall lawyer [city], motorcycle accident attorney [city] |
| Family Law | divorce attorney [city], family law lawyer [city] | child custody attorney [city], divorce lawyer near me, uncontested divorce [city] |
| Criminal Defense | criminal defense attorney [city], DUI lawyer [city] | criminal defense lawyer near me, felony attorney [city], DUI attorney [city state] |
| Estate Planning | estate planning attorney [city], will attorney [city] | living trust attorney [city], probate lawyer [city], estate planning lawyer near me |
| Immigration | immigration attorney [city], immigration lawyer [city] | green card attorney [city], deportation defense lawyer [city], visa attorney [city] |
| Business Law | business attorney [city], corporate lawyer [city] | contract lawyer [city], LLC attorney [city], small business attorney [city] |
| Employment Law | employment attorney [city], wrongful termination lawyer [city] | discrimination attorney [city], workplace harassment lawyer [city] |
| Workers' Comp | workers compensation attorney [city], work injury lawyer [city] | workers comp lawyer near me, on the job injury attorney [city] |

### City-Level Page Strategy

Create dedicated pages for: primary city, major surrounding suburbs (top 3–5 by population or case volume), county seat if different from city.

Each city-level page must have:
- Unique introductory paragraph referencing local courts, local context, or local community (not just city name swap)
- Embedded Google Map for that location or the nearest office
- Local phone number if available; at minimum, the main line
- Internal link back to the primary practice area page

---

## Legal Directory Citation Building

Build and maintain consistent NAP (Name, Address, Phone) listings across all directories. Inconsistent NAP is a local SEO ranking factor — check that every listing uses identical spelling, abbreviations, and formatting.

### Priority Directory List

| Directory | Priority | Notes |
|-----------|----------|-------|
| Google Business Profile | 1 — Critical | Highest impact on local rankings and conversions |
| Avvo.com | 2 — High | Attorney-specific; high domain authority; claim and complete fully |
| FindLaw.com | 3 — High | High traffic legal directory; free basic listing available |
| Martindale-Hubbell | 4 — High | Peer review ratings; long-established credibility signal |
| Justia.com | 5 — High | Free; strong domain authority; good for attorney profiles |
| Lawyers.com | 6 — Medium | Linked with Martindale; one profile serves both |
| Yelp | 7 — Medium | High consumer trust; claim and respond to reviews |
| State bar directory | 8 — Medium | Authoritative source; keep bio current |
| LinkedIn (attorney profiles) | 9 — Medium | Useful for business/corporate practices; links back to firm site |
| Nolo.com | 10 — Lower | Worth listing; drives some search traffic |
| HG.org | 11 — Lower | Older directory; still indexed |
| LegalMatch | 12 — Optional | Review carefully — some fee structures conflict with bar rules |

### Citation Audit Before Launch

Before submitting new listings, audit existing listings for the firm and its attorneys across the top 6 directories. Inconsistent old listings suppress rankings. Clean up or claim and correct any existing listings before creating new ones.

**NAP consistency rule**: Pick one format and use it everywhere.

```
Correct:
Name:    Smith Law Group, P.C.
Address: 123 Main Street, Suite 400, Chicago, IL 60601
Phone:   (312) 555-0100

Wrong (inconsistent with above):
Name:    Smith Law Group
Address: 123 Main St., Ste. 400, Chicago, Illinois 60601
Phone:   312-555-0100
```

---

## Review Acquisition Email Template

Send this email within 5 business days of a case closing successfully. Personalize the bracketed fields. Check your state bar's advertising rules before sending any review request — most jurisdictions permit this, but confirm.

---

Subject: [Client First Name] — a quick request from [Attorney First Name]

[Client First Name],

It was an honour to represent you through this process. I hope you are settling in well now that your case is behind you.

If you have a few minutes, I would genuinely appreciate a Google review. Reviews help other people in situations like yours find our firm when they need help most.

Here is a direct link: [Google Business Profile review link]

There is no obligation at all — I simply wanted to ask. If you prefer not to, that is completely fine.

Thank you for trusting me with your case.

[Attorney First Name]
[Firm Name] | [Phone]

---

**Ethics notes for review requests**:
- Do not offer anything of value in exchange for a review — this violates bar rules in most jurisdictions and Google's policies
- Do not ask clients to post positive reviews; ask them to share their honest experience
- Do not ask for reviews in the immediate aftermath of a difficult outcome — timing matters
- Do not use a mass review request service that sends unsolicited messages to all former clients

---

## Review Response Templates

### Positive Review Response

> Thank you for taking the time to share your experience, [First Name]. Representing clients through [type of situation] is work we take seriously, and it means a great deal to hear that we were able to help. We wish you all the best going forward. — [Attorney or Firm Name]

**Guidelines**:
- Respond within 48 hours
- Personalize with the client's first name if used in the review
- Do not disclose case details, even if the client did — privacy
- Keep it brief; do not use the response as advertising copy

### Negative Review Response

> Thank you for sharing your feedback. We take all client experiences seriously and are sorry to hear this did not meet your expectations. We would welcome the opportunity to discuss this with you directly — please contact our office at [phone] so we can understand what happened and how we can address it. — [Firm Name]

**Guidelines**:
- Never disclose client information or dispute facts publicly — this creates ethics exposure
- Acknowledge the feedback without admitting fault
- Offer to resolve it offline via phone
- Do not ask Google to remove a negative review unless it violates Google's policies (fake, spam, not a client)
- One response per review — do not engage in back-and-forth publicly
