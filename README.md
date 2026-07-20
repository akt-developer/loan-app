<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Signal — Loan Risk Assessment</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css" />
</head>
<body>

<div class="mesh-bg">
  <div class="blob blob-1"></div>
  <div class="blob blob-2"></div>
  <div class="blob blob-3"></div>
  <div class="grid-overlay"></div>
</div>

<header class="topbar">
  <div class="topbar-inner">
    <div class="brand">
      <div class="brand-mark">
        <svg width="26" height="26" viewBox="0 0 26 26" fill="none">
          <path d="M3 17L9 9L14 14L23 4" stroke="url(#g1)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
          <defs><linearGradient id="g1" x1="3" y1="4" x2="23" y2="17"><stop stop-color="#FF9466"/><stop offset="1" stop-color="#8B7CF6"/></linearGradient></defs>
        </svg>
      </div>
      <span class="brand-name">Signal</span>
    </div>
    <span class="topbar-tag">Instant credit risk read</span>
  </div>
</header>

<main class="shell">

  <section class="hero">
    <p class="kicker">Underwriting · Automated first read</p>
    <h1>Know the risk<br/><span class="hero-accent">before you say yes.</span></h1>
    <p class="hero-sub">Fill in the applicant's details. A model trained on 22 repayment signals reads the file and returns a probability in real time — no spreadsheets, no waiting.</p>
  </section>

  <div class="workspace">

    <!-- LEFT: APPLICATION FORM -->
    <section class="card intake">
      <div class="card-head">
        <span class="step-dot">01</span>
        <h2>Applicant file</h2>
      </div>

      <form id="loan-form">

        <div class="group">
          <p class="group-label"><svg class="ic" viewBox="0 0 24 24"><path d="M12 12a4 4 0 100-8 4 4 0 000 8zM4 21c1.5-4 4.5-6 8-6s6.5 2 8 6" stroke="currentColor" stroke-width="1.8" fill="none" stroke-linecap="round"/></svg>Applicant</p>
          <div class="row">
            <label>Age
              <input type="number" name="age" min="18" max="100" value="30" required />
            </label>
            <label>Gender
              <select name="gender">
                <option value="female">Female</option>
                <option value="male">Male</option>
              </select>
            </label>
          </div>
          <div class="row">
            <label>Annual income (₹)
              <input type="number" name="income" min="0" value="600000" required />
            </label>
            <label>Years employed
              <input type="number" name="employment_experience" min="0" value="4" required />
            </label>
          </div>
          <div class="row">
            <label>Highest education
              <select name="education">
                <option value="Associate">Associate</option>
                <option value="High School">High School</option>
                <option value="Bachelor" selected>Bachelor</option>
                <option value="Master">Master</option>
                <option value="Doctorate">Doctorate</option>
              </select>
            </label>
            <label>Home ownership
              <select name="home_ownership">
                <option value="MORTGAGE">Mortgage</option>
                <option value="RENT">Rent</option>
                <option value="OWN">Own</option>
                <option value="OTHER">Other</option>
              </select>
            </label>
          </div>
        </div>

        <div class="group">
          <p class="group-label"><svg class="ic" viewBox="0 0 24 24"><rect x="3" y="6" width="18" height="13" rx="2" stroke="currentColor" stroke-width="1.8" fill="none"/><path d="M3 10h18M8 3v4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>Credit standing</p>
          <div class="row">
            <label>Credit score
              <input type="number" name="credit_score" min="300" max="850" value="680" required />
            </label>
            <label>Credit history (yrs)
              <input type="number" name="credit_history" min="0" value="6" required />
            </label>
          </div>
          <div class="row">
            <label>Previous loan on file
              <select name="previous_loan">
                <option value="No">No</option>
                <option value="Yes">Yes</option>
              </select>
            </label>
          </div>
        </div>

        <div class="group">
          <p class="group-label"><svg class="ic" viewBox="0 0 24 24"><path d="M4 12h16M14 6l6 6-6 6" stroke="currentColor" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>The request</p>
          <div class="row">
            <label>Loan amount (₹)
              <input type="number" name="loan_amount" min="0" value="200000" required />
            </label>
            <label>Interest rate (%)
              <input type="number" step="0.01" name="interest_rate" min="0" value="11.5" required />
            </label>
          </div>
          <div class="row">
            <label>Loan intent
              <select name="loan_intent">
                <option value="DEBTCONSOLIDATION">Debt consolidation</option>
                <option value="EDUCATION">Education</option>
                <option value="HOMEIMPROVEMENT">Home improvement</option>
                <option value="MEDICAL">Medical</option>
                <option value="PERSONAL">Personal</option>
                <option value="VENTURE">Venture</option>
              </select>
            </label>
            <label>Loan as % of income
              <input type="number" step="0.01" name="loan_percent_income" min="0" max="1" value="0.33" required />
            </label>
          </div>
        </div>

        <button type="submit" id="submit-btn">
          <span>Run the assessment</span>
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
      </form>
    </section>

    <!-- RIGHT: RESULT PANEL -->
    <section class="card verdict">
      <div class="card-head">
        <span class="step-dot">02</span>
        <h2>Determination</h2>
      </div>

      <div class="verdict-panel" id="verdict-panel">

        <div class="verdict-empty" id="verdict-empty">
          <div class="gauge-shell idle">
            <svg viewBox="0 0 200 200" width="200">
              <circle cx="100" cy="100" r="86" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="14"/>
            </svg>
          </div>
          <p>Submit the file on the left — the gauge lights up the moment the model responds.</p>
        </div>

        <div class="verdict-result" id="verdict-result" hidden>
          <div class="gauge-shell" id="gauge-shell">
            <svg class="gauge" viewBox="0 0 200 200" width="200">
              <defs>
                <linearGradient id="gaugeGradGood" x1="0" y1="0" x2="1" y2="1">
                  <stop offset="0%" stop-color="#34D399"/>
                  <stop offset="100%" stop-color="#8B7CF6"/>
                </linearGradient>
                <linearGradient id="gaugeGradBad" x1="0" y1="0" x2="1" y2="1">
                  <stop offset="0%" stop-color="#FF9466"/>
                  <stop offset="100%" stop-color="#FF5C7A"/>
                </linearGradient>
              </defs>
              <circle cx="100" cy="100" r="86" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="14"/>
              <circle id="gauge-fill" cx="100" cy="100" r="86" fill="none" stroke-width="14" stroke-linecap="round" transform="rotate(-90 100 100)"/>
            </svg>
            <div class="gauge-center">
              <span class="gauge-number" id="dial-number">--%</span>
              <span class="gauge-caption" id="dial-caption">default risk</span>
            </div>
          </div>

          <div class="badge-wrap">
            <div class="badge" id="stamp">Approved</div>
          </div>

          <dl class="ledger-lines" id="ledger-lines"></dl>
        </div>

        <div class="verdict-error" id="verdict-error" hidden></div>
      </div>

      <p class="footnote">Logistic regression · 22 signals · trained on historical repayment outcomes. A probability, not a promise — one input among several.</p>
    </section>

  </div>

</main>

<footer class="colophon">
  <span>Signal · Automated First Read</span>
  <span id="today"></span>
</footer>

<script src="script.js"></script>
</body>
</html>
