# HACK-HER
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lost and Found</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header>
    <h1>UMass Amherst Lost and Found</h1>
    <nav>
      <ul>
        <li><a href="#lost-items">Lost Items</a></li>
        <li><a href="#found-items">Found Items</a></li>
        <li><a href="#report any item">Report</a></li>
      </ul>
    </nav>
  </header>
  <main>
    <section id="lost-items">
      <h2>Lost Items</h2>
      <div id="lost-items-list"></div>
    </section>
    <section id="found-items">
      <h2>Found Items</h2>
      <div id="found-items-list"></div>
    </section>
    <section id="report any item">
      <h2>Report Lost/Found Item</h2>
      <form id="report-form">
        <input type="text" id="item-name" placeholder="Item Name" required>
        <input type="text" id="item-description" placeholder="Item Description" required>
        <button type="submit">Submit</button>
      </form>
    </section>
  </main>
  <script src="script.js"></script>
</body>
</html>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UMass Amherst Lost and Found</title>
    
    <!-- Link to external CSS file -->
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <header>
        <h1>UMass Amherst Lost and Found</h1>
        <nav>
            <ul>
                <li><a href="report-lost.html">Report Lost Item</a></li>
                <li><a href="found-items.html">Found Items</a></li>
                <li><a href="contact.html">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section>
            <h2>Welcome to the UMass Amherst Lost and Found</h2>
            <p>If you've lost an item, you can report it here. If you've found something, check our list of found items and let us know if it's yours!</p>
            <a href="report-lost.html" class="button">Report a Lost Item</a>
        </section>
    </main>

    <footer>
        <p>© 2025 UMass Amherst</p>
    </footer>
</body>
</html>

