"""Visibility-service content using the site's existing sections and cards."""
from html import escape

ONE_TIME = [
 ('Google + AI Visibility Audit', 99, 'Website SEO audit; AI/AEO readiness audit; Search-result research; Competitor research; Service/keyword opportunities; Customer-question research; Existing FAQ analysis; Page-title/meta analysis; Heading/content structure review; Local relevance review; Business information consistency review; Schema / structured-data opportunities; Internal-link issues; Missing pages/content; AI search visibility testing; Prioritized recommendations report'),
 ('AI Search Foundation', 249, 'Optimize up to 5 existing pages; Rewrite page titles; Rewrite meta descriptions; Improve headings; Improve service descriptions; Add answer-friendly content; Create customer-focused FAQs; Improve local/service relevance; Improve internal linking; Structured FAQ content; Add appropriate schema where supported; Improve About/business entity information; Improve how services are described for search and AI systems; Identify thin or duplicate content; Baseline AI visibility testing; Before-and-after report'),
 ('Local SEO + AI Visibility', 399, 'Everything in AI Search Foundation, with up to 10 pages total; Competitor analysis; Local keyword research; AI question / prompt research; Service-area research; Location-specific content optimization; Expanded FAQs; Content-gap analysis; Stronger service-page copy; LocalBusiness / service schema where supported; Internal linking overhaul; Homepage entity optimization; About-page optimization; Contact/location-data optimization; Search-intent analysis; AI search testing across multiple customer searches; Recommendations for additional pages; Final visibility report'),
 ('AI Visibility Buildout', 649, 'Everything in Local SEO + AI Visibility, with up to 20 website pages total; Multiple services/categories; Multiple service areas; Deep competitor content comparison; Expanded customer-question research; New FAQ sections; New supporting website content; Service-page rewrites; Legitimate location-page copy where useful; Topic clusters; Stronger business/entity information; Advanced internal linking; Structured-data expansion where supported; Search/AI content-gap corrections; AI search testing; 30-day follow-up audit; Final improvement report'),
]
MONTHLY = [
 ('Visibility Watch', 49, 'Website search-health monitoring; Publicly visible indexing issue checks; Broken page/link checks; SEO change review; Competitor change monitoring; AI search visibility testing; Content-gap checks; Business information inconsistency checks on the site; Page improvement opportunities; Quarterly deeper review; Simple report'),
 ('Visibility Care', 99, 'Everything in Visibility Watch; Monthly SEO/AEO review; Website copy adjustments; FAQ improvements; Meta/title updates; Internal-link adjustments; Schema updates where supported; Search-intent improvements; Competitor comparison; AI visibility testing; One meaningful website optimization/update monthly; Monthly report'),
 ('Visibility Growth', 199, 'Everything in Visibility Care; Deeper competitor monitoring; Keyword/topic research; AI-question research; Two substantial website content improvements each month; New/expanded FAQs; Service-page optimization; Supporting content where warranted; Local/service-area improvements; Internal-link strategy; Schema updates where supported; Content-gap monitoring; AI/search visibility testing; Monthly performance report; Quarterly deeper audit'),
]
BUNDLES = [
 ('Professional Website', 299, 'Professional website; Mobile optimization; SEO-ready structure; AI-search-ready structure; Forms where applicable; Owner customization controls'),
 ('Website + AI Visibility', 499, 'Professional website; AI/search research; Core page optimization; FAQs; Meta optimization; Local optimization; Schema where supported; AI search testing'),
 ('Website + Local Growth', 699, 'Professional website; Local SEO/AEO research; Competitor research; Expanded page optimization; Service/location research; FAQ optimization; Content-gap research; Schema where supported; Internal linking; AI visibility testing; 30-day follow-up'),
]
ONE_TIME_CHECKOUT = {
 'Google + AI Visibility Audit': 'https://payhip.com/b/2FdZQ',
 'AI Search Foundation': 'https://payhip.com/b/GUDOl',
 'Local SEO + AI Visibility': 'https://payhip.com/b/YpAd7',
 'AI Visibility Buildout': 'https://payhip.com/b/D8WzO',
}

def section(k, h, body, light=False):
 return '<section class="section'+(' light' if light else '')+'"><div class="wrap"><span class="eyebrow">'+k+'</span><h2>'+h+'</h2>'+body+'</div></section>'

