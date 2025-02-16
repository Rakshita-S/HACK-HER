const express = require('express');
const cookieParser = require('cookie-parser');
const multer = require('multer');
const path = require('path');

const app = express();
const upload = multer({ dest: 'uploads/' });

app.use(cookieParser());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Serve static files
app.use(express.static(path.join(__dirname, 'public')));

app.post('/login', (req, res) => {
  const { username, email, password, phoneNumber } = req.body;
  res.cookie('userInfo', JSON.stringify({ username, email, phoneNumber }), { maxAge: 7 * 24 * 60 * 60 * 1000 });
  res.redirect('/main.html');
});

app.post('/upload', upload.single('file'), (req, res) => {
  const { description } = req.body;
  const { filename } = req.file;
  const item = { filename, description };
  const items = req.cookies.items ? JSON.parse(req.cookies.items) : [];
  items.push(item);
  res.cookie('items', JSON.stringify(items), { maxAge: 7 * 24 * 60 * 60 * 1000 });
  res.send('File uploaded successfully');
});

app.get('/files', (req, res) => {
  const items = req.cookies.items ? JSON.parse(req.cookies.items) : [];
  res.json(items);
});

app.get('/main.html', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'main.html'));
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
