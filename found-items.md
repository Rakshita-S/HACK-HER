<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header>
    <h1>UMass Amherst Lost and Found</h1>
  </header>
  <main>
    <section>
      <h2>Report a Lost Item</h2>
      <form id="report-form">
        <input type="text" id="item-name" placeholder="Item Name" required>
        <input type="text" id="item-description" placeholder="Item Description" required>
        <input type="text" id="contact-info" placeholder="Your Contact Info" required>
        <button type="submit">Submit</button>
      </form>
    </section>
    <section>
      <h2>Found Items</h2>
      <div id="found-items-list">
        <!-- Found items will be displayed here -->
        <div class="found-item">
          <h3>Item Name: Lost Wallet</h3>
          <p>Description: Black leather wallet found near the Student Union.</p>
        </div>
        <div class="found-item">
          <h3>Item Name: Blue Backpack</h3>
          <p>Description: Blue backpack with a UMass logo found in the library.</p>
        </div>
        <!-- More found items can be added here -->
      </div>
      <a href="main.md" class="button">Back to Main Page</a>
    </section>
  </main>
  <footer>
    <p>&copy; 2023 UMass Amherst Lost and Found</p>
  </footer>
</body>
</html>