def package_cards(packages, inquiry, kind):
 cards=[]
 for name, price, features in packages:
  badge='Recommended / Most Popular' if name=='Local SEO + AI Visibility' else {'once':'One-time visibility service','monthly':'Monthly visibility plan','bundle':'Website + visibility option'}[kind]
  amount=('Starting at ' if kind=='bundle' else '')+'$'+str(price)+('/month' if kind=='monthly' else ' one time')
  intro='<p>Professional Website is the existing $299 Website Only / Done-for-You option, shown here for comparison.</p>' if name=='Professional Website' else ''
  credit='<p>$99 can be credited toward a qualifying implementation package if you upgrade within 14 days.</p>' if price==99 and kind=='once' else ''
  items=''.join('<li>'+escape(item)+'</li>' for item in features.split('; '))
  action=('<a class="button" href="'+ONE_TIME_CHECKOUT[name]+'" target="_blank" rel="noopener noreferrer">View on Payhip ↗</a>' if kind=='once' else '<a class="button" href="'+escape(inquiry,quote=True)+'" target="_blank" rel="noopener noreferrer">Ask about '+escape(name)+'</a>')
  cards.append('<article class="card"><span class="badge">'+badge+'</span><h3>'+escape(name)+'</h3><strong class="price">'+amount+'</strong>'+intro+'<ul>'+items+'</ul>'+credit+action+'</article>')
 return '<div class="grid">'+''.join(cards)+'</div>'

def visibility_bundles(inquiry):
 return section('Website + visibility bundles','Build your website with search in mind.', '<p class="lead">Choose a website on its own or combine your build with expanded visibility work. These are website launch options, separate from intake and business-hub features.</p>'+package_cards(BUNDLES,inquiry,'bundle')+'<p>Starting prices depend on the agreed page count, services, locations and website requirements. Bundle scope is confirmed before purchase; visibility plans do not automatically add CRM, intake or client portals.</p>', True)

def visibility_page(inquiry):
 hero='<section class="hero"><div class="wrap"><span class="eyebrow">SEO + AI Search Visibility</span><h1>Get Found on Google + AI Search</h1><p class="lead">We optimize your website so search engines and AI-powered tools can better understand your business, services, locations, expertise, and the questions your customers are asking.</p></div></section>'
 hero+=section('One-time services','Choose your visibility starting point.', '<p class="lead">Improve visibility, discoverability and search readiness across Google and AI-powered search, including ChatGPT, Gemini, Perplexity and Bing/Copilot. Available for existing websites, even if we did not build yours.</p>'+package_cards(ONE_TIME,inquiry,'once'), True)
 hero+=section('Monthly visibility options','Keep your website clear and search-ready.','<p class="lead">Monthly checkout is not yet available. Ask about a plan; enrollment begins only after recurring billing is enabled and the scope is confirmed.</p>'+package_cards(MONTHLY,inquiry,'monthly')+'<p>Growth includes two substantial content improvements per month in total, replacing Care’s one-update allowance. Schema updates apply where the website platform supports them. Monitoring and reports focus on observable website and search signals; connected analytics are used when available.</p>')
 hero+=visibility_bundles(inquiry)
 hero+=section('Clear expectations','Visibility work with a defined scope.', '<p>These services improve how clearly your business can be understood online. Google rankings, ChatGPT recommendations, AI placement, traffic increases, leads and revenue are never guaranteed. AI search test results are snapshots and may vary by tool, wording, location and date.</p><p>Appropriate structured data is added only where supported and does not guarantee search features or AI recommendations. Location content reflects places you genuinely serve. We handle the agreed research, content and website updates; your role is to provide business facts and access, review recommendations and approve changes.</p><p>Packages focus on website research and optimization. They exclude manual backlink building, purchased links, bulk directory submissions, daily social posting, weekly Google Business posts, ongoing review-response or reputation management, and high-volume blogging.</p><p>Website page limits are total limits, not cumulative across package levels. Scope, platform access and qualifying audit-credit eligibility are confirmed before work begins. Monthly visibility plans are separate from website Managed Support and store-support plans.</p>')
 hero+=section('Get started','Tell us about your website.', '<p class="lead">Share your website, services and service areas so we can confirm the right package. Use the inquiry form and name the plan you are interested in.</p><a class="button" href="'+escape(inquiry,quote=True)+'" target="_blank" rel="noopener noreferrer">Request visibility services</a>', True)
 return hero
