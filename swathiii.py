import os

# Create folders
os.makedirs("portfolio/css", exist_ok=True)

# ---------------- index.html ---------------- #
index_html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>John Doe | Portfolio</title>
<meta name="description" content="Accessible Portfolio Website">
<meta name="keywords" content="portfolio, HTML5, CSS3, Accessibility">
<meta name="author" content="John Doe">
<link rel="stylesheet" href="css/style.css">
</head>

<body>

<a href="#main-content" class="skip-link">Skip to main content</a>

<header>
    <h1>John Doe</h1>

    <nav aria-label="Primary Navigation">
        <ul>
            <li><a href="index.html" aria-current="page">Home</a></li>
            <li><a href="about.html">About</a></li>
            <li><a href="contact.html">Contact</a></li>
        </ul>
    </nav>
</header>

<main id="main-content">

<section>
<h2>Welcome</h2>
<p>I build accessible websites using semantic HTML5.</p>
</section>

<section>
<h2>Projects</h2>

<article>
<h3>Portfolio Website</h3>
<p>Semantic HTML5 Portfolio</p>
</article>

<article>
<h3>E-Commerce UI</h3>
<p>Responsive shopping website.</p>
</article>

</section>

</main>

<footer>
<p>&copy; 2026 John Doe</p>
</footer>

</body>
</html>
"""

# ---------------- about.html ---------------- #
about_html = """<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>About</title>

<link rel="stylesheet" href="css/style.css">

</head>

<body>

<a href="#main-content" class="skip-link">Skip to main content</a>

<header>

<h1>About Me</h1>

<nav aria-label="Primary Navigation">

<ul>
<li><a href="index.html">Home</a></li>
<li><a href="about.html" aria-current="page">About</a></li>
<li><a href="contact.html">Contact</a></li>
</ul>

</nav>

</header>

<main id="main-content">

<section>

<h2>Who I Am</h2>

<p>I create responsive and accessible websites.</p>

</section>

<section>

<h2>Skills</h2>

<ul>
<li>HTML5</li>
<li>CSS3</li>
<li>JavaScript</li>
<li>React</li>
<li>Accessibility</li>
</ul>

</section>

</main>

<footer>

<p>&copy; 2026 John Doe</p>

</footer>

</body>

</html>
"""

# ---------------- contact.html ---------------- #
contact_html = """<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Contact</title>

<link rel="stylesheet" href="css/style.css">

</head>

<body>

<a href="#main-content" class="skip-link">Skip to main content</a>

<header>

<h1>Contact</h1>

<nav aria-label="Primary Navigation">

<ul>
<li><a href="index.html">Home</a></li>
<li><a href="about.html">About</a></li>
<li><a href="contact.html" aria-current="page">Contact</a></li>
</ul>

</nav>

</header>

<main id="main-content">

<section>

<h2>Contact Form</h2>

<form aria-label="Contact Form">

<label for="name">Name</label>
<input type="text" id="name" required>

<label for="email">Email</label>
<input type="email" id="email" required>

<label for="subject">Subject</label>
<input type="text" id="subject" required>

<label for="message">Message</label>
<textarea id="message" rows="6" required></textarea>

<button type="submit">Send</button>

</form>

</section>

</main>

<footer>

<p>&copy; 2026 John Doe</p>

</footer>

</body>

</html>
"""

# ---------------- style.css ---------------- #
style_css = """*{
box-sizing:border-box;
}

body{
font-family:Arial,sans-serif;
margin:0;
line-height:1.6;
}

header,footer{
background:#f4f4f4;
padding:20px;
}

main{
padding:20px;
}

nav ul{
display:flex;
gap:20px;
list-style:none;
padding:0;
}

.skip-link{
position:absolute;
left:-9999px;
}

.skip-link:focus{
left:10px;
top:10px;
background:black;
color:white;
padding:10px;
}

input,
textarea,
button{
width:100%;
padding:10px;
margin-bottom:15px;
font-size:16px;
}

button{
cursor:pointer;
}

a:focus,
button:focus,
input:focus,
textarea:focus{
outline:3px solid blue;
}
"""

# Write files
with open("portfolio/index.html", "w", encoding="utf-8") as f:
    f.write(index_html)

with open("portfolio/about.html", "w", encoding="utf-8") as f:
    f.write(about_html)

with open("portfolio/contact.html", "w", encoding="utf-8") as f:
    f.write(contact_html)

with open("portfolio/css/style.css", "w", encoding="utf-8") as f:
    f.write(style_css)

print("Portfolio website generated successfully!")