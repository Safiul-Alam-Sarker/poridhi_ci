const express = require('express');
const mongoose = require('mongoose');
const app = express();
app.use(express.json());

// MongoDB connection
const mongoURI = 'mongodb://db:27017/testdb';
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true });

const userSchema = new mongoose.Schema({
    name: String,
    email: String,
});

const User = mongoose.model('User', userSchema);

app.get('/users', async (req, res) => {
    const users = await User.find();
    res.json(users);
});

app.post('/add_user', async (req, res) => {
    const { name, email } = req.body;
    const user = new User({ name, email });
    await user.save();
    res.status(201).json({ message: 'User added successfully' });
});

app.listen(3000, () => {
    console.log('Server running on http://localhost:3000');
});
