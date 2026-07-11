import os

# Create CSS folder
os.makedirs("portfolio/css", exist_ok=True)

css = """
/* ===============================
   CSS VARIABLES
================================ */

:root{
    --primary:#2563eb;
    --secondary:#1e40af;
    --background:#ffffff;
    --surface:#f5f5f5;
    --text:#222222;
    --heading:#111111;
    --border:#dddddd;
    --shadow:rgba(0,0,0,.10);
    --radius:12px;
    --transition:.3s ease;
    --max-width:1200px;
}

/* Dark Theme */

@media (prefers-color-scheme: dark){

:root{
    --background:#121212;
    --surface:#1f1f1f;
    --text:#eeeeee;
    --heading:#ffffff;
    --border:#444444;
    --shadow:rgba(255,255,255,.08);
}

}

/* Reset */

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

html{
    scroll-behavior:smooth;
}

body{
    font-family:Arial,Helvetica,sans-serif;
    background:var(--background);
    color:var(--text);
    line-height:1.6;

    display:grid;
    grid-template-rows:auto 1fr auto;
    min-height:100vh;
}

/* Skip Link */

.skip-link{
    position:absolute;
    left:-9999px;
}

.skip-link:focus{
    left:20px;
    top:20px;
    background:#000;
    color:#fff;
    padding:10px;
}

/* Header */

header{
    background:var(--surface);
    padding:20px;
    box-shadow:0 2px 10px var(--shadow);
}

/* Navigation */

nav ul{
    display:flex;
    flex-wrap:wrap;
    justify-content:center;
    gap:20px;
    list-style:none;
}

nav a{
    color:var(--text);
    text-decoration:none;
    font-weight:bold;
    transition:var(--transition);
}

nav a:hover{
    color:var(--primary);
}

/* Main */

main{
    width:min(90%, var(--max-width));
    margin:auto;
    padding:40px 0;
    display:grid;
    gap:40px;
}

/* Sections */

section{
    background:var(--surface);
    padding:30px;
    border-radius:var(--radius);
    box-shadow:0 5px 15px var(--shadow);
}

/* Project Grid */

.projects{
    display:grid;
    grid-template-columns:1fr;
    gap:20px;
}

article{
    background:var(--background);
    border:1px solid var(--border);
    padding:20px;
    border-radius:10px;
    transition:.3s;
}

article:hover{
    transform:translateY(-8px);
    box-shadow:0 10px 20px var(--shadow);
}

/* Form */

form{
    display:grid;
    gap:15px;
}

label{
    font-weight:bold;
}

input,
textarea{
    width:100%;
    padding:12px;
    border:1px solid var(--border);
    border-radius:8px;
    background:var(--background);
    color:var(--text);
}

button{
    background:var(--primary);
    color:white;
    border:none;
    padding:12px;
    border-radius:8px;
    cursor:pointer;
    transition:.3s;
}

button:hover{
    background:var(--secondary);
}

/* Footer */

footer{
    background:var(--surface);
    padding:20px;
    text-align:center;
}

/* Images */

img{
    max-width:100%;
    height:auto;
    display:block;
    border-radius:10px;
}

/* Accessibility */

a:focus,
button:focus,
input:focus,
textarea:focus{
    outline:3px solid var(--primary);
    outline-offset:3px;
}

/* Tablet */

@media (min-width:768px){

header{
    display:flex;
    justify-content:space-between;
    align-items:center;
}

.projects{
    grid-template-columns:repeat(2,1fr);
}

}

/* Desktop */

@media (min-width:1024px){

.projects{
    grid-template-columns:repeat(3,1fr);
}

main{
    gap:60px;
}

}

/* Large Desktop */

@media (min-width:1400px){

main{
    width:1200px;
}

}
"""

with open("portfolio/css/style.css", "w", encoding="utf-8") as file:
    file.write(css)

print("Advanced responsive CSS file created successfully!")